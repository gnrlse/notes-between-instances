"""Power of experiment 013's confirmatory tests under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates both tests (two-sided Fisher exact, gap against closed and absent against closed,
Holm across the two) and reports how often each is supported: adjusted p < 0.05 with
adoption higher than under the closed doc. 011's closed-doc, plain-note cell adopted 1/30,
010's search-first pilot cell 0/10, and 012's two arms 0/96.
"""
import random
import sys

from analyze import fisher, holm

SCENARIOS = {
    "nothing moves (5%, 5%, 5%)": (.05, .05, .05),
    "only absent moves (5%, 5%, 30%)": (.05, .05, .30),
    "both +15 points (5%, 20%, 20%)": (.05, .20, .20),
    "both +20 points (5%, 25%, 25%)": (.05, .25, .25),
    "both +25 points (5%, 30%, 30%)": (.05, .30, .30),
    "gap +10, absent +30 (5%, 15%, 35%)": (.05, .15, .35),
}


def simulate(rates, n, sims=4000, seed=13):
    rng = random.Random(seed)
    closed, gap, absent = rates
    hits = [0, 0]
    for _ in range(sims):
        k0 = sum(rng.random() < closed for _ in range(n))
        ks = [sum(rng.random() < r for _ in range(n)) for r in (gap, absent)]
        ps = [fisher(k, n - k, k0, n - k0) for k in ks]
        for i, (k, pa) in enumerate(zip(ks, holm(ps))):
            hits[i] += pa < 0.05 and k > k0
    return [round(h / sims, 2) for h in hits]


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [40]:
        print(f"n = {n} per cell (H1 gap, H2 absent)")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
