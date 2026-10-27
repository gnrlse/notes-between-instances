"""Power of experiment 008's two confirmatory tests under plausible true rates.

  python3 power.py

Simulates the two tests (two-sided Fisher exact, search first against read first, within
each truth condition, Holm across the two) and reports how often each is supported:
Holm-adjusted p < 0.05 with adoption higher when searching first. Also reports how often
the 95% interval of the difference between the two order effects excludes zero (E1). In
007, with no examples file and the note wrong, adoption under the plain notice was 45/72
searching first and 20/72 reading first.
"""
import random

from analyze import fisher, holm

SCENARIOS = {
    "examples ignored: 007's rates in both truth conditions": dict(search_subtotal=.62, inspect_subtotal=.28, search_per_line=.62, inspect_per_line=.28),
    "judgement: reading first cuts only wrong uptake": dict(search_subtotal=.30, inspect_subtotal=.11, search_per_line=.89, inspect_per_line=.85),
    "skepticism: reading first cuts both by 20 points": dict(search_subtotal=.40, inspect_subtotal=.20, search_per_line=.85, inspect_per_line=.65),
    "half of 007's gap when wrong, none when right": dict(search_subtotal=.35, inspect_subtotal=.18, search_per_line=.88, inspect_per_line=.88),
    "evidence decides: no order effect": dict(search_subtotal=.12, inspect_subtotal=.10, search_per_line=.90, inspect_per_line=.90),
}


def simulate(rates, n=72, sims=4000, seed=8, draws=400):
    rng = random.Random(seed)
    hits = {"H1": 0, "H2": 0, "E1 difference excludes 0": 0}
    for _ in range(sims):
        k = {c: sum(rng.random() < p for _ in range(n)) for c, p in rates.items()}
        sw, iw, sr, ir = k["search_subtotal"], k["inspect_subtotal"], k["search_per_line"], k["inspect_per_line"]
        adj = holm([fisher(sw, n - sw, iw, n - iw), fisher(sr, n - sr, ir, n - ir)])
        hits["H1"] += adj[0] < 0.05 and sw > iw
        hits["H2"] += adj[1] < 0.05 and sr > ir
        b = lambda x: rng.betavariate(x + 0.5, n - x + 0.5)
        diffs = sorted((b(sw) - b(iw)) - (b(sr) - b(ir)) for _ in range(draws))
        hits["E1 difference excludes 0"] += diffs[int(.025 * draws)] > 0 or diffs[int(.975 * draws)] < 0
    return {t: round(v / sims, 2) for t, v in hits.items()}


if __name__ == "__main__":
    for name, rates in SCENARIOS.items():
        print(f"{name}: {simulate(rates)}")
