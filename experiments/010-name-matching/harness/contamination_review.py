"""Show each flagged trial's outside calls, for the blind contamination review.

  python3 contamination_review.py WAVE > SCRATCH/contam_review_WAVE.txt

For every trial with a flagged call before the follow-up question (transcripts.py's
check), prints the call and, from its tool result, how many output lines name paths
outside the trial directory, with a few examples. Prints no condition and no outcome.
The reviewer then writes results/WAVE.contamination-review.json by the pre-registered
rule: reading a file's contents outside the trial (other than system or library
files) or any network request excludes; listings and the agent's own scratch files don't.
"""
import json
import re
import sys
from pathlib import Path

from transcripts import MARKER, TASKS, contamination, is_probe

HERE = Path(__file__).resolve().parent
PATHS = re.compile(r"(/home/miki[^\s'\"]*|/tmp/claude-502/[^\s'\"]*)")


def result_text(c):
    content = c.get("content")
    if isinstance(content, list):
        return "\n".join(str(x.get("text", "")) for x in content if isinstance(x, dict))
    return str(content or "")


def calls_with_results(path):
    calls, results = [], {}
    for line in path.read_text().splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if is_probe(o):
            break
        for c in (o.get("message") or {}).get("content", []) or []:
            if not isinstance(c, dict):
                continue
            if c.get("type") == "tool_use":
                calls.append((c.get("id"), c.get("name"), c.get("input") or {}))
            elif c.get("type") == "tool_result":
                results[c.get("tool_use_id")] = result_text(c)
    return calls, results


def main(wave):
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    for tid, aid in sorted(agents.items()):
        p = TASKS / f"{aid}.output"
        if not p.exists():
            continue
        calls, results = calls_with_results(p)
        flagged = []
        for cid, name, inp in calls:
            if contamination(tid, [(name, inp)]):
                flagged.append((cid, name, inp))
        if not flagged:
            continue
        print(f"===== {tid}")
        for cid, name, inp in flagged:
            shown = inp.get("command") or inp.get("file_path") or json.dumps(inp)
            print(f"--- {name}: {str(shown)[:400]}")
            out = results.get(cid, "")
            lines = out.splitlines()
            outside = [l for l in lines if any(tid not in m for m in PATHS.findall(l))]
            print(f"    output: {len(lines)} lines; lines naming outside paths: {len(outside)}")
            for l in outside[:6]:
                print("      |", l[:200])


if __name__ == "__main__":
    main(sys.argv[1])
