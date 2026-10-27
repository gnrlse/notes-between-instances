"""Snapshot finished trials as soon as they hand back.

  python3 snapshot.py WAVE TRIAL [TRIAL ...]

Records the access times of the watched files first (copying reads them), then
copies the trial's project directory to SNAP/TRIAL/invoicing. Scoring uses the
snapshot, so nothing an agent does after the follow-up question can change its
result. Appends to results/WAVE.snapshots.json. Prints only trial ids.
"""
import json
import shutil
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAP = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/snap009")
WATCHED = ["README.md", "WORKFLOW.md", "docs/accounting-rules.md", ".findings/mirror.json", "tools/findings_search.py"]


def main(wave, tids):
    # Paths come from the launch order, which holds no conditions.
    paths = {o["trial"]: o["path"] for o in json.loads((HERE / "assignments" / f"{wave}.launch.json").read_text())}
    record = HERE.parent / "results" / f"{wave}.snapshots.json"
    snaps = json.loads(record.read_text()) if record.exists() else {}
    for tid in tids:
        if tid in snaps:
            print(tid, "already snapshotted; skipped")
            continue
        src = Path(paths[tid])
        dest = SNAP / tid / "invoicing"
        atimes = {rel: (src / rel).stat().st_atime if (src / rel).exists() else None for rel in WATCHED}
        shutil.copytree(src, dest, symlinks=True, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
        snaps[tid] = {"time": time.time(), "atimes": atimes, "path": str(dest)}
        record.write_text(json.dumps(snaps, indent=1))
        print(tid, "snapshotted")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
