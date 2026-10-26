"""Power of experiment 007's two confirmatory tests under plausible true rates.

  python3 power.py

Simulates the two tests (two-sided Fisher exact on cells pooled over the other factor,
Holm across the two) and reports how often each is supported: Holm-adjusted p < 0.05
with the difference in the stated direction. In 006, agents that chose to read the code
or docs before their first search adopted the note 22/178 times, against 39/107 for
those that searched first. The neutral notice gave 27/71 against the plain notice's 15/71.
"""
import random

from analyze import fisher, holm

SCENARIOS = {
    "order: full 006 gap; neutral: full 006 rise": dict(search_plain=.30, search_neutral=.47, inspect_plain=.10, inspect_neutral=.20),
    "order: half the gap; neutral: half the rise": dict(search_plain=.27, search_neutral=.35, inspect_plain=.15, inspect_neutral=.21),
    "order: half the gap; neutral: no effect": dict(search_plain=.27, search_neutral=.27, inspect_plain=.15, inspect_neutral=.15),
    "order: no effect; neutral: half the rise": dict(search_plain=.24, search_neutral=.32, inspect_plain=.24, inspect_neutral=.32),
    "nothing": dict(search_plain=.24, search_neutral=.24, inspect_plain=.24, inspect_neutral=.24),
}


def simulate(rates, n=72, sims=4000, seed=7):
    rng = random.Random(seed)
    hits = {"H1": 0, "H2": 0}
    for _ in range(sims):
        k = {c: sum(rng.random() < p for _ in range(n)) for c, p in rates.items()}
        s, i = k["search_plain"] + k["search_neutral"], k["inspect_plain"] + k["inspect_neutral"]
        ne, pl = k["search_neutral"] + k["inspect_neutral"], k["search_plain"] + k["inspect_plain"]
        m = 2 * n
        adj = holm([fisher(s, m - s, i, m - i), fisher(ne, m - ne, pl, m - pl)])
        hits["H1"] += adj[0] < 0.05 and s > i
        hits["H2"] += adj[1] < 0.05 and ne > pl
    return {t: round(v / sims, 2) for t, v in hits.items()}


if __name__ == "__main__":
    for name, rates in SCENARIOS.items():
        print(f"{name}: {simulate(rates)}")
