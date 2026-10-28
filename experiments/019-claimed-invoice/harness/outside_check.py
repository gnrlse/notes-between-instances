# Written during 013's blind review and reused in 014's to 019's harnesses before any trial. Reads no conditions or outcomes.
"""Independent count of tool calls naming paths outside each trial. Counts only, no content."""
import json, re, sys
from collections import Counter
from pathlib import Path

agents = json.loads(Path(sys.argv[1]).read_text())
tasks = Path(sys.argv[2])
other_trial = Counter(); home = Counter(); scratch_other = Counter(); total = Counter(); abs_own = Counter()
for tid, aid in agents.items():
    for line in (tasks / f"{aid}.output").read_text().splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if o.get("type") != "assistant":
            continue
        for c in (o.get("message") or {}).get("content") or []:
            if c.get("type") != "tool_use":
                continue
            s = json.dumps(c.get("input") or {})
            total[tid] += 1
            ids = set(re.findall(r"trials019/(main19-[0-9a-f]{6})", s))
            if ids - {tid}:
                other_trial[tid] += 1
            if ids == {tid}:
                abs_own[tid] += 1
            if re.search(r"/home/|~/|\$HOME", s):
                home[tid] += 1
            for m in re.finditer(r"scratchpad(/[^\s\"']*)?", s):
                rest = m.group(1) or ""
                if not rest.startswith(f"/trials019/{tid}"):
                    scratch_other[tid] += 1
print("trials:", len(agents), "| tool calls:", sum(total.values()))
print("calls naming own trial path:", sum(abs_own.values()), "in", len(abs_own), "trials")
print("calls naming another trial:", dict(other_trial))
print("calls naming home paths:", dict(home))
print("calls naming scratchpad outside own trial:", dict(scratch_other))
