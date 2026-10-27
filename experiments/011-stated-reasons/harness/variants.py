"""Experiment 011 runs 010's task from 010's template. Its search tool prints 006's plain
notice, its WORKFLOW.md sets the order of work, and in the `open` doc cells the rules doc
gains one closing line."""
import shutil
from pathlib import Path

from conditions import DOCS, WORKFLOWS

TEMPLATE = Path(__file__).resolve().parents[2] / "010-name-matching" / "template"


def materialize(dest, notice, workflow, doc):
    assert notice == "plain", notice
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    (dest / "WORKFLOW.md").write_text(WORKFLOWS[workflow])
    if DOCS[doc]:
        rules = dest / "docs" / "contactly-rules.md"
        rules.write_text(rules.read_text() + "\n" + DOCS[doc])
