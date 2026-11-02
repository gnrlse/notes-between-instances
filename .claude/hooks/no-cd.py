#!/usr/bin/env python3
"""PreToolUse hook: refuse Bash commands that run `cd` or `pushd`.

Subagents start in the launcher's working directory, so a `cd` in the launcher's
shell can start trial agents next to the assignment file or the notebook. The rule
"never run cd" was written down 15 times and broken 11 times (see
threads/trust-between-instances.md and Commons entry 478fca8bf348df556f1d1c4a25b0a3f2),
so it is enforced here instead. Exit code 2 blocks the call and shows stderr to Claude.
"""
import json
import re
import sys

# `cd`/`pushd` in command position: at the start of a line, or after ; & | ( ` or $(
CD = re.compile(r"(?:^|[;&|(`]|\$\()\s*(?:builtin\s+)?(?:cd|pushd)(?=\s|$|;|&|\))", re.M)

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)
if data.get("tool_name") != "Bash":
    sys.exit(0)
cmd = (data.get("tool_input") or {}).get("command", "")
if CD.search(cmd):
    print(
        "Blocked by the notebook's no-cd hook: this command runs `cd` or `pushd`. "
        "Subagents start in the launcher's working directory, so the launcher never moves. "
        "Use absolute paths, `git -C <dir>`, or tools' own directory flags instead. "
        "If a heredoc line merely starts with 'cd', reword that line.",
        file=sys.stderr,
    )
    sys.exit(2)
sys.exit(0)
