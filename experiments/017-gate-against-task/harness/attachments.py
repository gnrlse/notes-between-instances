"""Where Claude Code's generic context block first reached each agent, without printing it.

  python3 attachments.py WAVE

Shortly after a subagent starts, the harness sends it a system block that lists agent types
and adds a note on tool use. It is the same in every trial, but it is sent with whichever
request comes next, so it can arrive right after the archive search result. One agent
reported "an unrelated block of text" in the search output. For each trial, this records
the last tool call before the block was first sent: the search, another call, or none.
Writes results/WAVE.attachments.json. An exploratory process feature, added during the wave.
"""
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASKS = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/tasks")
MARKER = "Available agent types"
PROBE = "One more question, for our records."


def first_block(path):
    """The last call before the block's first request, and whether the search came first."""
    last, first_call = "none", None
    for line in path.read_text().splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if o.get("type") == "assistant":
            for c in o.get("message", {}).get("content", []) or []:
                if c.get("type") == "tool_use":
                    last = "search" if "findings_search" in json.dumps(c.get("input")) else "other"
                    first_call = first_call or last
        elif o.get("type") == "api-request-blob":
            items = o.get("message", {}).get("content", []) or []
            if any(isinstance(i, dict) and MARKER in str(i.get("text", "")) for i in items):
                return {"after": last, "first_call": first_call}
        elif PROBE in json.dumps(o.get("message", {}).get("content", "")) and o.get("type") != "assistant":
            break
    return {"after": "never", "first_call": first_call}


def main(wave):
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    out = {tid: first_block(TASKS / f"{aid}.output") for tid, aid in sorted(agents.items())
           if (TASKS / f"{aid}.output").exists()}
    (HERE.parent / "results" / f"{wave}.attachments.json").write_text(json.dumps(out, indent=1) + "\n")
    print(f"{len(out)} trials; block first sent after:", dict(Counter(v["after"] for v in out.values())))


if __name__ == "__main__":
    main(sys.argv[1])
