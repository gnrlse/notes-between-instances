"""Check blind judges' transcripts by script: models used and every tool call, without printing texts.

  python3 judgecheck.py JUDGE_AGENTS_JSON WAVE

JUDGE_AGENTS_JSON maps a judge part (R1a, S2c, P1b, ...) to its agent id. A clean judge
reads only its own input (judge/WAVE-PART.json) and writes only its own codes
(judge/WAVE-PART.codes.jsonl). Anything else is printed as a flag.
"""
import json
import sys
from pathlib import Path

TASKS = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/tasks")


def calls_of(path):
    models, calls = set(), []
    for line in path.read_text().splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if o.get("type") != "assistant":
            continue
        m = o.get("message", {}).get("model")
        if m:
            models.add(m)
        for c in o.get("message", {}).get("content", []) or []:
            if c.get("type") == "tool_use":
                inp = c.get("input") or {}
                arg = inp.get("file_path") or inp.get("path") or inp.get("command") or inp.get("pattern") or ""
                calls.append((c.get("name"), str(arg)))
    return models, calls


def main(agents_json, wave):
    agents = json.loads(Path(agents_json).read_text())
    bad = 0
    for part, aid in sorted(agents.items()):
        p = TASKS / f"{aid}.output"
        if not p.exists():
            print(f"{part}: no transcript")
            bad += 1
            continue
        models, calls = calls_of(p)
        own_in = f"{wave}-{part}.json"
        own_out = f"{wave}-{part}.codes.jsonl"
        flags = []
        for name, arg in calls:
            base = Path(arg).name if arg else ""
            if name == "Read" and base == own_in:
                continue
            if name == "Write" and base == own_out:
                continue
            if name == "SubagentHandback":
                continue
            flags.append(f"{name}({arg[:90]})")
        reads = sum(1 for n, a in calls if n == "Read" and Path(a).name == own_in)
        writes = sum(1 for n, a in calls if n == "Write" and Path(a).name == own_out)
        status = "ok" if not flags and writes >= 1 else "CHECK"
        bad += status != "ok"
        print(f"{part}: {status} models={sorted(models)} reads_own={reads} writes_own={writes} other={flags}")
    print(f"# {len(agents)} judges, {bad} to check")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
