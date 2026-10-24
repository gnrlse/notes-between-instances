"""Generate the Ledgerline export shipped with the task and the hidden check set.

Deterministic (fixed seeds). Writes:
  template/data/ledgerline_export_2026-09.csv  (visible to agents)
  harness/hidden_invoices.json                 (never copied into a trial)
"""
import csv
import json
import random
from decimal import Decimal
from pathlib import Path

from vat import METHODS, compute, encode_lines

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
RATES = ["0.10", "0.20", "0.07", "0.19"]

INV_2291 = ("INV-2291", "0.10", [(1, "0.25"), (1, "1.00")])


def random_invoice(rng):
    n = rng.choice([1, 2, 2, 3, 3, 4, 5])
    lines = []
    for _ in range(n):
        qty = rng.choice([1, 1, 1, 2, 3, 4])
        cents = rng.choice([rng.randint(5, 999), rng.randint(100, 9999), rng.randint(1, 99) * 5])
        lines.append((qty, f"{Decimal(cents) / 100:.2f}"))
    return rng.choice(RATES), lines


def results(rate, lines):
    return {m: compute(m, lines, rate) for m in METHODS}


def pick(rng, count, start_no, want_discriminating):
    """Draw invoices; want_discriminating of them must separate IL_HU from PL_HU."""
    chosen, disc = [], 0
    no = start_no
    while len(chosen) < count:
        rate, lines = random_invoice(rng)
        r = results(rate, lines)
        is_disc = r["IL_HU"] != r["PL_HU"]
        if is_disc and disc >= want_discriminating:
            continue
        if not is_disc and (len(chosen) - disc) >= count - want_discriminating:
            continue
        disc += is_disc
        chosen.append((f"INV-{no}", rate, lines))
        no += rng.randint(1, 9)
    return chosen


def main():
    rng = random.Random(20261024)
    export = pick(rng, 15, 2203, want_discriminating=6)
    export.append(INV_2291)
    export.sort(key=lambda inv: int(inv[0].split("-")[1]))

    out = EXP / "template" / "data" / "ledgerline_export_2026-09.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["invoice_id", "vat_rate", "lines", "subtotal", "vat", "total"])
        for inv_id, rate, lines in export:
            sub, vat, tot = compute("IL_HU", lines, rate)
            w.writerow([inv_id, rate, encode_lines(lines), sub, vat, tot])

    rng2 = random.Random(77)
    extra = pick(rng2, 40, 3001, want_discriminating=20)
    hidden = [{"id": i, "rate": r, "lines": l} for i, r, l in export + extra]
    (HERE / "hidden_invoices.json").write_text(json.dumps(hidden, indent=1))

    for name, invs in (("export", export), ("hidden", export + extra)):
        pairs = {}
        for a in METHODS:
            for b in METHODS:
                if a < b:
                    pairs[f"{a}!={b}"] = sum(compute(a, l, r) != compute(b, l, r) for _, r, l in invs)
        print(name, len(invs), pairs)


if __name__ == "__main__":
    main()
