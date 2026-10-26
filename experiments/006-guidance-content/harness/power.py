"""Power of experiment 006's confirmatory tests under plausible true rates.

  python3 power.py

Simulates the three confirmatory tests (two-sided Fisher exact, Holm across the three)
and reports how often each is supported: Holm-adjusted p < 0.05 with the difference in
the stated direction (the first cell higher). 005 measured plain 20/60 and guided 6/60
under the human label.
"""
import random
from math import comb

SCENARIOS = {
    "content matters, provenance line half": dict(plain=.33, guided=.10, neutral=.33, provenance=.20),
    "content matters, provenance line all": dict(plain=.33, guided=.10, neutral=.33, provenance=.10),
    "content matters, provenance line nothing": dict(plain=.33, guided=.10, neutral=.33, provenance=.33),
    "half content, half length": dict(plain=.33, guided=.10, neutral=.22, provenance=.25),
    "length is enough": dict(plain=.33, guided=.10, neutral=.10, provenance=.30),
    "nothing replicates": dict(plain=.20, guided=.15, neutral=.20, provenance=.20),
}
TESTS = (("H1", "plain", "guided"), ("H2", "neutral", "guided"), ("H3", "plain", "provenance"))


def fisher(a, b, c, d):
    """Two-sided Fisher exact p for [[a, b], [c, d]] (rows: groups; columns: adopted, not)."""
    n1, n2, k = a + b, c + d, a + c
    n = n1 + n2

    def pmf(x):
        return comb(n1, x) * comb(n2, k - x) / comb(n, k)

    p0 = pmf(a)
    lo, hi = max(0, k - n2), min(k, n1)
    return min(1.0, sum(pmf(x) for x in range(lo, hi + 1) if pmf(x) <= p0 * (1 + 1e-9)))


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj, running = [0.0] * len(ps), 0.0
    for rank, i in enumerate(order):
        running = max(running, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = running
    return adj


def simulate(rates, n=60, sims=4000, seed=6):
    rng = random.Random(seed)
    hits = {t: 0 for t, _, _ in TESTS}
    for _ in range(sims):
        k = {c: sum(rng.random() < rates[c] for _ in range(n)) for c in rates}
        ps = [fisher(k[g1], n - k[g1], k[g2], n - k[g2]) for _, g1, g2 in TESTS]
        signs = [k[g1] > k[g2] for _, g1, g2 in TESTS]
        for (t, _, _), p, s in zip(TESTS, holm(ps), signs):
            hits[t] += p < 0.05 and s
    return {t: round(v / sims, 2) for t, v in hits.items()}


if __name__ == "__main__":
    for name, rates in SCENARIOS.items():
        print(f"{name}: {simulate(rates)}")
