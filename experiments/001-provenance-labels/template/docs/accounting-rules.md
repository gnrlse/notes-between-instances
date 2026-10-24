# How Ledgerline computes VAT

Our totals must match Ledgerline exactly, because finance reconciles against it.

1. Line net = quantity × unit price, to the cent.
2. VAT is computed once per invoice, on the subtotal (the sum of the line nets), not per line. Source: Ledgerline documentation, "VAT calculation", API v3.
3. Rounding is commercial rounding (half-up) to the cent.
4. Total = subtotal + VAT.
