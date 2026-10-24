"""Merge the two blind judges' codes and measure their agreement.

  python3 merge_codes.py WAVE [resolutions.json]

Reads scratchpad/judge/WAVE-A.codes.jsonl and WAVE-B.codes.jsonl, reports
Cohen's kappa per code, and writes results/WAVE.codes.jsonl. A disagreement
needs a resolution {trial: {code: bool}}, decided blind to condition.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
JUDGE = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/judge")
CODES = ("mentions_note", "flagged_conflict", "asserted_claim", "says_verified_against_export",
         "cites_author", "author_as_reason")


def load(path):
    rows = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    by = {r["trial"]: r for r in rows}
    assert len(by) == len(rows), f"duplicate ids in {path}"
    return by


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def main(wave, resolutions):
    a, b = load(JUDGE / f"{wave}-A.codes.jsonl"), load(JUDGE / f"{wave}-B.codes.jsonl")
    trials = sorted(json.loads((HERE / "assignments" / f"{wave}.json").read_text()))
    missing = [t for t in trials if t not in a or t not in b]
    assert not missing, f"missing codes for {missing}"
    agreement, merged, open_items = {}, {}, []
    for code in CODES:
        xa = [bool(a[t][code]) for t in trials]
        xb = [bool(b[t][code]) for t in trials]
        agreement[code] = {"agree": sum(x == y for x, y in zip(xa, xb)), "n": len(trials),
                           "kappa": round(kappa(xa, xb), 3), "yes_A": sum(xa), "yes_B": sum(xb)}
    for t in trials:
        row = {"trial": t}
        for code in CODES:
            va, vb = bool(a[t][code]), bool(b[t][code])
            if va == vb:
                row[code] = va
            elif t in resolutions and code in resolutions[t]:
                row[code] = bool(resolutions[t][code])
            else:
                row[code] = None
                open_items.append((t, code, va, vb))
        merged[t] = row
    print(json.dumps(agreement, indent=1))
    if open_items:
        print(f"{len(open_items)} disagreements need a blind resolution:")
        for t, code, va, vb in open_items:
            print(f"  {t} {code}: A={va} B={vb}")
        return 1
    (RESULTS / f"{wave}.codes.jsonl").write_text("".join(json.dumps(r) + "\n" for r in merged.values()))
    (RESULTS / f"{wave}.agreement.json").write_text(json.dumps(agreement, indent=1))
    print("wrote", RESULTS / f"{wave}.codes.jsonl")
    return 0


if __name__ == "__main__":
    res = json.loads(Path(sys.argv[2]).read_text()) if len(sys.argv) > 2 else {}
    sys.exit(main(sys.argv[1], res))
