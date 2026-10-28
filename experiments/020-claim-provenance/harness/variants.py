"""Experiment 020 runs 002's task from 002's template with 007's search-first workflow, in world W:
the template's failing test (INV-2291) is kept. Every cell adds 018's self-checkable exit as the
rules doc's fourth item. The record variant (exit_record) also adds finance's reconciliation of
the stated invoice after the doc's intro. The archive note's text is set by make_trials.build,
not here."""
import shutil
from pathlib import Path

from conditions import DOCS, INTRO, OLD_TEST, RECORD, RULE3, SCOPES, WORKFLOWS

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
    assert s.endswith(RULE3) and s.count(INTRO) == 1
    if doc == "exit_record":
        s = s.replace(INTRO, INTRO[:-1] + RECORD + "\n")
    rules.write_text(s + DOCS[doc])
