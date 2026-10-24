"""Experiment 002 has a single task variant: the template as is."""
import shutil
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "template"


def materialize(dest, variant):
    if variant != "C":
        raise ValueError(variant)
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
