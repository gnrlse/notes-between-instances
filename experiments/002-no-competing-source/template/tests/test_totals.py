from decimal import Decimal

from invoicing.totals import invoice_totals

D = Decimal


def test_single_line():
    t = invoice_totals([(2, "10.00")], "0.20")
    assert t == (D("20.00"), D("4.00"), D("24.00"))


def test_zero_rate():
    t = invoice_totals([(3, "1.99"), (1, "0.50")], "0")
    assert t.total == D("6.47")


def test_inv_2291():
    # Reported by finance: Ledgerline has 1.38 for this invoice, we have 1.37.
    t = invoice_totals([(1, "0.25"), (1, "1.00")], "0.10")
    assert t.total == D("1.38")
