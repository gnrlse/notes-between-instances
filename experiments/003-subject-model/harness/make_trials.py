"""Create randomized trial directories from 002's template.

  python3 make_trials.py WAVE MODELS none=8 self=16 ...

MODELS is a comma-separated list of subject models (sonnet,haiku); each count
applies to each model. Writes harness/assignments/WAVE.json (trial id ->
condition and model) and prints only trial ids, models and paths, in a random
launch order, so the person launching agents stays blind to the condition.
"""
import json
import os
import secrets
import sys
import time
from pathlib import Path

from conditions import CONDITIONS, SUBJECTS, mirror
from variants import materialize

HERE = Path(__file__).resolve().parent
VARIANT = "C"
TRIALS = Path(os.environ.get("TRIALS_ROOT", "/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/trials003"))
OLD = time.time() - 3 * 86400  # files older than relatime's window, so the first read updates atime


def main(wave, models, counts):
    out = HERE / "assignments" / f"{wave}.json"
    launch = HERE / "assignments" / f"{wave}.launch.json"
    if out.exists():
        sys.exit(f"{out} exists; pick a new wave name")
    plan = [(m, c) for m in models for c, n in counts.items() for _ in range(n)]
    rng = secrets.SystemRandom()
    rng.shuffle(plan)
    assignment, order = {}, []
    for model, condition in plan:
        tid = f"{wave}-{secrets.token_hex(3)}"
        while tid in assignment:
            tid = f"{wave}-{secrets.token_hex(3)}"
        dest = TRIALS / tid / "invoicing"
        materialize(dest, VARIANT)
        (dest / ".findings" / "mirror.json").write_text(json.dumps(mirror(condition, model), indent=1))
        for dirpath, _, files in os.walk(dest):
            for name in files:
                os.utime(Path(dirpath) / name, (OLD, OLD))
        assignment[tid] = {"condition": condition, "model": model, "variant": VARIANT, "path": str(dest), "created": time.time()}
        order.append({"trial": tid, "model": model, "path": str(dest)})
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(assignment, indent=1))
    launch.write_text(json.dumps(order, indent=1))
    for o in order:
        print(o["trial"], o["model"], o["path"])


if __name__ == "__main__":
    models = sys.argv[2].split(",")
    assert all(m in SUBJECTS for m in models), models
    counts = {}
    for arg in sys.argv[3:]:
        k, v = arg.split("=")
        assert k in CONDITIONS, k
        counts[k] = int(v)
    main(sys.argv[1], models, counts)
