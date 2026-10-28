"""Power of experiment 020's confirmatory tests under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates both tests (two-sided Fisher exact, project_record against archive_theirs and
archive_ours against archive_theirs, Holm across the two) and reports how often each is
supported: adjusted p < 0.05, with switching higher in the treatment cell.
"""
import random
import sys

from analyze import fisher, holm

# (archive_theirs, archive_ours, project_record): the share that switch to VAT per line.
SCENARIOS = {
    "nothing gets through (0, 0, 0)": (0, 0, 0),
    "only the record gets through (0, 0, 70%)": (0, 0, .70),
    "the record gets through less (0, 0, 30%)": (0, 0, .30),
    "the claimed provenance leaks a little (0, 10%, 70%)": (0, .10, .70),
    "the claimed provenance leaks (0, 20%, 70%)": (0, .20, .70),
    "the claimed provenance works like the record (0, 60%, 70%)": (0, .60, .70),
}


def simulate(rates, n, sims=4000, seed=20):
    rng = random.Random(seed)
    t, o, r = rates
    hits = [0, 0]
    for _ in range(sims):
        kt, ko, kr = (sum(rng.random() < x for _ in range(n)) for x in (t, o, r))
        ps = [fisher(kr, n - kr, kt, n - kt), fisher(ko, n - ko, kt, n - kt)]
        a1, a2 = holm(ps)
        hits[0] += a1 < 0.05 and kr > kt
        hits[1] += a2 < 0.05 and ko > kt
    return [round(h / sims, 2) for h in hits]


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [50]:
        print(f"n = {n} per cell (H1 project_record above archive_theirs, H2 archive_ours above archive_theirs)")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
