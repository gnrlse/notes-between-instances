# Written during 013's blind review and reused in 014's to 020's harnesses before any trial. Reads no conditions or outcomes.
"""Structure around interrupted responses: entry kinds, times and tool names only, no content."""
import json, sys
from pathlib import Path

CUTOFF = "Your response above was cut off mid-stream"
agents = json.loads(Path(sys.argv[1]).read_text())
tasks = Path(sys.argv[2])
for tid in sys.argv[3:]:
    rows = []
    for line in (tasks / f"{agents[tid]}.output").read_text().splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = o.get("type")
        ts = str(o.get("timestamp", ""))[11:19]
        m = o.get("message") or {}
        if t == "assistant":
            if o.get("isApiErrorMessage") or m.get("model") == "<synthetic>":
                kind = "SYNTHETIC"
            else:
                names = [c.get("name") for c in m.get("content") or [] if c.get("type") == "tool_use"]
                texts = sum(1 for c in m.get("content") or [] if c.get("type") == "text")
                kind = "asst " + (",".join(names) if names else f"text x{texts}")
        elif t == "user":
            c = m.get("content")
            if isinstance(c, str):
                kind = "CUTOFF-NOTICE" if c.startswith(CUTOFF) else f"user text len={len(c)}"
            else:
                kinds = [x.get("type") for x in c or [] if isinstance(x, dict)]
                kind = "user " + ",".join(kinds)
        else:
            kind = str(t)
        rows.append((ts, kind))
    print(f"== {tid}: {len(rows)} entries")
    hits = [i for i, (_, k) in enumerate(rows) if k in ("SYNTHETIC", "CUTOFF-NOTICE")]
    hb = [i for i, (_, k) in enumerate(rows) if "SubagentHandback" in k]
    print("interruptions at", hits, "| handback at", hb)
    show = set()
    for i in hits:
        show.update(range(max(0, i - 3), min(len(rows), i + 4)))
    for i in sorted(show):
        print(i, *rows[i])
    print("last:", len(rows) - 1, *rows[-1])
