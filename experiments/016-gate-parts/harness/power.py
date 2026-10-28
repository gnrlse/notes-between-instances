"""Power of experiment 016's confirmatory tests under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates both tests (two-sided Fisher exact, instr against gap and pending against gap, Holm
across the two) and reports how often each is supported: adjusted p < 0.05 with adoption
lower than under gap. The gap item, which gap repeats, adopted 26/50 in 014 and 21/50 in 015.
"""
import random
import sys

from analyze import fisher, holm

# (gap, instr, pending)
SCENARIOS = {
    "nothing moves (45%, 45%, 45%)": (.45, .45, .45),
    "only instr moves (45%, 0%, 45%)": (.45, .00, .45),
    "instr to 0, pending -20 (45%, 0%, 25%)": (.45, .00, .25),
    "instr to 5, pending -25 (45%, 5%, 20%)": (.45, .05, .20),
    "both -30 (45%, 15%, 15%)": (.45, .15, .15),
    "instr -25, pending -15 (45%, 20%, 30%)": (.45, .20, .30),
    "both -15 (45%, 30%, 30%)": (.45, .30, .30),
}


def simulate(rates, n, sims=4000, seed=16):
    rng = random.Random(seed)
    base, instr, pending = rates
    hits = [0, 0]
    for _ in range(sims):
        k0 = sum(rng.random() < base for _ in range(n))
        ks = [sum(rng.random() < r for _ in range(n)) for r in (instr, pending)]
        ps = [fisher(k, n - k, k0, n - k0) for k in ks]
        for i, (k, pa) in enumerate(zip(ks, holm(ps))):
            hits[i] += pa < 0.05 and k < k0
    return [round(h / sims, 2) for h in hits]


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [50]:
        print(f"n = {n} per cell (H1 instr, H2 pending)")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
