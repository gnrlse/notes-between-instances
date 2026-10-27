"""Blind contamination detail: full text of every flagged call, and every git or bd call.

  python3 contamination_detail.py WAVE

For flagged calls (transcripts.contamination) prints the whole command or input, so a
truncated command can be checked for content reads (cat, head, grep, python, ...) on
paths outside the trial. For git or bd calls prints the command and the first two lines
of its output, which show where it ran. Prints no condition and no outcome.
"""
import json
import re
import sys
from pathlib import Path

from transcripts import TASKS, contamination
from contamination_review import calls_with_results

HERE = Path(__file__).resolve().parent
READERS = re.compile(r"(?<![\w-])(cat|head|tail|less|more|sed|awk|grep|rg|python3?|diff|cp|xxd|strings|wc|sort|uniq|open\(|source|tar|zip)(?![\w-])")
GIT = re.compile(r"(?:^|[;&|(\s])(git|bd)(?=\s|$)")


def main(wave):
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    for tid, aid in sorted(agents.items()):
        p = TASKS / f"{aid}.output"
        if not p.exists():
            continue
        calls, results = calls_with_results(p)
        out = []
        for cid, name, inp in calls:
            cmd = inp.get("command", "") if name == "Bash" else json.dumps(inp)
            is_flag = bool(contamination(tid, [(name, inp)]))
            is_git = name == "Bash" and bool(GIT.search(cmd))
            if not (is_flag or is_git):
                continue
            readers = sorted(set(m.group(1) for m in READERS.finditer(cmd)))
            tag = ("FLAG" if is_flag else "") + ("+GIT" if is_git else "")
            out.append(f"--- [{tag}] {name} readers={readers}\n    {cmd}")
            if is_git:
                res = results.get(cid, "").strip().splitlines()
                out.append("    git output: " + " / ".join(r[:140] for r in res[:2]) + f"  ({len(res)} lines)")
        if out:
            print(f"===== {tid}")
            print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1])
