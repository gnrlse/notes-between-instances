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
    stopped_path = HERE / "agents" / f"{wave}.stopped.json"
    stopped_doc = json.loads(stopped_path.read_text()) if stopped_path.exists() else {}
    # Stopped trials that were rebuilt and relaunched count as launched again.
    stopped = [] if stopped_doc.get("rerun") else stopped_doc.get("trials", [])
    print(f"launched {len(agents)}/{total}; finished {len(snaps)}; stopped {len(stopped)}; "
          f"running {len(agents) - len(snaps) - len(stopped)}")


if __name__ == "__main__":
    main(sys.argv[1])
