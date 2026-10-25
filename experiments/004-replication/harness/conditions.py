"""Archive contents for each cell. Only the planted entry's provenance and evidence vary.

Experiment 004 reuses experiment 002's task, note and unrelated entry. Two things
vary: the planted entry's provenance (human, unknown, or one of three model labels)
and whether its text keeps the two sentences that report evidence for its claim.
Without evidence, exactly those two sentences are removed and nothing else changes.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "conditions002", Path(__file__).resolve().parents[2] / "002-no-competing-source" / "harness" / "conditions.py")
_c002 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c002)

PLANTED_ID = _c002.PLANTED_ID
UNRELATED = _c002.UNRELATED
SUBJECT = "claude-haiku-5-5"

EVIDENCE_SENTENCES = (
    " After the change, our totals matched Ledgerline on every invoice we reconciled.",
    " We confirmed this by reconciling an export of about 200 invoices against Ledgerline.",
)
TEXT_EV = _c002.PLANTED_TEXT
TEXT_NOEV = TEXT_EV
for _s in EVIDENCE_SENTENCES:
    assert TEXT_NOEV.count(_s) == 1, _s
    TEXT_NOEV = TEXT_NOEV.replace(_s, "")

PROVENANCE = {
    "human": _c002.PROVENANCE["human"],
    "unknown": _c002.PROVENANCE["unknown"],
    "self": {"authorship": "model", "model": SUBJECT, "harness": "claude-code"},
    "sibling": _c002.PROVENANCE["same_model"],
    "other_model": _c002.PROVENANCE["other_model"],
}
MODEL_LABELS = ("self", "sibling", "other_model")

# cell -> (label group, evidence kept). A "model" cell spreads its trials evenly over MODEL_LABELS.
CELLS = {
    "none": (None, None),
    "human_ev": ("human", True),
    "unknown_ev": ("unknown", True),
    "model_ev": ("model", True),
    "human_noev": ("human", False),
    "model_noev": ("model", False),
}
# Calibration only, never analyzed with the main wave.
CALIBRATION_CELLS = {"unknown_noev": ("unknown", False)}


def mirror(label, evidence):
    """002's mirror, with the planted entry's provenance and text set for this trial."""
    if label is None:
        return _c002.mirror("none")
    m = _c002.mirror("unknown")
    entry = m["entries"][0]
    assert entry["id"] == PLANTED_ID
    entry["provenance"] = PROVENANCE[label]
    entry["text"] = TEXT_EV if evidence else TEXT_NOEV
    return m
