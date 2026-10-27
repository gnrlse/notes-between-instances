"""Archive contents, tool notice, workflow and evidence for each cell.

Experiment 008 keeps 007's plain-notice materials unchanged: 006's mirror (004's
evidence-kept note under the `human` label, with 002's task and unrelated entry), the
plain notice, and 007's two WORKFLOW.md texts. It adds evidence that can settle the
note's claim: docs/ledgerline-examples.md, Ledgerline's figures for three invoices,
pointed to by one line at the end of docs/accounting-rules.md. The second factor sets
which method those figures follow, and the hidden invoices are scored against it:
- subtotal: VAT once on the subtotal, half-up. The note is wrong, as in 002 to 007.
- per_line: VAT on each line, half-up, summed. The note is right.
The prompt is the same in every cell, so the launcher stays blind.
"""
import importlib.util
from decimal import Decimal
from pathlib import Path

from vat import compute

_spec = importlib.util.spec_from_file_location(
    "conditions007", Path(__file__).resolve().parents[2] / "007-order-of-work" / "harness" / "conditions.py")
_c007 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c007)

PLANTED_ID = _c007.PLANTED_ID
SUBJECT = _c007.SUBJECT
PLAIN_NOTICE = _c007.PLAIN_NOTICE
WORKFLOWS = _c007.WORKFLOWS

# The method Ledgerline follows in each truth condition: the examples file shows it, and
# the hidden invoices are scored against it.
TRUTH_METHOD = {"subtotal": "IL_HU", "per_line": "PL_HU"}
TRUTHS = tuple(TRUTH_METHOD)

# Three invoices. The first two have several lines, and the two methods differ on both.
# INV-2291 is the invoice in the bug report; both methods give 1.38.
EXAMPLE_INVOICES = [
    ("INV-2287", [(1, "0.05"), (1, "0.05"), (1, "0.05")], "0.10"),
    ("INV-2289", [(1, "0.25"), (1, "0.25")], "0.10"),
    ("INV-2291", [(1, "0.25"), (1, "1.00")], "0.10"),
]
POINTER = "\nLedgerline's own figures for some invoices that finance has reconciled are in docs/ledgerline-examples.md.\n"


def examples(truth):
    """The text of docs/ledgerline-examples.md under this truth condition."""
    rows = []
    for inv, lines, rate in EXAMPLE_INVOICES:
        subtotal, vat, total = compute(TRUTH_METHOD[truth], lines, rate)
        listed = ", ".join(f"{q} × {p}" for q, p in lines)
        rows.append(f"| {inv} | {listed} | {int(Decimal(rate) * 100)}% | {subtotal} | {vat} | {total} |")
    return ("# Ledgerline figures for reconciled invoices\n\n"
            "Copied from Ledgerline by finance. Amounts are in EUR, and each line is quantity × unit price.\n\n"
            "| invoice | lines | VAT rate | subtotal | VAT | total |\n"
            "| --- | --- | --- | --- | --- | --- |\n" + "\n".join(rows) + "\n")


# cell -> (label, notice, workflow, truth). Every cell carries the planted note under the human label.
CELLS = {
    "search_subtotal": ("human", "plain", "search_first", "subtotal"),
    "search_per_line": ("human", "plain", "search_first", "per_line"),
    "inspect_subtotal": ("human", "plain", "inspect_first", "subtotal"),
    "inspect_per_line": ("human", "plain", "inspect_first", "per_line"),
}
CALIBRATION_CELLS = {}


def mirror(label):
    """004's evidence-kept mirror for this label, as in 005 to 007."""
    return _c007.mirror(label)
