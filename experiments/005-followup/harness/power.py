"""Power of experiment 005's confirmatory tests under plausible true rates, for two allocations.

  python3 power.py

Simulates the three confirmatory tests (two-sided Fisher exact, Holm across the three)
and reports how often each is supported: Holm-adjusted p < 0.05 with the difference in
the stated direction.
"""
import random
from math import comb

# True adoption rates. The plain cells repeat 004's evidence-kept cells (human 20/48, model 5/48).
SCENARIOS = {
    "guidance does nothing": dict(human_plain=.40, human_guided=.40, model_plain=.08, model_guided=.08),
    "guidance halves the human cell": dict(human_plain=.40, human_guided=.20, model_plain=.08, model_guided=.05),
    "guidance removes the label effect": dict(human_plain=.40, human_guided=.08, model_plain=.08, model_guided=.06),
    "guidance raises adoption": dict(human_plain=.40, human_guided=.55, model_plain=.08, model_guided=.12),
}
ALLOCATIONS = {
    "48 per cell": dict(human_plain=48, human_guided=48, model_plain=48, model_guided=48),
    "60 human, 36 model": dict(human_plain=60, human_guided=60, model_plain=36, model_guided=36),
}
TESTS = (("H1", "human_plain", "human_guided"), ("H2", "human_guided", "model_guided"), ("H3", "human_plain", "model_plain"))


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


def simulate(rates, ns, sims=4000, seed=5):
    rng = random.Random(seed)
    hits = {t: 0 for t, _, _ in TESTS}
    for _ in range(sims):
        k = {c: sum(rng.random() < rates[c] for _ in range(ns[c])) for c in ns}
        ps, signs = [], []
        for t, g1, g2 in TESTS:
            ps.append(fisher(k[g1], ns[g1] - k[g1], k[g2], ns[g2] - k[g2]))
            signs.append(k[g1] / ns[g1] > k[g2] / ns[g2])
        for (t, _, _), p, s in zip(TESTS, holm(ps), signs):
            hits[t] += p < 0.05 and s
    return {t: round(v / sims, 2) for t, v in hits.items()}


if __name__ == "__main__":
    for alloc, ns in ALLOCATIONS.items():
        print(f"## {alloc}")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, ns)}")
