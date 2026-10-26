"""Exploratory checks for experiment 005, added after unblinding. Not pre-registered.

  python3 explore.py WAVE > ../results/explore-WAVE.md

Adoption by process features that agents chose themselves (so these are correlations,
not effects): whether the agent read the code or docs before its first search run,
whether its flagged calls were listings outside the trial, and where Claude Code's
generic context block first arrived (attachments.py). Also counts follow-up answers
that refer to the guided notice or its wording, by text match.
"""
import json
import math
import re
import sys
from pathlib import Path

from transcripts import TASKS, phases, text_of

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
NOTE_CELLS = ("human_plain", "model_plain", "human_guided", "model_guided")
RUN = re.compile(r"python3?\s+(-I\s+)?\S*findings_search\.py\s+['\"]")
LOOK = re.compile(r"\b(cat|sed|head|less|grep)\b[^|;&]*(totals\.py|accounting-rules)")
NOTICE = re.compile(r"\bnotices?\b|guidance|search (tool|output|results?) (says|treats|notes|states|warns)"
                    r"|mirror (treats|says|notes)|declared,? (and )?not verified"
                    r"|provenance is (only |just )?(a )?(declared )?claim", re.I)


def fisher(a, b, c, d):
    n1, n2, k = a + b, c + d, a + c

    def pmf(x):
        return math.comb(n1, x) * math.comb(n2, k - x) / math.comb(n1 + n2, k)

    p0 = pmf(a)
    return min(1.0, sum(pmf(x) for x in range(max(0, k - n2), min(k, n1) + 1) if pmf(x) <= p0 * (1 + 1e-9)))


def inspected_before_search(path):
    """True if a Read or shell read of totals.py or the rules doc came before the first search run."""
    (task, _), _ = phases(path)
    first_run = first_look = None
    for i, (name, inp) in enumerate(task["calls"]):
        s = text_of(inp)
        if first_run is None and name == "Bash" and RUN.search(s):
            first_run = i
        looks = name == "Read" and any(k in str(inp.get("file_path", "")) for k in ("totals.py", "accounting-rules"))
        looks = looks or (name == "Bash" and LOOK.search(s) is not None)
        if first_look is None and looks:
            first_look = i
    return None if first_run is None else (first_look is not None and first_look < first_run)


def split(title, rows, key):
    out = [f"### {title}", "", "| cell | yes | no |", "| --- | --- | --- |"]
    tot = {True: [0, 0], False: [0, 0]}
    for c in NOTE_CELLS:
        cells = []
        for v in (True, False):
            rs = [r for r in rows if r["cell"] == c and key(r) is v]
            k = sum(r["adopted"] for r in rs)
            tot[v][0] += k
            tot[v][1] += len(rs)
            cells.append(f"{k}/{len(rs)}")
        out.append(f"| {c} | " + " | ".join(cells) + " |")
    (k1, n1), (k2, n2) = tot[True], tot[False]
    out += [f"| all note cells | {k1}/{n1} | {k2}/{n2} |", "",
            f"Adoption, yes against no: Fisher p = {fisher(k1, n1 - k1, k2, n2 - k2):.3f}", ""]
    return out


def main(wave):
    assignment = json.loads((HERE / "assignments" / f"{wave}.json").read_text())
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    res = {r["trial"]: r for r in map(json.loads, (RESULTS / f"{wave}.jsonl").read_text().splitlines())}
    proc = {r["trial"]: r for r in map(json.loads, (RESULTS / f"{wave}.process.jsonl").read_text().splitlines())}
    att = json.loads((RESULTS / f"{wave}.attachments.json").read_text())
    rows = [{"trial": t, "cell": a["cell"], "adopted": res[t]["outcome"] == "adopted_note",
             "inspected": inspected_before_search(TASKS / f"{agents[t]}.output"),
             "flagged": bool(proc[t]["contamination"]), "block_after_search": att[t]["after"] == "search",
             "cites_notice": bool(NOTICE.search(proc[t].get("answer") or ""))} for t, a in sorted(assignment.items())]
    out = [f"# Experiment 005, exploratory checks after unblinding: wave {wave}", "",
           "Not pre-registered. Each table splits adoption of the note by a feature the agent chose, so it shows a correlation.", ""]
    out += split("Read the code or docs before the first search run", rows, lambda r: r["inspected"])
    out += split("Had a flagged listing outside the trial directory", rows, lambda r: r["flagged"])
    out += split("Claude Code's generic context block first arrived right after the search", rows,
                 lambda r: r["block_after_search"])
    out += ["### Follow-up answers that refer to the notice or its wording (text match)", "",
            "| cell | refer to it | adopted among them |", "| --- | --- | --- |"]
    for c in ("none_plain", "none_guided") + NOTE_CELLS:
        rs = [r for r in rows if r["cell"] == c]
        cite = [r for r in rs if r["cites_notice"]]
        out.append(f"| {c} | {len(cite)}/{len(rs)} | {sum(r['adopted'] for r in cite)} |")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1])
