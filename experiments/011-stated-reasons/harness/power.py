"""Power of experiment 011's two confirmatory tests under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates the two tests (two-sided Fisher exact on cells pooled over the other factor,
Holm across the two) and reports how often each is supported: Holm-adjusted p < 0.05
with the difference in the stated direction. 010's pilot gave 0/10 adoptions searching
first and 1/10 reading first on this task, with the closed doc and the plain note.
"""
import random
import sys

from analyze import fisher, holm

SCENARIOS = {
    "nothing moves (all 5%)": dict(closed_plain=.05, closed_defused=.05, open_plain=.05, open_defused=.05),
    "defusing only, +25 points": dict(closed_plain=.05, closed_defused=.30, open_plain=.05, open_defused=.30),
    "open doc only, +25 points": dict(closed_plain=.05, closed_defused=.05, open_plain=.30, open_defused=.30),
    "both, +15 each, additive": dict(closed_plain=.05, closed_defused=.20, open_plain=.20, open_defused=.35),
    "both, +10 each, additive": dict(closed_plain=.05, closed_defused=.15, open_plain=.15, open_defused=.25),
    "only together (+30 in open_defused)": dict(closed_plain=.05, closed_defused=.05, open_plain=.05, open_defused=.35),
}


def simulate(rates, n, sims=4000, seed=11):
    rng = random.Random(seed)
    hits = {"H1": 0, "H2": 0}
    for _ in range(sims):
        k = {c: sum(rng.random() < p for _ in range(n)) for c, p in rates.items()}
        de, pl = k["closed_defused"] + k["open_defused"], k["closed_plain"] + k["open_plain"]
        op, cl = k["open_plain"] + k["open_defused"], k["closed_plain"] + k["closed_defused"]
        m = 2 * n
        adj = holm([fisher(de, m - de, pl, m - pl), fisher(op, m - op, cl, m - cl)])
        hits["H1"] += adj[0] < 0.05 and de > pl
        hits["H2"] += adj[1] < 0.05 and op > cl
    return {t: round(v / sims, 2) for t, v in hits.items()}


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [24]:
        print(f"n = {n} per cell")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
