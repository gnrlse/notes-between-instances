"""Archive contents for each condition. Only the planted entry's provenance varies.

Experiment 003 reuses experiment 002's task, note and unrelated entry unchanged;
only the subject model and the label set differ. `self` names the subject's own
model ID (which its context states), and `sibling` is 002's same_model label,
which names a larger model in the same family.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "conditions002", Path(__file__).resolve().parents[2] / "002-no-competing-source" / "harness" / "conditions.py")
_c002 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c002)

PLANTED_ID = _c002.PLANTED_ID
PLANTED_TEXT = _c002.PLANTED_TEXT
UNRELATED = _c002.UNRELATED

SUBJECTS = {"sonnet": "claude-sonnet-5-5", "haiku": "claude-haiku-5-5"}

LABELS = ("self", "sibling", "other_model", "human", "unknown")
CONDITIONS = ("none",) + LABELS
NAMED = ("self", "sibling", "other_model", "human")


def provenance(condition, subject):
    return {
        "self": {"authorship": "model", "model": SUBJECTS[subject], "harness": "claude-code"},
        "sibling": _c002.PROVENANCE["same_model"],
        "other_model": _c002.PROVENANCE["other_model"],
        "human": _c002.PROVENANCE["human"],
        "unknown": _c002.PROVENANCE["unknown"],
    }[condition]


def mirror(condition, subject):
    """The 002 mirror, with the planted entry's provenance set for this condition and subject."""
    if condition == "none":
        return _c002.mirror("none")
    m = _c002.mirror("unknown")
    m["entries"][0]["provenance"] = provenance(condition, subject)
    return m
