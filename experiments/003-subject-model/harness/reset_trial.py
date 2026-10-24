"""Rebuild interrupted trials from the template and their unchanged assignment.

  python3 reset_trial.py WAVE TRIAL [TRIAL ...]

Deletes each trial directory, re-creates it exactly as make_trials.py did (same
condition and model, read from the assignment without printing them), and
records the rebuild time. Prints only trial ids and models.
"""
import json
import os
import shutil
import sys
import time
from pathlib import Path

from conditions import mirror
from make_trials import OLD, VARIANT
from variants import materialize

HERE = Path(__file__).resolve().parent


def main(wave, tids):
    path = HERE / "assignments" / f"{wave}.json"
    assignment = json.loads(path.read_text())
    for tid in tids:
        a = assignment[tid]
        dest = Path(a["path"])
        assert dest.parent.name == tid, dest
        shutil.rmtree(dest.parent)
        materialize(dest, VARIANT)
        (dest / ".findings" / "mirror.json").write_text(json.dumps(mirror(a["condition"], a["model"]), indent=1))
        for dirpath, _, files in os.walk(dest):
            for name in files:
                os.utime(Path(dirpath) / name, (OLD, OLD))
        a["rebuilt"] = a["created"] = time.time()
        print(tid, a["model"])
    path.write_text(json.dumps(assignment, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
