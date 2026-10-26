"""Experiment 006 runs experiment 002's task. Each trial's search tool prints one of four notices."""
import shutil
from pathlib import Path

from conditions import NOTICES, PLAIN_NOTICE

TEMPLATE = Path(__file__).resolve().parents[2] / "002-no-competing-source" / "template"
PLAIN_LINE = f'NOTICE = "{PLAIN_NOTICE}"'


def materialize(dest, notice):
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    if notice != "plain":
        tool = dest / "tools" / "findings_search.py"
        src = tool.read_text()
        assert src.count(PLAIN_LINE) == 1
        tool.write_text(src.replace(PLAIN_LINE, f'NOTICE = """{NOTICES[notice]}"""'))
