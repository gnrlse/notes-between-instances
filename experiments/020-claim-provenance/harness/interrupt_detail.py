# Written during 013's blind review and reused in 014's to 020's harnesses before any trial. Reads no conditions or outcomes.
"""Usage, stop reasons and message ids around an interruption; harness notices only by prefix. No agent content."""
import json, sys
from pathlib import Path

agents = json.loads(Path(sys.argv[1]).read_text())
tasks = Path(sys.argv[2])
tid, lo, hi = sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
rows = []
for line in (tasks / f"{agents[tid]}.output").read_text().splitlines():
    try:
        rows.append(json.loads(line))
    except json.JSONDecodeError:
        pass
for i in range(lo, hi + 1):
    o = rows[i]
    m = o.get("message") or {}
    u = m.get("usage") or {}
    info = {"type": o.get("type"), "ts": str(o.get("timestamp", ""))[11:19], "id": str(m.get("id", ""))[-8:],
            "model": m.get("model"), "stop": m.get("stop_reason"), "out": u.get("output_tokens"),
            "apiErr": o.get("isApiErrorMessage")}
    if o.get("type") == "assistant" and m.get("model") == "<synthetic>":
        t = " ".join(c.get("text", "") for c in m.get("content") or [] if c.get("type") == "text")
        info["synthetic_prefix"] = t[:45]
    if o.get("type") == "user" and isinstance(m.get("content"), str):
        info["notice_prefix"] = m["content"][:45]
    asst = sum(1 for r in rows[:i] if r.get("type") == "assistant" and (r.get("message") or {}).get("model") != "<synthetic>")
    info["assistant_entries_before"] = asst
    print(i, {k: v for k, v in info.items() if v not in (None, "")})
ids = []
for r in rows:
    if r.get("type") == "assistant":
        mid = (r.get("message") or {}).get("id")
        if mid and mid not in ids:
            ids.append(mid)
print("distinct assistant messages:", len(ids))
