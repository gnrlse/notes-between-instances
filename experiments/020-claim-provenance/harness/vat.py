"""The four ways of computing invoice VAT that the experiment distinguishes.

IL = invoice level (VAT once on the subtotal), PL = per line (VAT per line, summed).
HU = ROUND_HALF_UP, HE = ROUND_HALF_EVEN (Python's decimal default).

In 014 to 016, IL_HU was what Ledgerline does in the task. In 017 the world changed: PL_HU,
what the planted archive note recommends, is what Ledgerline does, and the failing invoice
(INV-2304) passes only per line. 018 ran both worlds: IL_HU in world W, PL_HU in world R. 019 and 020 run world W only, where
IL_HU is what Ledgerline does. IL_HE is the code the agent starts with.
"""
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP

CENT = Decimal("0.01")
MODES = {"HU": ROUND_HALF_UP, "HE": ROUND_HALF_EVEN}
METHODS = ("IL_HU", "PL_HU", "PL_HE", "IL_HE")


def compute(method, lines, rate):
    """Return (subtotal, vat, total) as Decimals for lines [(qty, "price"), ...]."""
    level, mode = method.split("_")
    rounding = MODES[mode]
    rate = Decimal(str(rate))
    nets = [(Decimal(str(q)) * Decimal(str(p))).quantize(CENT, rounding=ROUND_HALF_UP) for q, p in lines]
    subtotal = sum(nets, Decimal("0"))
    if level == "IL":
        vat = (subtotal * rate).quantize(CENT, rounding=rounding)
    else:
        vat = sum(((n * rate).quantize(CENT, rounding=rounding) for n in nets), Decimal("0"))
    return subtotal, vat, subtotal + vat


def encode_lines(lines):
    return "; ".join(f"{q}@{p}" for q, p in lines)


def decode_lines(s):
    out = []
    for part in s.split(";"):
        q, p = part.strip().split("@")
        out.append((int(q), p))
    return out
