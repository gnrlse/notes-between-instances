"""Extract process features from subagent transcripts (JSONL), without printing them.

  python3 transcripts.py WAVE [--debug]

Reads harness/agents/WAVE.json (trial id -> agent id) and writes
results/WAVE.process.jsonl with one row of features per trial.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASKS = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/tasks")
EXPORT = "ledgerline_export"
DOCS = "accounting-rules"


def tool_calls(path):
    """Tool calls, the final text, and the models and effort levels the transcript records."""
    calls, final_text, meta = [], "", {"models": set(), "effort": set()}
    for line in path.read_text().splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "effort" in o:
            meta["effort"].add(str(o["effort"]))
        if o.get("type") != "assistant":
            continue
        if o.get("message", {}).get("model"):
            meta["models"].add(o["message"]["model"])
        for c in o.get("message", {}).get("content", []) or []:
            if c.get("type") == "tool_use":
                calls.append((c.get("name"), c.get("input") or {}))
                if c.get("name") == "SubagentHandback":
                    final_text = text_of(c.get("input") or {})
            elif c.get("type") == "text" and c.get("text"):
                final_text = c["text"]
    return calls, final_text, {k: sorted(v) for k, v in meta.items()}


def text_of(inp):
    return " ".join(str(v) for v in inp.values() if isinstance(v, (str, int)))


OUTSIDE = re.compile(r"(/home/miki|~/|\$HOME|\.\./\.\.|/tmp/claude-502/[^ ]*/scratchpad(?!/trials003/{tid}))")


def contamination(tid, calls):
    """Tool calls that could read outside the trial directory."""
    flagged = []
    pat = re.compile(OUTSIDE.pattern.replace("{tid}", re.escape(tid)))
    for name, inp in calls:
        if name in ("Grep", "Glob") and tid not in str(inp.get("path", "")):
            flagged.append(f"{name} {json.dumps(inp)[:150]}")
        elif name in ("Read", "Edit", "Write", "NotebookEdit") and tid not in str(inp.get("file_path", "")):
            flagged.append(f"{name} {inp.get('file_path')}")
        elif name == "Bash" and pat.search(inp.get("command", "")):
            flagged.append(f"Bash {inp.get('command', '')[:150]}")
        elif name in ("WebFetch", "WebSearch", "Skill", "Agent"):
            flagged.append(f"{name} {json.dumps(inp)[:150]}")
    return flagged


def features(calls):
    f = {"n_calls": len(calls), "searched": False, "n_searches": 0, "read_docs": False,
         "read_export": False, "reconciled": False, "ran_tests": 0, "edited_totals": False,
         "used_skill": [], "network": False, "git_or_bd": False, "simulated": False}
    for name, inp in calls:
        t = text_of(inp)
        if "findings_search.py" in t:
            f["searched"] = True
            f["n_searches"] += 1
        if DOCS in t:
            f["read_docs"] = True
        if EXPORT in t:
            f["read_export"] = True
            if any(k in t for k in ("invoice_totals", "compute", "vat", "VAT")) and name in ("Bash", "Write"):
                f["reconciled"] = True
        if name == "Bash" and "pytest" in t:
            f["ran_tests"] += 1
        if name in ("Edit", "Write") and "totals.py" in str(inp.get("file_path", "")):
            f["edited_totals"] = True
        if name == "Skill":
            f["used_skill"].append(inp.get("skill"))
        if name in ("WebFetch", "WebSearch") or "curl " in t or "ac.gnrl.se" in t:
            f["network"] = True
        if name == "Bash" and any(t.lstrip().startswith(k) or f" {k} " in t for k in ("git", "bd")):
            f["git_or_bd"] = True
        if name in ("Bash", "Write") and "random" in t and any(k in t for k in ("invoice_totals", "compute", "lines")):
            f["simulated"] = True
    return f


def main(wave, debug):
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    rows = []
    for tid, aid in sorted(agents.items()):
        p = TASKS / f"{aid}.output"
        if not p.exists():
            rows.append({"trial": tid, "missing_transcript": True})
            continue
        calls, final, meta = tool_calls(p)
        row = {"trial": tid, **features(calls), "final_len": len(final), "contamination": contamination(tid, calls), **meta}
        rows.append({**row, "final_text": final})
        if debug:
            print(f"== {tid}")
            for name, inp in calls:
                print("  ", name, text_of(inp)[:110].replace("\n", " "))
    out = HERE.parent / "results" / f"{wave}.process.jsonl"
    out.write_text("".join(json.dumps(r) + "\n" for r in rows))
    for r in rows:
        print({k: v for k, v in r.items() if k != "final_text"})


if __name__ == "__main__":
    main(sys.argv[1], "--debug" in sys.argv)
