"""Write the blind judge's input: trial ids and summaries only, shuffled.

  python3 judge_input.py WAVE  -> scratchpad/judge/WAVE.json
"""
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
OUT = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/judge")


def main(wave):
    res = [json.loads(l) for l in (RESULTS / f"{wave}.jsonl").read_text().splitlines()]
    proc = {}
    pp = RESULTS / f"{wave}.process.jsonl"
    if pp.exists():
        proc = {r["trial"]: r for r in map(json.loads, pp.read_text().splitlines())}
    items = []
    for r in res:
        summary = r.get("notes") or proc.get(r["trial"], {}).get("final_text") or ""
        items.append({"id": r["trial"], "summary": summary.strip()})
    random.SystemRandom().shuffle(items)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{wave}.json").write_text(json.dumps(items, indent=1))
    print(OUT / f"{wave}.json", len(items), "summaries")


if __name__ == "__main__":
    main(sys.argv[1])
