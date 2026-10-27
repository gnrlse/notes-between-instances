"""Power of experiment 012's confirmatory test under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates the test (two-sided Fisher exact, review against skip) and reports how often it
is supported: p < 0.05 with adoption higher under review. 011's closed-doc, plain-note cell
adopted 1/30, and 010's search-first pilot cell 0/10.
"""
import random
import sys

from analyze import fisher

SCENARIOS = {
    "nothing moves (5%, 5%)": (.05, .05),
    "review +10 points (5%, 15%)": (.05, .15),
    "review +15 points (5%, 20%)": (.05, .20),
    "review +20 points (5%, 25%)": (.05, .25),
    "review +25 points (5%, 30%)": (.05, .30),
}


def simulate(rates, n, sims=4000, seed=12):
    rng = random.Random(seed)
    skip, review = rates
    hits = 0
    for _ in range(sims):
        a = sum(rng.random() < skip for _ in range(n))
        b = sum(rng.random() < review for _ in range(n))
        hits += fisher(b, n - b, a, n - a) < 0.05 and b > a
    return round(hits / sims, 2)


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [50]:
        print(f"n = {n} per cell")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
