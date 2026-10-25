"""Experiment 004 runs experiment 002's task unchanged: its template, copied as is."""
import shutil
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parents[2] / "002-no-competing-source" / "template"


def materialize(dest, variant):
    if variant != "C":
        raise ValueError(variant)
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
