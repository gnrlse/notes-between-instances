"""Write results/WAVE.contamination-review.json for the blind review, from transcript structure.

  python3 -I write_review.py WAVE [HAND_NOTES_JSON]

HAND_NOTES_JSON maps trial ids to {"decision", "kind", "why"} written by hand in the blind
review, for every trial with an interrupted response, a flagged call or a git-or-bd flag
(contamination_review.py, contamination_detail.py and the structural views show what is
needed). Trials held by a session-wide pause, with every re-sent request carrying the same
messages and nothing appended, get a generated keep note of kind "infrastructure". The script
stops if a flagged trial has no hand note, or if a re-sent request changed. It reads no
conditions, no outcomes and no agent-written content.
"""
import json
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASKS = Path("/tmp/claude-502/-home-miki-c/c8ad033d-f2a8-4ff1-ba3c-35d4ef5410e7/tasks")
GAP_SECONDS = 300
NOTE = ("No '<synthetic>' or API-error entry and no cut-off notice reached the agent, so this is not an interrupted API "
        "response under the pre-registered rule. Kept and noted; the pre-registered sensitivity analysis leaves it out.")


def ts(r):
    t = r.get("timestamp")
    return datetime.fromisoformat(t.replace("Z", "+00:00")) if t else None


def held_note(tid, rows):
    stamped = [(i, ts(r)) for i, r in enumerate(rows) if ts(r)]
    gaps = [i for (i, a), (j, b) in zip(stamped, stamped[1:]) if (b - a).total_seconds() > GAP_SECONDS]
    if not gaps:
        return None
    reqs = [(i, r) for i, r in enumerate(rows) if r.get("type") == "api-request"]
    episodes = {}
    for gi in gaps:
        nxt = min((i for i, r in enumerate(rows) if i > gi and r.get("type") == "assistant"), default=len(rows))
        episodes.setdefault(nxt, gi)
    parts = []
    for nxt, gi in sorted(episodes.items()):
        before = [(i, r) for i, r in reqs if i <= gi]
        if not before:
            sys.exit(f"{tid}: a gap with no request before it; review by hand")
        first_i, first = before[-1]
        resent = [r for i, r in reqs if first_i < i < nxt]
        n_first = first["keep"] + len(first.get("tail") or [])
        if not all(r["keep"] + len(r.get("tail") or []) == n_first and not r.get("tail") for r in resent):
            sys.exit(f"{tid}: a re-sent request did not carry the same messages; review by hand")
        resumed = ts(rows[nxt]).strftime("%H:%M:%S") if nxt < len(rows) else "the end"
        parts.append(f"one API request sent at {ts(first).strftime('%H:%M:%S')} UTC got no response; the client re-sent the same "
                     f"{n_first} messages, with nothing appended, at {', '.join(ts(r).strftime('%H:%M:%S') for r in resent)}, "
                     f"and the agent went on from there at {resumed}")
    return "Ran across a session-wide pause: " + "; ".join(parts) + ". " + NOTE


def main(wave, hand_path=None):
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    proc = {r["trial"]: r for r in map(json.loads, (HERE.parent / "results" / f"{wave}.process.jsonl").read_text().splitlines()) if r}
    hand = json.loads(Path(hand_path).read_text()) if hand_path else {}
    review = {}
    for tid, aid in sorted(agents.items()):
        p = proc.get(tid, {})
        flagged = p.get("api_errors") or p.get("contamination") or p.get("network") or p.get("git_or_bd")
        if tid in hand:
            review[tid] = hand[tid]
            continue
        if flagged:
            sys.exit(f"{tid}: flagged in transcripts.py but has no hand note")
        rows = [json.loads(l) for l in (TASKS / f"{aid}.output").read_text().splitlines() if l.strip()]
        why = held_note(tid, rows)
        if why:
            review[tid] = {"decision": "keep", "kind": "infrastructure", "why": why}
    out = HERE.parent / "results" / f"{wave}.contamination-review.json"
    out.write_text(json.dumps(review, indent=1, ensure_ascii=False))
    kinds = {}
    for v in review.values():
        kinds[f"{v['decision']} {v['kind']}"] = kinds.get(f"{v['decision']} {v['kind']}", 0) + 1
    print(len(review), "entries", kinds)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
