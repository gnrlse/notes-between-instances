"""Write blind judge inputs: trial ids and texts only, freshly shuffled per judge, split in halves.

  python3 judge_input.py WAVE KIND JUDGE [JUDGE ...]
      KIND: summary or answer  ->  scratchpad/judge/WAVE-JUDGE{a,b}.json and the filled-in prompts

A summary is the trial's NOTES.md from its snapshot, or the agent's final reply before
the follow-up question if NOTES.md is missing. An answer is the agent's reply to the
follow-up question. Each judge's shuffled list is split into halves a and b, coded by
separate agents, so no agent holds more than half the texts in context.
"""
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
OUT = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/judge")
RUBRIC = {"R": "judge_refined.txt", "S": "judge_supplementary.txt", "P": "judge_probe.txt"}


def texts(wave, kind):
    res = [json.loads(l) for l in (RESULTS / f"{wave}.jsonl").read_text().splitlines()]
    proc = {r["trial"]: r for r in map(json.loads, (RESULTS / f"{wave}.process.jsonl").read_text().splitlines())}
    items, fallback = [], 0
    for r in res:
        if kind == "summary":
            text = r.get("notes")
            if not text:
                fallback += 1
                text = proc.get(r["trial"], {}).get("final_text") or ""
        else:
            text = proc.get(r["trial"], {}).get("answer")
            if text is None:
                fallback += 1
                continue
        items.append({"id": r["trial"], kind: text.strip()})
    note = "fell back to the final reply" if kind == "summary" else "had no answer and were left out"
    print(len(items), f"{kind}s;", fallback, note)
    return items


def main(wave, kind, judges):
    items = texts(wave, kind)
    OUT.mkdir(parents=True, exist_ok=True)
    for j in judges:
        xs = items[:]
        random.SystemRandom().shuffle(xs)
        half = (len(xs) + 1) // 2
        rubric = (HERE / RUBRIC[j[0]]).read_text()
        for part, chunk in (("a", xs[:half]), ("b", xs[half:])):
            path = OUT / f"{wave}-{j}{part}.json"
            out = OUT / f"{wave}-{j}{part}.codes.jsonl"
            path.write_text(json.dumps(chunk, indent=1))
            prompt = rubric.replace("{path}", str(path)).replace("{out}", str(out)).replace("{n}", str(len(chunk)))
            (OUT / f"{wave}-{j}{part}.prompt.txt").write_text(prompt)
            print(path, len(chunk))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
