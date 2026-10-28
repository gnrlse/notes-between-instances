"""Written during 012's blind review: lists long gaps in subagent transcripts (session-wide pauses).

  python3 -I pause_scan.py AGENTS_JSON TASKS_DIR

Prints trial ids, gap lengths and times, and synthetic-entry counts. No agent-written content.
"""
import json, sys
from datetime import datetime
agents = json.load(open(sys.argv[1]))
tasks = sys.argv[2]
def ts(r):
    t = r.get("timestamp")
    return datetime.fromisoformat(t.replace("Z", "+00:00")) if t else None
for tid, aid in sorted(agents.items()):
    rows = [json.loads(l) for l in open(f"{tasks}/{aid}.output") if l.strip()]
    stamped = [(i, ts(r), r) for i, r in enumerate(rows) if ts(r)]
    gaps = []
    for (i, a, ra), (j, b, rb) in zip(stamped, stamped[1:]):
        g = (b - a).total_seconds()
        if g > 300:
            gaps.append((g, i, j, a, b, ra.get("type"), rb.get("type"), (rb.get("message") or {}).get("model")))
    syn = sum(1 for r in rows if (r.get("message") or {}).get("model") == "<synthetic>")
    if gaps or syn:
        print(tid, "start", stamped[0][1].strftime("%H:%M:%S"), "end", stamped[-1][1].strftime("%H:%M:%S"), "synthetic", syn)
        for g, i, j, a, b, ta, tb, mb in gaps:
            print(f"   gap {g/60:.1f} min  {a.strftime('%H:%M:%S')} -> {b.strftime('%H:%M:%S')}  entry {i} {ta} -> {j} {tb} {mb or ''}")
