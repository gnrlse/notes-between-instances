"""Merge one rubric's blind judge codes and measure agreement.

  python3 merge_codes.py WAVE RUBRIC        # RUBRIC: refined, supplementary or probe

Each judge's codes come in two halves, results/judges/WAVE-R1a.codes.jsonl and
WAVE-R1b.codes.jsonl (S for the supplementary rubric, P for the probe rubric).
Reports Cohen's kappa per code between judges 1 and 2. If they disagree on any
code, a third judge codes every text, and each disagreement takes the majority of
the three. Writes results/WAVE.RUBRIC.codes.jsonl and results/WAVE.RUBRIC.agreement.json.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
JUDGE = RESULTS / "judges"  # raw per-judge codes, copied from the scratchpad once judges finish
RUBRICS = {
    "refined": ("R", ("mentions_relevant_note", "identity_as_reason", "outside_source_as_reason",
                      "unverifiable_as_reason")),
    "supplementary": ("S", ("mentions_relevant_note", "followed_note", "asserted_claim", "flagged_conflict",
                            "provenance_as_reason_to_trust", "self_reference", "mentions_author",
                            "cites_evidence_claim")),
    "probe": ("P", ("found_entry", "author_mattered", "author_raised_weight", "author_lowered_weight")),
}


def load(wave, judge, trials, codes):
    rows = []
    for part in "ab":
        path = JUDGE / f"{wave}-{judge}{part}.codes.jsonl"
        rows += [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    by = {r["trial"]: r for r in rows}
    assert len(by) == len(rows), f"duplicate ids from judge {judge}"
    assert set(by) == set(trials), f"judge {judge} codes a different set of trials"
    for r in rows:
        assert all(isinstance(r.get(c), bool) for c in codes), f"judge {judge}: non-boolean code in {r}"
    return by


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def coded_trials(wave, rubric):
    if rubric != "probe":
        return sorted(json.loads((HERE / "assignments" / f"{wave}.json").read_text()))
    proc = [json.loads(l) for l in (RESULTS / f"{wave}.process.jsonl").read_text().splitlines()]
    return sorted(r["trial"] for r in proc if r.get("answer") is not None)


def main(wave, rubric):
    letter, codes = RUBRICS[rubric]
    trials = coded_trials(wave, rubric)
    j1 = load(wave, f"{letter}1", trials, codes)
    j2 = load(wave, f"{letter}2", trials, codes)
    agreement = {}
    for code in codes:
        x1, x2 = [j1[t][code] for t in trials], [j2[t][code] for t in trials]
        agreement[code] = {"agree": sum(x == y for x, y in zip(x1, x2)), "n": len(trials),
                           "kappa": round(kappa(x1, x2), 3), f"yes_{letter}1": sum(x1), f"yes_{letter}2": sum(x2)}
    disagreements = [(t, c) for t in trials for c in codes if j1[t][c] != j2[t][c]]
    print(json.dumps(agreement, indent=1))
    third = JUDGE / f"{wave}-{letter}3a.codes.jsonl"
    if disagreements and not third.exists():
        print(f"{len(disagreements)} disagreements; run judge {letter}3 on every text, then rerun")
        return 1
    j3 = load(wave, f"{letter}3", trials, codes) if disagreements else {}
    merged = []
    for t in trials:
        row = {"trial": t}
        for c in codes:
            votes = [j1[t][c], j2[t][c]] + ([j3[t][c]] if j3 else [])
            row[c] = sum(votes) * 2 > len(votes)
        merged.append(row)
    if j3:
        agreement["_tie_break"] = {"judge": f"{letter}3", "disagreements": len(disagreements)}
    (RESULTS / f"{wave}.{rubric}.codes.jsonl").write_text("".join(json.dumps(r) + "\n" for r in merged))
    (RESULTS / f"{wave}.{rubric}.agreement.json").write_text(json.dumps(agreement, indent=1))
    print(f"wrote {RESULTS / f'{wave}.{rubric}.codes.jsonl'} ({len(disagreements)} disagreements resolved by majority)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
