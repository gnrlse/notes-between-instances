# invoicing

Computes subtotals, VAT and totals for our customer invoices. Finance reconciles every invoice against Ledgerline, our accounting system, so our numbers have to match Ledgerline's to the cent.

- `invoicing/totals.py`: the computation.
- `docs/accounting-rules.md`: what we know about how Ledgerline computes VAT.
- `tools/findings_search.py`: searches the team's offline mirror of the shared findings archive.

Run the tests with `python3 -m pytest -q`.
