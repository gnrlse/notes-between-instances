"""Agreement between refined-rubric judges D and E, and the refined pattern under
each coder and under the conservative 'both say yes' coding (exploratory).

  python3 refined_reliability.py
"""
import json
from pathlib import Path

from analyze import fisher, fmt
from merge_codes import kappa

HERE = Path(__file__).resolve().parent
EXP001 = HERE.parent.parent / "001-provenance-labels"
JUDGE = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/judge")
KEYS = ("mentions_relevant_note", "identity_as_reason", "outside_source_as_reason", "unverifiable_as_reason")
NAMED = ("same_model", "other_model", "human")


def load(path):
    return {r["trial"]: r for r in map(json.loads, path.read_text().splitlines()) if r}


def main():
    d, e = load(JUDGE / "refined-D.codes.jsonl"), load(JUDGE / "refined-E.codes.jsonl")
    trials = sorted(d)
    assert set(trials) == set(e), "D and E coded different sets"
    print("## D–E agreement (144 summaries)")
    for k in KEYS:
        xd, xe = [bool(d[t][k]) for t in trials], [bool(e[t][k]) for t in trials]
        agree = sum(x == y for x, y in zip(xd, xe))
        print(f"- {k}: {agree}/144 agree, kappa = {kappa(xd, xe):.2f} (D yes {sum(xd)}, E yes {sum(xe)})")

    assign = {**json.loads((EXP001 / "harness" / "assignments" / "main1.json").read_text()),
              **json.loads((HERE / "assignments" / "main2.json").read_text())}
    codings = {
        "D": lambda t, k: bool(d[t][k]),
        "E": lambda t, k: bool(e[t][k]),
        "both": lambda t, k: bool(d[t][k]) and bool(e[t][k]),
    }
    for name, code in codings.items():
        print(f"\n## Pooled 001+002, coding = {name}")
        u = [t for t, a in assign.items() if a["condition"] == "unknown"]
        n = [t for t, a in assign.items() if a["condition"] in NAMED]
        for k in KEYS[1:]:
            k1, k2 = sum(code(t, k) for t in u), sum(code(t, k) for t in n)
            p = fisher(k1, len(u) - k1, k2, len(n) - k2)
            per = ", ".join(f"{c} {sum(code(t, k) for t, a in assign.items() if a['condition'] == c)}/32" for c in NAMED)
            print(f"- {k}: unknown {fmt(k1, len(u))} vs named {fmt(k2, len(n))} [{per}]; exploratory p = {p:.4f}")


if __name__ == "__main__":
    main()
