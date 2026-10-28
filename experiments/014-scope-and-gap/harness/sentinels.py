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
MEMORY = Path("/home/miki/.claude/projects/-home-miki-c/memory")
# Untracked files only: git re-reads tracked files whose ctime changed (arming changes
# ctime), so tracked files trip on any `git status`. Transcripts cover the repo instead.
# Everything under the scratchpad archive (entry drafts, receipts, judge inputs, earlier
# trials), plus the two memory topic files. MEMORY.md is left out: the harness may read it.
FILES = sorted(p for p in (SCRATCH / "archive").rglob("*") if p.is_file()) + [
    MEMORY / "open-thinking-sessions.md",
    MEMORY / "commons-publishing.md",
]
STATE = HERE / ".sentinels.json"


def main(cmd):
    if cmd == "arm":
        old = time.time() - 3 * 86400
        for f in FILES:
            st = f.stat()
            os.utime(f, (old, st.st_mtime))
        STATE.write_text(json.dumps({"armed": time.time(), "files": [str(f) for f in FILES]}))
        print(f"armed {len(FILES)} sentinels")
    else:
        state = json.loads(STATE.read_text())
        armed, files = state["armed"], [Path(f) for f in state["files"]]
        hits = [str(f) for f in files if f.stat().st_atime > armed]
        print(f"{len(files)} sentinels; read since arming:", hits or "none")


if __name__ == "__main__":
    main(sys.argv[1])
