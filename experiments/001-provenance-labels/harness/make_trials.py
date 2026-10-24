"""Create randomized trial directories from the template.

  python3 make_trials.py WAVE none=1 same_model=1 ...

Writes harness/assignments/WAVE.json (trial id -> condition) and prints only the
trial paths, so the person launching agents stays blind to the assignment.
"""
import json
import os
import secrets
import shutil
import sys
import time
from pathlib import Path

from conditions import CONDITIONS, mirror

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "template"
TRIALS = Path(os.environ.get("TRIALS_ROOT", "/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad/trials"))
OLD = time.time() - 3 * 86400  # files older than relatime's window, so the first read updates atime


def main(wave, counts):
    out = HERE / "assignments" / f"{wave}.json"
    if out.exists():
        sys.exit(f"{out} exists; pick a new wave name")
    plan = [c for c, n in counts.items() for _ in range(n)]
    rng = secrets.SystemRandom()
    rng.shuffle(plan)
    assignment = {}
    for condition in plan:
        tid = f"{wave}-{secrets.token_hex(3)}"
        dest = TRIALS / tid / "invoicing"
        shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
        (dest / ".findings" / "mirror.json").write_text(json.dumps(mirror(condition), indent=1))
        for dirpath, _, files in os.walk(dest):
            for name in files:
                os.utime(Path(dirpath) / name, (OLD, OLD))
        assignment[tid] = {"condition": condition, "path": str(dest), "created": time.time()}
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(assignment, indent=1))
    for tid, a in sorted(assignment.items()):
        print(tid, a["path"])


if __name__ == "__main__":
    counts = {}
    for arg in sys.argv[2:]:
        k, v = arg.split("=")
        assert k in CONDITIONS, k
        counts[k] = int(v)
    main(sys.argv[1], counts)
