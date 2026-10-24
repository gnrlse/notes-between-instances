"""Contamination tripwires: files that would reveal the experiment if an agent read them.

  python3 sentinels.py arm     # set their atime 3 days back (mtime untouched)
  python3 sentinels.py check   # report any that were read since arming
"""
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRATCH = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/scratchpad")
# Untracked files only: git re-reads tracked files whose ctime changed (arming changes
# ctime), so tracked files trip on any `git status`. Transcripts cover the repo instead.
FILES = [
    SCRATCH / "trust-note.json",
    SCRATCH / "build.py",
    SCRATCH / "build2.py",
    SCRATCH / "build3.py",
    SCRATCH / "letter.json",
    SCRATCH / "exp001-results.json",
    SCRATCH / "requests" / "convention.json",
    SCRATCH / "requests" / "search-embargo-fixtures.json",
    SCRATCH / "archive" / "exp001-trials.tgz",
    SCRATCH / "archive" / "exp001-stray-analysis.tgz",
    SCRATCH / "judge" / "main1-A.json",
    SCRATCH / "build4.py",
    SCRATCH / "exp002-results.json",
    SCRATCH / "archive" / "exp002-trials.tgz",
    SCRATCH / "judge" / "main2-A.json",
    SCRATCH / "judge" / "refined-D.json",
    Path("/home/miki/.claude/projects/-home-miki-c/memory/open-thinking-sessions.md"),
]
STATE = HERE / ".sentinels.json"


def main(cmd):
    if cmd == "arm":
        old = time.time() - 3 * 86400
        for f in FILES:
            st = f.stat()
            os.utime(f, (old, st.st_mtime))
        STATE.write_text(json.dumps({"armed": time.time()}))
        print(f"armed {len(FILES)} sentinels")
    else:
        armed = json.loads(STATE.read_text())["armed"]
        hits = [str(f) for f in FILES if f.stat().st_atime > armed]
        print("sentinels read since arming:", hits or "none")


if __name__ == "__main__":
    main(sys.argv[1])
