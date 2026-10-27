"""Written during 012's blind review: writes results/WAVE.contamination-review.json from transcript structure.

  python3 -I write_review.py AGENTS_JSON TASKS_DIR OUT_JSON

The four exclusion notes were written by hand from the structural views (synthetic entries, cut-off
notices, entry types and tool names). The keep notes for trials held by a pause are generated, after
checking that every re-sent request carried the same messages with nothing appended. No conditions,
no outcomes and no agent-written content are read.
"""
import json, sys
from datetime import datetime
agents = json.load(open(sys.argv[1]))
tasks, out_path = sys.argv[2], sys.argv[3]

def ts(r):
    t = r.get("timestamp")
    return datetime.fromisoformat(t.replace("Z", "+00:00")) if t else None

def hms(d):
    return d.strftime("%H:%M:%S")

NOTE = ("No '<synthetic>' or API-error entry and no cut-off notice reached the agent, and no response was cut off "
        "mid-stream, so this is not an interrupted API response under the pre-registered rule. Kept and noted. "
        "An unplanned sensitivity analysis without the 21 kept trials held by a pause, decided here before any "
        "assignment was opened, will be reported and labelled as unplanned.")
EXCLUDE = {
    "main12-a4151e": ("Infrastructure failure during the task: one API response stopped arriving (assistant step 21 of 43, "
                      "before its hand-back). The request went out at 21:21:36 UTC, as the second session-wide pause began; at "
                      "22:29:04 the harness recorded a '<synthetic>' entry, 'API Error: The response stopped arriving. The "
                      "response above may be incomplete.', which reached the agent. The run then continued and finished. "
                      "Excluded by the pre-registered rule, as 006's main6-025db7 was. No flagged call."),
    "main12-87baf9": ("Infrastructure failure during the task: a response was cut off mid-stream at 20:48:55 UTC, as the first "
                      "session-wide pause began (8 output tokens recorded). At 21:18:04 the harness told the agent 'Your response "
                      "above was cut off mid-stream and only your next message is delivered.' The agent then read the code, "
                      "edited names.py and the tests, ran the tests, wrote NOTES.md and handed back. An API response that stopped "
                      "arriving before the hand-back: excluded by the pre-registered rule. transcripts.py counted only "
                      "'<synthetic>' entries; its detector was extended to this notice in the blind review. No flagged call."),
    "main12-1c5903": ("Infrastructure failure during the task: a response that ended the agent's turn was cut off mid-stream at "
                      "21:21:35 UTC, as the second session-wide pause began (3 output tokens recorded). At 22:29:04 the harness "
                      "told the agent its response was cut off and only its next message would be delivered. After the pause it "
                      "wrote NOTES.md again, ran one command and handed back at 22:44:33. An API response that stopped arriving "
                      "before the hand-back: excluded by the pre-registered rule. transcripts.py counted only '<synthetic>' "
                      "entries; its detector was extended to this notice in the blind review. No flagged call."),
    "main12-4d8254": ("Infrastructure failure during the task: a response that ended the agent's turn was cut off mid-stream at "
                      "21:21:36 UTC, as the second session-wide pause began (6 output tokens recorded). At 22:29:04 the harness "
                      "told the agent its response was cut off and only its next message would be delivered. After the pause it "
                      "wrote NOTES.md again, ran one command and handed back at 22:44:49. An API response that stopped arriving "
                      "before the hand-back: excluded by the pre-registered rule. transcripts.py counted only '<synthetic>' "
                      "entries; its detector was extended to this notice in the blind review. No flagged call."),
}
GIT = {"main12-aea86d": (" Separately, transcripts.py's git-or-bd pattern matched a Bash command only because the word 'git' "
                         "appears inside an echo string ('(no git used)'). Every file the command read (cat, find) is inside the "
                         "trial, and no git or bd command was run.")}

review = {}
for tid, aid in sorted(agents.items()):
    rows = [json.loads(l) for l in open(f"{tasks}/{aid}.output") if l.strip()]
    if tid in EXCLUDE:
        review[tid] = {"decision": "exclude", "kind": "infrastructure", "why": EXCLUDE[tid]}
        continue
    stamped = [(i, ts(r)) for i, r in enumerate(rows) if ts(r)]
    gaps = [(i, j) for (i, a), (j, b) in zip(stamped, stamped[1:]) if (b - a).total_seconds() > 300]
    if not gaps:
        if tid in GIT:
            review[tid] = {"decision": "keep", "kind": "git flag", "why": GIT[tid].strip()}
        continue
    # One episode per wait: from the last request before the first gap to the response that ended it.
    reqs = [(i, r) for i, r in enumerate(rows) if r.get("type") == "api-request"]
    episodes = {}
    for gi, gj in gaps:
        nxt = min((i for i, r in enumerate(rows) if i > gi and r.get("type") == "assistant"), default=len(rows))
        episodes.setdefault(nxt, gi)
    parts = []
    for nxt, gi in sorted(episodes.items()):
        before = [(i, r) for i, r in reqs if i <= gi]
        if not before:
            raise SystemExit(f"{tid}: gap without a request before it")
        first_i, first = before[-1]
        resent = [r for i, r in reqs if first_i < i < nxt]
        n_first = first["keep"] + len(first.get("tail") or [])
        if not all(r["keep"] + len(r.get("tail") or []) == n_first and not r.get("tail") for r in resent):
            raise SystemExit(f"{tid}: a re-sent request did not carry the same messages; review by hand")
        t0 = ts(first)
        pause = "first" if t0.hour == 20 else "second"
        times = ", ".join(hms(ts(r)) for r in resent)
        toks = sorted({first["params"]["max_tokens"]} | {r["params"]["max_tokens"] for r in resent}, reverse=True)
        parts.append(f"one API request sent at {hms(t0)} UTC, as the {pause} session-wide pause began, got no response; the client "
                     f"re-sent the same {n_first} messages, with nothing appended, at {times}"
                     + (f" (max_tokens {toks[0]} then {toks[-1]})" if len(toks) > 1 else "")
                     + f", and the agent went on from there at {hms(ts(rows[nxt]))}")
    why = "Ran across " + ("both session-wide pauses" if len(parts) > 1 else "a session-wide pause") + " of 2026-10-27: " + "; ".join(parts) + ". " + NOTE + GIT.get(tid, "")
    review[tid] = {"decision": "keep", "kind": "infrastructure", "why": why}

json.dump(review, open(out_path, "w"), indent=1, ensure_ascii=False)
kinds = {}
for v in review.values():
    kinds[(v["decision"], v["kind"])] = kinds.get((v["decision"], v["kind"]), 0) + 1
print(len(review), "entries", kinds)
