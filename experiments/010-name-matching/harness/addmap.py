"""Record trial-to-agent mappings: python3 addmap.py WAVE TRIAL=AGENT [TRIAL=AGENT ...]"""
import json
import sys
from pathlib import Path

p = Path(__file__).resolve().parent / "agents" / f"{sys.argv[1]}.json"
m = json.loads(p.read_text()) if p.exists() else {}
for pair in sys.argv[2:]:
    t, a = pair.split("=")
    m[t] = a
p.write_text(json.dumps(m, indent=1))
total = len(json.loads((p.parent.parent / "assignments" / f"{sys.argv[1]}.json").read_text()))
print(f"{len(m)} of {total} mapped")
