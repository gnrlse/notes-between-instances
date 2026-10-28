"""Experiment 018 runs 002's task from 002's template with 007's search-first workflow. World W
keeps the template's failing test (INV-2291); world R replaces it with 017's INV-2304, which only
VAT per line fixes. Every cell adds a fourth item to the rules doc: 014's open item with 016's
instruction (instr), or with the self-checkable exit (exit)."""
import shutil
from pathlib import Path

from conditions import DOCS, OLD_TEST, RULE3, SCOPES, WORKFLOWS

TEMPLATE = Path(__file__).resolve().parents[2] / "002-no-competing-source" / "template"


def materialize(dest, notice, workflow, scope, doc):
    assert notice == "plain", notice
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    (dest / "WORKFLOW.md").write_text(WORKFLOWS[workflow])
    test = dest / "tests" / "test_totals.py"
    s = test.read_text()
    assert s.count(OLD_TEST) == 1
    test.write_text(s.replace(OLD_TEST, SCOPES[scope]))
    rules = dest / "docs" / "accounting-rules.md"
    s = rules.read_text()
    assert s.endswith(RULE3)
    rules.write_text(s + DOCS[doc])
