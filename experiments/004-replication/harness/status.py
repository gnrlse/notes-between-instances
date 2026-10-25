"""Wave status for the launcher, from files only: what is running, what still needs the question.

  python3 status.py WAVE

A trial needs the question when it has been snapshotted but its transcript holds no
follow-up question yet. Prints agent ids (to send the question to) and counts only.
"""
import json
import sys
from pathlib import Path

from transcripts import TASKS, is_probe

HERE = Path(__file__).resolve().parent


def asked(aid):
    p = TASKS / f"{aid}.output"
    if not p.exists():
        return False
    for line in p.read_text().splitlines():
        try:
            if is_probe(json.loads(line)):
                return True
        except json.JSONDecodeError:
            continue
    return False


def main(wave):
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    snaps_path = HERE.parent / "results" / f"{wave}.snapshots.json"
    snaps = json.loads(snaps_path.read_text()) if snaps_path.exists() else {}
    total = len(json.loads((HERE / "assignments" / f"{wave}.launch.json").read_text()))
    need = [agents[t] for t in sorted(snaps) if not asked(agents[t])]
    print(f"launched {len(agents)}/{total}; finished {len(snaps)}; running {len(agents) - len(snaps)}; "
          f"asked {len(snaps) - len(need)}")
    print("need the question:", need)


if __name__ == "__main__":
    main(sys.argv[1])
