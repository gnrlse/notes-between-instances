"""Power of experiment 018's confirmatory tests under plausible true rates.

  python3 power.py [N_PER_CELL ...]

Simulates both tests (two-sided Fisher exact, R_exit against R_instr and W_exit against W_instr,
Holm across the two) and reports how often each is supported: adjusted p < 0.05, with switching
higher under the exit than under the instruction in that world.
"""
import random
import sys

from analyze import fisher, holm

# (W_instr, W_exit, R_instr, R_exit): the share that switch to VAT per line.
SCENARIOS = {
    "nothing moves (0, 0, 0, 0)": (0, 0, 0, 0),
    "exit lets R through a little (0, 2%, 0, 15%)": (0, .02, 0, .15),
    "exit lets R through (0, 2%, 0, 30%)": (0, .02, 0, .30),
    "exit lets R through (0, 2%, 0, 60%)": (0, .02, 0, .60),
    "exit lets R through (0, 2%, 0, 90%)": (0, .02, 0, .90),
    "exit leaks in W a little (0, 10%, 0, 60%)": (0, .10, 0, .60),
    "exit leaks in W (0, 20%, 0, 60%)": (0, .20, 0, .60),
    "exit opens both (0, 40%, 0, 90%)": (0, .40, 0, .90),
}


def simulate(rates, n, sims=4000, seed=18):
    rng = random.Random(seed)
    wi, we, ri, re_ = rates
    hits = [0, 0]
    for _ in range(sims):
        k_wi, k_we, k_ri, k_re = (sum(rng.random() < r for _ in range(n)) for r in (wi, we, ri, re_))
        ps = [fisher(k_re, n - k_re, k_ri, n - k_ri), fisher(k_we, n - k_we, k_wi, n - k_wi)]
        a1, a2 = holm(ps)
        hits[0] += a1 < 0.05 and k_re > k_ri
        hits[1] += a2 < 0.05 and k_we > k_wi
    return [round(h / sims, 2) for h in hits]


if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [50]:
        print(f"n = {n} per cell (H1 R_exit above R_instr, H2 W_exit above W_instr)")
        for name, rates in SCENARIOS.items():
            print(f"  {name}: {simulate(rates, n)}")
