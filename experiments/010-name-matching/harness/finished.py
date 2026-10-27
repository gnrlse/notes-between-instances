"""Snapshot the trials of agents that just finished, by agent id.

  python3 finished.py WAVE AGENT [AGENT ...]

Looks up each agent's trial in harness/agents/WAVE.json, snapshots it (snapshot.py),
and prints progress. 010 asks no follow-up question.
"""
import json
import sys
from pathlib import Path

import snapshot

HERE = Path(__file__).resolve().parent


def main(wave, agent_ids):
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    trial_of = {a: t for t, a in agents.items()}
    unknown = [a for a in agent_ids if a not in trial_of]
    if unknown:
        sys.exit(f"not in the {wave} map: {unknown}")
    snapshot.main(wave, [trial_of[a] for a in agent_ids])
    snaps = json.loads((HERE.parent / "results" / f"{wave}.snapshots.json").read_text())
    total = len(json.loads((HERE / "assignments" / f"{wave}.launch.json").read_text()))
    stopped_path = HERE / "agents" / f"{wave}.stopped.json"
    stopped_doc = json.loads(stopped_path.read_text()) if stopped_path.exists() else {}
    # Stopped trials that were rebuilt and relaunched count as launched again.
    stopped = [] if stopped_doc.get("rerun") else stopped_doc.get("trials", [])
    print(f"# {len(snaps)} finished and snapshotted, {len(stopped)} stopped, "
          f"{len(agents) - len(snaps) - len(stopped)} running, {total - len(agents)} not launched")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
