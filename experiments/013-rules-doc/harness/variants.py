"""Experiment 013 runs 010's task from 010's template, with 011's materials. The doc variant
adds a third item to the rules doc (gap), or removes the doc and every mention of it (absent)."""
import shutil
from pathlib import Path

from conditions import DOCSTRING_REF, GAP_ITEM, README_DOC_LINE, RULE2, WORKFLOWS

TEMPLATE = Path(__file__).resolve().parents[2] / "010-name-matching" / "template"


def materialize(dest, notice, workflow, doc):
    assert notice == "plain", notice
    assert (doc == "absent") == (workflow == "search_first_nodoc"), (doc, workflow)
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    (dest / "WORKFLOW.md").write_text(WORKFLOWS[workflow])
    rules = dest / "docs" / "contactly-rules.md"
    if doc == "gap":
        s = rules.read_text()
        assert s.endswith(RULE2)
        rules.write_text(s + GAP_ITEM)
    elif doc == "absent":
        shutil.rmtree(dest / "docs")
        readme = dest / "README.md"
        s = readme.read_text()
        assert s.count(README_DOC_LINE) == 1
        readme.write_text(s.replace(README_DOC_LINE, ""))
        names = dest / "crmsync" / "names.py"
        s = names.read_text()
        assert s.count(DOCSTRING_REF) == 1
        names.write_text(s.replace(DOCSTRING_REF, ""))
    else:
        assert doc == "closed", doc
