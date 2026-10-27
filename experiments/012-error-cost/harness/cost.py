"""Token usage and wall time from subagent transcripts, without printing their contents.

  python3 cost.py AGENTS_JSON

AGENTS_JSON maps a trial or judge id to an agent id. Usage is summed once per API
message id (a streamed message is recorded several times with the same usage).
"""
import json
import sys
from datetime import datetime
from pathlib import Path

TASKS = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/tasks")


def usage(path):
    seen, tot, times = set(), {"input": 0, "cache_write": 0, "cache_read": 0, "output": 0}, []
    for line in path.read_text().splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if o.get("timestamp"):
            times.append(o["timestamp"])
        if o.get("type") != "assistant":
            continue
        m = o.get("message", {})
        mid = m.get("id")
        u = m.get("usage")
        if not u or not mid or mid in seen:
            continue
        seen.add(mid)
        tot["input"] += u.get("input_tokens", 0) or 0
        tot["cache_write"] += u.get("cache_creation_input_tokens", 0) or 0
        tot["cache_read"] += u.get("cache_read_input_tokens", 0) or 0
        tot["output"] += u.get("output_tokens", 0) or 0
    return tot, times


def main(agents_json):
    agents = json.loads(Path(agents_json).read_text())
    grand = {"input": 0, "cache_write": 0, "cache_read": 0, "output": 0}
    first, last, n = None, None, 0
    for key, aid in agents.items():
        p = TASKS / f"{aid}.output"
        if not p.exists():
            continue
        n += 1
        tot, times = usage(p)
        for k in grand:
            grand[k] += tot[k]
        if times:
            first = min(first or times[0], min(times))
            last = max(last or times[-1], max(times))
    unc = grand["input"] + grand["cache_write"] + grand["output"]
    print(f"{n} transcripts; uncached {unc/1e6:.1f}M (input {grand['input']/1e6:.2f}M, cache writes {grand['cache_write']/1e6:.1f}M, "
          f"output {grand['output']/1e6:.2f}M); cache reads {grand['cache_read']/1e6:.0f}M; per transcript {unc/max(n,1)/1e3:.0f}k uncached")
    if first and last:
        f = datetime.fromisoformat(first.replace("Z", "+00:00"))
        l = datetime.fromisoformat(last.replace("Z", "+00:00"))
        print(f"first {first}  last {last}  span {(l - f).total_seconds()/60:.0f} min")


if __name__ == "__main__":
    main(sys.argv[1])
