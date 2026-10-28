"""Power of experiment 017's confirmatory tests under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates both tests (two-sided Fisher exact, instr against gap and until against instr, Holm
across the two) and reports how often each is supported: adjusted p < 0.05, with switching lower
under instr than under gap (H1) and higher under until than under instr (H2).
"""
import random
import sys

from analyze import fisher, holm

# (gap, instr, until): the share that switch to VAT per line.
SCENARIOS = {
    "nothing moves (95%, 95%, 95%)": (.95, .95, .95),
    "instr -15, until like instr (95%, 80%, 80%)": (.95, .80, .80),
    "instr -45, until like instr (95%, 50%, 50%)": (.95, .50, .50),
    "instr -45, until +15 (95%, 50%, 65%)": (.95, .50, .65),
    "instr -45, until +30 (95%, 50%, 80%)": (.95, .50, .80),
    "instr -75, until +30 (95%, 20%, 50%)": (.95, .20, .50),
    "instr holds, until back to gap (95%, 5%, 95%)": (.95, .05, .95),
    "both hold (95%, 5%, 5%)": (.95, .05, .05),
}


def simulate(rates, n, sims=4000, seed=17):
    rng = random.Random(seed)
    gap, instr, until = rates
    hits = [0, 0]
    for _ in range(sims):
        kg, ki, ku = (sum(rng.random() < r for _ in range(n)) for r in (gap, instr, until))
        ps = [fisher(ki, n - ki, kg, n - kg), fisher(ku, n - ku, ki, n - ki)]
        a1, a2 = holm(ps)
        hits[0] += a1 < 0.05 and ki < kg
        hits[1] += a2 < 0.05 and ku > ki
    return [round(h / sims, 2) for h in hits]


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [50]:
        print(f"n = {n} per cell (H1 instr below gap, H2 until above instr)")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
