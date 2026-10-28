"""Experiment 014 runs 002's task from 002's template with 007's search-first workflow. The scope
variant changes the failing test's invoice to one line (one_line); the doc variant adds a fourth
item to the rules doc (gap)."""
import shutil
from pathlib import Path

from conditions import GAP_ITEM, RULE3, SCOPES, TWO_LINE_CALL, WORKFLOWS

TEMPLATE = Path(__file__).resolve().parents[2] / "002-no-competing-source" / "template"


def materialize(dest, notice, workflow, scope, doc):
    assert notice == "plain", notice
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    (dest / "WORKFLOW.md").write_text(WORKFLOWS[workflow])
    test = dest / "tests" / "test_totals.py"
    s = test.read_text()
    assert s.count(TWO_LINE_CALL) == 1
    test.write_text(s.replace(TWO_LINE_CALL, SCOPES[scope]))
    rules = dest / "docs" / "accounting-rules.md"
    if doc == "gap":
        s = rules.read_text()
        assert s.endswith(RULE3)
        rules.write_text(s + GAP_ITEM)
    else:
        assert doc == "original", doc
