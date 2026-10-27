"""Experiment 008 runs experiment 002's task with 007's plain search tool. Each trial's
WORKFLOW.md sets the order of work, and docs/ledgerline-examples.md holds Ledgerline's
figures, following the trial's truth condition."""
import shutil
from pathlib import Path

from conditions import POINTER, WORKFLOWS, examples

TEMPLATE = Path(__file__).resolve().parents[2] / "002-no-competing-source" / "template"


def materialize(dest, workflow, truth):
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    (dest / "WORKFLOW.md").write_text(WORKFLOWS[workflow])
    rules = dest / "docs" / "accounting-rules.md"
    rules.write_text(rules.read_text() + POINTER)
    (dest / "docs" / "ledgerline-examples.md").write_text(examples(truth))
