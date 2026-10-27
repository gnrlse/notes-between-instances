"""Rebuild interrupted trials from the template and their unchanged assignment.

  python3 reset_trial.py WAVE TRIAL [TRIAL ...]

Deletes each trial directory, re-creates it exactly as make_trials.py did (same
label, notice, workflow, note, doc and cost, read from the assignment without printing them), and records
the rebuild time. Prints only trial ids.
"""
import json
import shutil
import sys
import time
from pathlib import Path

from make_trials import build

HERE = Path(__file__).resolve().parent


def main(wave, tids):
    path = HERE / "assignments" / f"{wave}.json"
    assignment = json.loads(path.read_text())
    for tid in tids:
        a = assignment[tid]
        dest = Path(a["path"])
        assert dest.parent.name == tid, dest
        shutil.rmtree(dest.parent)
        build(dest, a["label"], a["notice"], a["workflow"], a["note"], a["doc"], a["cost"])
        a["rebuilt"] = a["created"] = time.time()
        print(tid, "rebuilt")
    path.write_text(json.dumps(assignment, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
