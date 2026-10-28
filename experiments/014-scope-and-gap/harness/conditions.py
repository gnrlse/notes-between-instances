"""Archive contents, tool notice, workflow, failing test and rules doc for each cell.

Experiment 014 runs 007's search-first, plain-notice cell on 002's invoice task (45/72 adopted
the wrong per-line VAT note there) and varies two things, one at a time:
- scope: the failing invoice INV-2291 has two lines, as in 007, or one line with the same
  totals (1.37 against Ledgerline's 1.38). The note's claim is about invoices with several
  lines, so a one-line invoice puts the reported case outside it, as the name task's reported
  customer (no umlauts) is outside its umlaut rule.
- doc: 007's rules doc, or the same doc with a fourth item marking the note's question as
  open, worded like 013's gap item.
Three cells: two_line (007's cell), one_line, and gap (two lines plus the open item).
The prompt is the same in every cell, so the launcher stays blind.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "conditions007", Path(__file__).resolve().parents[2] / "007-order-of-work" / "harness" / "conditions.py")
_c007 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c007)

SUBJECT = _c007.SUBJECT
PLANTED_ID = _c007.PLANTED_ID
PLAIN_NOTICE = _c007.PLAIN_NOTICE
NOTICES = {"plain": _c007.PLAIN_NOTICE}
WORKFLOWS = {"search_first": _c007.WORKFLOWS["search_first"]}

# The failing test's call, in 007's two-line form and in the one-line form.
TWO_LINE_CALL = 't = invoice_totals([(1, "0.25"), (1, "1.00")], "0.10")'
ONE_LINE_CALL = 't = invoice_totals([(1, "1.25")], "0.10")'
SCOPES = {"two_line": TWO_LINE_CALL, "one_line": ONE_LINE_CALL}

# The doc's last line, and the item the gap variant adds right after it.
RULE3 = "3. Total = subtotal + VAT.\n"
GAP_ITEM = "4. VAT (on each line, or once on the subtotal): we don't know yet how Ledgerline computes it.\n"
DOCS = {"original": None, "gap": GAP_ITEM}


def mirror(label):
    return _c007.mirror(label)


# cell -> (label, notice, workflow, scope, doc).
CELLS = {
    "two_line": ("human", "plain", "search_first", "two_line", "original"),
    "one_line": ("human", "plain", "search_first", "one_line", "original"),
    "gap": ("human", "plain", "search_first", "two_line", "gap"),
}
CALIBRATION_CELLS = {}
