"""Wave status for the launcher, from files only.

  python3 status.py WAVE

Prints counts only: launched, finished (snapshotted) and running.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main(wave):
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    snaps_path = HERE.parent / "results" / f"{wave}.snapshots.json"
    snaps = json.loads(snaps_path.read_text()) if snaps_path.exists() else {}
    total = len(json.loads((HERE / "assignments" / f"{wave}.launch.json").read_text()))
    print(f"launched {len(agents)}/{total}; finished {len(snaps)}; running {len(agents) - len(snaps)}")


if __name__ == "__main__":
    main(sys.argv[1])
