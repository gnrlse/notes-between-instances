"""Write blind judge inputs: trial ids and summaries only, freshly shuffled per judge.

  python3 judge_input.py WAVE JUDGE [JUDGE ...]  -> scratchpad/judge/WAVE-JUDGE.json

The summary is the trial's NOTES.md, or the agent's final reply if NOTES.md is missing.
"""
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
OUT = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/judge")


def main(wave, judges):
    res = [json.loads(l) for l in (RESULTS / f"{wave}.jsonl").read_text().splitlines()]
    proc = {r["trial"]: r for r in map(json.loads, (RESULTS / f"{wave}.process.jsonl").read_text().splitlines())}
    items, fallback = [], 0
    for r in res:
        summary = r.get("notes")
        if not summary:
            fallback += 1
            summary = proc.get(r["trial"], {}).get("final_text") or ""
        items.append({"id": r["trial"], "summary": summary.strip()})
    OUT.mkdir(parents=True, exist_ok=True)
    for j in judges:
        xs = items[:]
        random.SystemRandom().shuffle(xs)
        (OUT / f"{wave}-{j}.json").write_text(json.dumps(xs, indent=1))
        print(OUT / f"{wave}-{j}.json")
    print(len(items), "summaries;", fallback, "fell back to the final reply")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
