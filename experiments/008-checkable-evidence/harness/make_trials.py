"""Create randomized trial directories from 002's template.

  python3 make_trials.py WAVE search_subtotal=72 search_per_line=72 inspect_subtotal=72 inspect_per_line=72

Every trial runs on Haiku, and every trial's mirror holds the planted note under the
human label, with the plain notice. The project's WORKFLOW.md and its
docs/ledgerline-examples.md vary. Writes harness/assignments/WAVE.json (trial id -> cell,
label, notice, workflow and truth) and prints only trial ids and paths, in a random
launch order, so the launcher stays blind.
"""
import json
import os
import secrets
import sys
import time
from pathlib import Path

from conditions import CALIBRATION_CELLS, CELLS, mirror
from variants import materialize

HERE = Path(__file__).resolve().parent
TRIALS = Path(os.environ.get("TRIALS_ROOT", "/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/trials008"))
OLD = time.time() - 3 * 86400  # files older than relatime's window, so the first read updates atime


def build(dest, label, workflow, truth):
    materialize(dest, workflow, truth)
    (dest / ".findings" / "mirror.json").write_text(json.dumps(mirror(label), indent=1))
    for dirpath, _, files in os.walk(dest):
        for name in files:
            os.utime(Path(dirpath) / name, (OLD, OLD))


def main(wave, counts):
    out = HERE / "assignments" / f"{wave}.json"
    launch = HERE / "assignments" / f"{wave}.launch.json"
    if out.exists():
        sys.exit(f"{out} exists; pick a new wave name")
    cells = {**CELLS, **CALIBRATION_CELLS}
    plan = []
    for cell, n in counts.items():
        plan += [(cell, *cells[cell])] * n
    rng = secrets.SystemRandom()
    rng.shuffle(plan)
    assignment, order = {}, []
    for cell, label, notice, workflow, truth in plan:
        tid = f"{wave}-{secrets.token_hex(3)}"
        while tid in assignment:
            tid = f"{wave}-{secrets.token_hex(3)}"
        dest = TRIALS / tid / "invoicing"
        build(dest, label, workflow, truth)
        assignment[tid] = {"cell": cell, "label": label, "notice": notice, "workflow": workflow, "truth": truth,
                           "evidence": True, "model": "haiku", "path": str(dest), "created": time.time()}
        order.append({"trial": tid, "model": "haiku", "path": str(dest)})
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(assignment, indent=1))
    launch.write_text(json.dumps(order, indent=1))
    for o in order:
        print(o["trial"], o["model"], o["path"])


if __name__ == "__main__":
    counts = {}
    for arg in sys.argv[2:]:
        k, v = arg.split("=")
        assert k in CELLS or k in CALIBRATION_CELLS, k
        counts[k] = int(v)
    main(sys.argv[1], counts)
