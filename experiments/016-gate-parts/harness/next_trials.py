"""Print the next N trials to launch, in the wave's random launch order: id and model only.

  python3 next_trials.py WAVE N

A trial counts as launched once addmap.py has recorded its agent.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main(wave, n):
    order = json.loads((HERE / "assignments" / f"{wave}.launch.json").read_text())
    mapped = HERE / "agents" / f"{wave}.json"
    launched = json.loads(mapped.read_text()) if mapped.exists() else {}
    pending = [o for o in order if o["trial"] not in launched]
    for o in pending[:n]:
        print(o["trial"], o["model"])
    print(f"# {len(launched)} launched, {len(pending)} pending")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
