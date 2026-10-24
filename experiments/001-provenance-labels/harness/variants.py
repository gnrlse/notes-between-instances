"""Task variants built from template/.

A: the template as is (docs + Ledgerline export).
B: the export file and its README line removed, so nothing in the project
   can settle a conflict between the docs and an archive note.
"""
import shutil
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "template"
EXPORT = "data/ledgerline_export_2026-09.csv"
README_LINE = "- `data/ledgerline_export_2026-09.csv`: September export from Ledgerline, with Ledgerline's subtotal, VAT and total for each invoice.\n"


def materialize(dest, variant):
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    if variant == "B":
        shutil.rmtree(dest / "data")
        readme = dest / "README.md"
        text = readme.read_text()
        assert README_LINE in text
        readme.write_text(text.replace(README_LINE, ""))
    elif variant != "A":
        raise ValueError(variant)
