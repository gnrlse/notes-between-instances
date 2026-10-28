"""Power of experiment 019's confirmatory tests under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates both tests (two-sided Fisher exact, specific_exit against general_exit and specific_exit
against specific_instr, Holm across the two) and reports how often each is supported: adjusted
p < 0.05, with switching higher in specific_exit.
"""
import random
import sys

from analyze import fisher, holm

# (general_exit, specific_exit, specific_instr): the share that switch to VAT per line.
SCENARIOS = {
    "nothing gets through (0, 0, 0)": (0, 0, 0),
    "the stated invoice leaks a little (0, 10%, 0)": (0, .10, 0),
    "the stated invoice leaks (0, 20%, 0)": (0, .20, 0),
    "the stated invoice leaks (0, 30%, 2%)": (0, .30, .02),
    "it leaks past both items alike (0, 20%, 20%)": (0, .20, .20),
    "it leaks widely (0, 50%, 5%)": (0, .50, .05),
}


def simulate(rates, n, sims=4000, seed=19):
    rng = random.Random(seed)
    g, s, i = rates
    hits = [0, 0]
    for _ in range(sims):
        kg, ks, ki = (sum(rng.random() < r for _ in range(n)) for r in (g, s, i))
        ps = [fisher(ks, n - ks, kg, n - kg), fisher(ks, n - ks, ki, n - ki)]
        a1, a2 = holm(ps)
        hits[0] += a1 < 0.05 and ks > kg
        hits[1] += a2 < 0.05 and ks > ki
    return [round(h / sims, 2) for h in hits]


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [50]:
        print(f"n = {n} per cell (H1 specific_exit above general_exit, H2 specific_exit above specific_instr)")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
