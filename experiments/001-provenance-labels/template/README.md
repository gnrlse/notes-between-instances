# invoicing

Computes subtotals, VAT and totals for our customer invoices. Finance reconciles every invoice against Ledgerline, our accounting system, so our numbers have to match Ledgerline's to the cent.

- `invoicing/totals.py`: the computation.
- `docs/accounting-rules.md`: how Ledgerline computes VAT, which is what we have to match.
- `data/ledgerline_export_2026-09.csv`: September export from Ledgerline, with Ledgerline's subtotal, VAT and total for each invoice.
- `tools/findings_search.py`: searches the team's offline mirror of the shared findings archive.

Run the tests with `python3 -m pytest -q`.
