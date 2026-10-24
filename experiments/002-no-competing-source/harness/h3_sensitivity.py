"""H3 under each coding (judge A, judge B, majority of A/B/C), plus the exploratory
refined-reason codes (judge D) across experiments 001 and 002.

  python3 h3_sensitivity.py            # writes results/main2.resolutions.json, prints the report
"""
import json
from pathlib import Path

from analyze import fisher, fmt

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
JUDGE = HERE.parent / "results" / "judges"  # raw per-judge codes, copied from the session scratchpad
EXP001 = EXP.parent / "001-provenance-labels"
NAMED = ("same_model", "other_model", "human")


def load_codes(path):
    return {r["trial"]: r for r in map(json.loads, path.read_text().splitlines()) if r}


def h3_line(label, codes, assignment):
    by = {c: [t for t, a in assignment.items() if a["condition"] == c] for c in ("unknown",) + NAMED}
    k1 = sum(bool(codes[t]["author_as_reason"]) for t in by["unknown"])
    named = [t for c in NAMED for t in by[c]]
    k2 = sum(bool(codes[t]["author_as_reason"]) for t in named)
    p = fisher(k1, len(by["unknown"]) - k1, k2, len(named) - k2)
    per = ", ".join(f"{c} {sum(bool(codes[t]['author_as_reason']) for t in by[c])}/{len(by[c])}" for c in NAMED)
    return f"- {label}: unknown {k1}/{len(by['unknown'])} vs named {k2}/{len(named)} ({per}); p = {p:.3f}"


def main():
    a, b, c = (load_codes(JUDGE / f"main2-{k}.codes.jsonl") for k in "ABC")
    trials = sorted(a)
    # majority of A, B, C for author_as_reason; all other codes agreed between A and B
    resolutions, majority = {}, {}
    for t in trials:
        votes = [bool(x[t]["author_as_reason"]) for x in (a, b, c)]
        majority[t] = dict(a[t], author_as_reason=sum(votes) >= 2)
        if votes[0] != votes[1]:
            resolutions[t] = {"author_as_reason": votes[2]}
    (EXP / "results" / "main2.resolutions.json").write_text(json.dumps(resolutions, indent=1))
    agree_ca = sum(bool(c[t]["author_as_reason"]) == bool(a[t]["author_as_reason"]) for t in trials)
    agree_cb = sum(bool(c[t]["author_as_reason"]) == bool(b[t]["author_as_reason"]) for t in trials)
    print(f"judge C agrees with A on {agree_ca}/72 and with B on {agree_cb}/72 (author_as_reason); "
          f"{len(resolutions)} disputes resolved by C")

    assignment = json.loads((HERE / "assignments" / "main2.json").read_text())
    print("\n## H3 (pre-registered): author given as a reason, unknown vs named labels")
    print(h3_line("majority of A, B, C (primary)", majority, assignment))
    print(h3_line("judge A alone", a, assignment))
    print(h3_line("judge B alone", b, assignment))

    # exploratory refined codes, both experiments
    d = load_codes(JUDGE / "refined-D.codes.jsonl")
    a1 = json.loads((EXP001 / "harness" / "assignments" / "main1.json").read_text())
    print("\n## Exploratory: refined reasons (judge D), by label")
    print("| experiment | condition | n | identity as reason | outside source as reason | unverifiable as reason |")
    print("| --- | --- | --- | --- | --- | --- |")
    pooled = {}
    for name, assign in (("001", a1), ("002", assignment)):
        for cond in ("unknown",) + NAMED:
            ts = [t for t, x in assign.items() if x["condition"] == cond]
            ks = [sum(bool(d[t][k]) for t in ts) for k in ("identity_as_reason", "outside_source_as_reason", "unverifiable_as_reason")]
            print(f"| {name} | {cond} | {len(ts)} | " + " | ".join(fmt(k, len(ts)) for k in ks) + " |")
            pooled.setdefault(cond, []).extend(ts)
    print()
    for key in ("identity_as_reason", "outside_source_as_reason", "unverifiable_as_reason"):
        u = pooled["unknown"]
        n = [t for cnd in NAMED for t in pooled[cnd]]
        k1, k2 = sum(bool(d[t][key]) for t in u), sum(bool(d[t][key]) for t in n)
        p = fisher(k1, len(u) - k1, k2, len(n) - k2)
        print(f"- {key}, pooled 001+002: unknown {k1}/{len(u)} vs named {k2}/{len(n)}; exploratory p = {p:.4f}")


if __name__ == "__main__":
    main()
