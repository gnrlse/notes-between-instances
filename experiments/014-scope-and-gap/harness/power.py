"""Power of experiment 014's confirmatory tests under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates both tests (two-sided Fisher exact, one_line against two_line and gap against
two_line, Holm across the two) and reports how often each is supported: adjusted p < 0.05
with adoption lower than under two_line. 007's search-first, plain-notice cell, which
two_line repeats, adopted 45/72 (63%).
"""
import random
import sys

from analyze import fisher, holm

# (two_line, one_line, gap)
SCENARIOS = {
    "nothing moves (60%, 60%, 60%)": (.60, .60, .60),
    "only gap moves (60%, 60%, 10%)": (.60, .60, .10),
    "one_line -15 points (60%, 45%, 10%)": (.60, .45, .10),
    "one_line -25 points (60%, 35%, 10%)": (.60, .35, .10),
    "one_line -35 points (60%, 25%, 10%)": (.60, .25, .10),
    "both -20 points (60%, 40%, 40%)": (.60, .40, .40),
}


def simulate(rates, n, sims=4000, seed=14):
    rng = random.Random(seed)
    base, one_line, gap = rates
    hits = [0, 0]
    for _ in range(sims):
        k0 = sum(rng.random() < base for _ in range(n))
        ks = [sum(rng.random() < r for _ in range(n)) for r in (one_line, gap)]
        ps = [fisher(k, n - k, k0, n - k0) for k in ks]
        for i, (k, pa) in enumerate(zip(ks, holm(ps))):
            hits[i] += pa < 0.05 and k < k0
    return [round(h / sims, 2) for h in hits]


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [50]:
        print(f"n = {n} per cell (H1 one_line, H2 gap)")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
