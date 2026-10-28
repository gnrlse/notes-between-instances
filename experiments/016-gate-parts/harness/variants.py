"""Experiment 016 runs 002's task from 002's template with 007's search-first workflow and 007's
two-line failing invoice. Every cell adds a fourth item to the rules doc: 014's open item (gap),
or the same item with an instruction that names nothing (instr) or an owner and no instruction
(pending)."""
import shutil
from pathlib import Path

from conditions import DOCS, RULE3, SCOPES, TWO_LINE_CALL, WORKFLOWS

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
    s = rules.read_text()
    assert s.endswith(RULE3)
    rules.write_text(s + DOCS[doc])
