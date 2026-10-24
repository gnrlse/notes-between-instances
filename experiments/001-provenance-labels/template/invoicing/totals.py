"""Invoice totals. These must match Ledgerline; see docs/accounting-rules.md."""
from collections import namedtuple
from decimal import Decimal

CENT = Decimal("0.01")

Totals = namedtuple("Totals", "subtotal vat total")


def line_net(qty, unit_price):
    return (Decimal(str(qty)) * Decimal(str(unit_price))).quantize(CENT)


def invoice_totals(lines, vat_rate):
    """Return Totals(subtotal, vat, total) for an invoice.

    lines: iterable of (quantity, unit_price) pairs, e.g. [(2, "9.99")].
    vat_rate: rate as a string or Decimal, e.g. "0.10".
    """
    rate = Decimal(str(vat_rate))
    subtotal = Decimal("0")
    vat = Decimal("0")
    for qty, unit_price in lines:
        net = line_net(qty, unit_price)
        subtotal += net
        vat += (net * rate).quantize(CENT)
    return Totals(subtotal, vat, subtotal + vat)
