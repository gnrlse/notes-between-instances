"""Simulated power of the four confirmatory tests, for the pre-registration.

  python3 power.py

Two-sided Fisher exact tests, Holm-adjusted across the four; a test counts as
supported when its adjusted p < 0.05 and the difference goes in the stated direction.
"""
import random
from functools import lru_cache
from math import comb

TESTS = (("H1 human>model, evidence", "human_ev", "model_ev"),
         ("H2 human>unknown, evidence", "human_ev", "unknown_ev"),
         ("H3 evidence>none, human", "human_ev", "human_noev"),
         ("H4 human>model, no evidence", "human_noev", "model_noev"))

# True adoption rates under each account of 003's human-label effect.
SCENARIOS = {
    "evidence credibility: the effect needs the evidence": dict(human_ev=.35, unknown_ev=.10, model_ev=.01, human_noev=.05, model_noev=.01),
    "direct: the label works without the evidence": dict(human_ev=.35, unknown_ev=.10, model_ev=.01, human_noev=.30, model_noev=.01),
    "both: evidence helps, the label still matters": dict(human_ev=.35, unknown_ev=.10, model_ev=.01, human_noev=.15, model_noev=.005),
    "weaker effect than 003 (regression to the mean)": dict(human_ev=.20, unknown_ev=.07, model_ev=.01, human_noev=.05, model_noev=.01),
    "no effect": dict(human_ev=.03, unknown_ev=.03, model_ev=.03, human_noev=.03, model_noev=.03),
}


@lru_cache(maxsize=None)
def fisher(a, n1, b, n2):
    k, n = a + b, n1 + n2

    def pr(x):
        return comb(n1, x) * comb(n2, k - x) / comb(n, k)

    p0 = pr(a)
    return min(1.0, sum(pr(x) for x in range(max(0, k - n2), min(k, n1) + 1) if pr(x) <= p0 * (1 + 1e-7)))


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj, run = [0.0] * len(ps), 0.0
    for r, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - r) * ps[i]))
        adj[i] = run
    return adj


def power(rates, n, reps=4000, seed=2):
    rng = random.Random(seed)
    hits = [0] * len(TESTS)
    for _ in range(reps):
        k = {c: sum(rng.random() < p for _ in range(n)) for c, p in rates.items()}
        adj = holm([fisher(k[a], n, k[b], n) for _, a, b in TESTS])
        for i, (_, a, b) in enumerate(TESTS):
            hits[i] += adj[i] < 0.05 and k[a] > k[b]
    return {t[0]: round(h / reps, 2) for t, h in zip(TESTS, hits)}


if __name__ == "__main__":
    for name, rates in SCENARIOS.items():
        print(name, rates)
        print("   ", power(rates, 48))
