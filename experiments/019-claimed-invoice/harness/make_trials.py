"""Create randomized trial directories from 002's template.

  python3 make_trials.py WAVE general_exit=N specific_exit=N specific_instr=N

Every trial runs on Haiku in world W (the template's failing test, INV-2291), searches first, and
has 007's note under the human label with the plain notice. The note's text (018's, or 018's plus
one stated invoice) and the rules doc's fourth item vary. Writes harness/assignments/WAVE.json
(trial id -> cell, label, notice, workflow, scope, doc and note) and a launch list. Prints only
trial ids, worlds and paths, in a random launch order, so the launcher stays blind to the cell.
"""
import json
import os
import secrets
import sys
import time
from pathlib import Path

from conditions import CALIBRATION_CELLS, CELLS, WORLD, mirror
from variants import materialize

HERE = Path(__file__).resolve().parent
TRIALS = Path(os.environ.get("TRIALS_ROOT", "/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/trials019"))
OLD = time.time() - 3 * 86400  # files older than relatime's window, so the first read updates atime


def build(dest, label, notice, workflow, scope, doc, note):
    materialize(dest, notice, workflow, scope, doc)
    (dest / ".findings" / "mirror.json").write_text(json.dumps(mirror(label, note), indent=1))
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
    for cell, label, notice, workflow, scope, doc, note in plan:
        tid = f"{wave}-{secrets.token_hex(3)}"
        while tid in assignment:
            tid = f"{wave}-{secrets.token_hex(3)}"
        dest = TRIALS / tid / "invoicing"
        build(dest, label, notice, workflow, scope, doc, note)
        assignment[tid] = {"cell": cell, "label": label, "notice": notice, "workflow": workflow, "scope": scope, "doc": doc, "note": note,
                           "model": "haiku", "path": str(dest), "created": time.time()}
        order.append({"trial": tid, "model": "haiku", "world": WORLD[scope], "path": str(dest)})
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(assignment, indent=1))
    launch.write_text(json.dumps(order, indent=1))
    for o in order:
        print(o["trial"], o["model"], o["world"], o["path"])


if __name__ == "__main__":
    counts = {}
    for arg in sys.argv[2:]:
        k, v = arg.split("=")
        assert k in CELLS or k in CALIBRATION_CELLS, k
        counts[k] = int(v)
    main(sys.argv[1], counts)
