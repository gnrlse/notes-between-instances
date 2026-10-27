"""Experiment 012 runs 010's task from 010's template, with 011's materials. The cost
variant adds one sentence after the README's description of the matching, and the same
sentence to find_existing's docstring."""
import shutil
from pathlib import Path

from conditions import COSTS, DOCS, DOCSTRING_AFTER, README_AFTER, WORKFLOWS

TEMPLATE = Path(__file__).resolve().parents[2] / "010-name-matching" / "template"


def materialize(dest, notice, workflow, doc, cost):
    assert notice == "plain", notice
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    (dest / "WORKFLOW.md").write_text(WORKFLOWS[workflow])
    if DOCS[doc]:
        rules = dest / "docs" / "contactly-rules.md"
        rules.write_text(rules.read_text() + "\n" + DOCS[doc])
    readme = dest / "README.md"
    s = readme.read_text()
    assert s.count(README_AFTER) == 1
    readme.write_text(s.replace(README_AFTER, f"{README_AFTER} {COSTS[cost]}"))
    names = dest / "crmsync" / "names.py"
    s = names.read_text()
    assert s.count(DOCSTRING_AFTER) == 1
    names.write_text(s.replace(DOCSTRING_AFTER, f"{DOCSTRING_AFTER}\n    {COSTS[cost]}\n"))
