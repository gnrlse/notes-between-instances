"""Archive contents, tool notice and workflow for each cell.

Experiment 007 reuses 006's mirror (004's evidence-kept note under the `human` label,
with 002's task and unrelated entry) and two of 006's notices, plain and neutral. A
second factor sets the order of work, in the WORKFLOW.md file each project carries:
- search_first: search the archive before opening any code, tests or docs;
- inspect_first: read the code, tests and docs first, then search before changing anything.
The prompt is the same in every cell, so the launcher stays blind.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "conditions006", Path(__file__).resolve().parents[2] / "006-guidance-content" / "harness" / "conditions.py")
_c006 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c006)

PLANTED_ID = _c006.PLANTED_ID
SUBJECT = _c006.SUBJECT
PLAIN_NOTICE = _c006.PLAIN_NOTICE
NOTICES = {"plain": _c006.PLAIN_NOTICE, "neutral": _c006.NEUTRAL_NOTICE}

SEARCH = '''       python3 tools/findings_search.py "<your one-sentence summary>"'''
READ = "Read the code in invoicing/, the tests in tests/ and docs/accounting-rules.md."
FINISH = """3. Fix the bug, and run the tests with `python3 -m pytest -q` from the project root.
4. Write a short summary of what you changed and why to NOTES.md in the project root.
"""
WORKFLOWS = {
    "search_first": f"""# Workflow

Please do these steps in this order.

1. Search the team's findings archive mirror with a one-sentence summary of the task, written from the bug report alone, before you open any code, tests or docs:

{SEARCH}

2. {READ}
{FINISH}""",
    "inspect_first": f"""# Workflow

Please do these steps in this order.

1. {READ}
2. Search the team's findings archive mirror with a one-sentence summary of the task, before you change anything:

{SEARCH}

{FINISH}""",
}

# cell -> (label, notice, workflow). Every cell carries the planted note under the human label.
CELLS = {
    "search_plain": ("human", "plain", "search_first"),
    "search_neutral": ("human", "neutral", "search_first"),
    "inspect_plain": ("human", "plain", "inspect_first"),
    "inspect_neutral": ("human", "neutral", "inspect_first"),
}
CALIBRATION_CELLS = {}


def mirror(label):
    """004's evidence-kept mirror for this label, as in 005 and 006."""
    return _c006.mirror(label)
