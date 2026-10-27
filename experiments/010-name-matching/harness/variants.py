"""Experiment 010 runs a second task, customer name matching against Contactly. Its search
tool prints 006's plain notice, and its WORKFLOW.md sets the order of work."""
import shutil
from pathlib import Path

from conditions import WORKFLOWS

TEMPLATE = Path(__file__).resolve().parents[1] / "template"


def materialize(dest, notice, workflow):
    assert notice == "plain", notice
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    (dest / "WORKFLOW.md").write_text(WORKFLOWS[workflow])
