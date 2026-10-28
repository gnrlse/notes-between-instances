"""Power of experiment 015's confirmatory tests under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates both tests (two-sided Fisher exact, owner against gap and check against gap, Holm
across the two) and reports how often each is supported: adjusted p < 0.05 with adoption
lower than under gap. 014's gap cell, which gap repeats, adopted 26/50 (52%).
"""
import random
import sys

from analyze import fisher, holm

# (gap, owner, check)
SCENARIOS = {
    "nothing moves (50%, 50%, 50%)": (.50, .50, .50),
    "only owner moves (50%, 10%, 50%)": (.50, .10, .50),
    "owner -40, check -20 (50%, 10%, 30%)": (.50, .10, .30),
    "owner -40, check -25 (50%, 10%, 25%)": (.50, .10, .25),
    "both -30 (50%, 20%, 20%)": (.50, .20, .20),
    "owner -20, check -10 (50%, 30%, 40%)": (.50, .30, .40),
    "both -15 (50%, 35%, 35%)": (.50, .35, .35),
}


def simulate(rates, n, sims=4000, seed=15):
    rng = random.Random(seed)
    base, owner, check = rates
    hits = [0, 0]
    for _ in range(sims):
        k0 = sum(rng.random() < base for _ in range(n))
        ks = [sum(rng.random() < r for _ in range(n)) for r in (owner, check)]
        ps = [fisher(k, n - k, k0, n - k0) for k in ks]
        for i, (k, pa) in enumerate(zip(ks, holm(ps))):
            hits[i] += pa < 0.05 and k < k0
    return [round(h / sims, 2) for h in hits]


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [50]:
        print(f"n = {n} per cell (H1 owner, H2 check)")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
