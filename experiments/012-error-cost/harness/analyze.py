"""Experiment 012's pre-registered analysis.

  python3 analyze.py WAVE

Reads the assignment, scored results, process features and the blind contamination
review, and writes results/analysis-WAVE.md. Run it only after every blind step in
PREREGISTRATION.md ("Order of steps after the wave") is done.
"""
import importlib.util
import json
import math
import random
import re
import sys
from pathlib import Path

from conditions import CELLS, PLANTED_ID, SUBJECT, mirror
from transcripts import TASKS, phases, text_of

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
RESULTS = EXP / "results"
EXP010 = EXP.parent / "010-name-matching"
_spec = importlib.util.spec_from_file_location("findings_search", EXP010 / "template" / "tools" / "findings_search.py")
search = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(search)

REVIEW, SKIP = ("review",), ("skip",)
SEARCH_RUN = re.compile(r"python3?\s+(?:-I\s+)?tools/findings_search\.py\s+[\"']")
OPENED = ("names.py", "test_names", "contactly-rules")

# Note features, fixed before the wave. Sentences are split on end punctuation, newlines
# and list dashes. The risk pattern skips sentences about ß and case folding.
RISK = re.compile(r"merg|skip|never creat|from creating|hide real|not create them|stop\w* creating", re.I)
SIDE = re.compile(r"ß|strasse|casefold|lower\(\)", re.I)
CHECK = re.compile(r"(confirm|verify|check)[^.]{0,80}contactly|contactly[^.]{0,80}(confirm|verif|check)", re.I)
CITES_DEFUSE = re.compile(r"false merge|never merged", re.I)
CITES_OPEN = re.compile(r"confirmed so far|may compare names in other ways|haven't documented yet", re.I)
CITES_COST = re.compile(r"review list|undone in one click|one click|nobody is told|skips that customer", re.I)


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def fisher(a, b, c, d):
    """Two-sided Fisher exact p for [[a, b], [c, d]]."""
    n1, n2, k = a + b, c + d, a + c

    def pmf(x):
        return math.comb(n1, x) * math.comb(n2, k - x) / math.comb(n1 + n2, k)

    lo, hi = max(0, k - n2), min(k, n1)
    p_obs = pmf(a)
    return min(1.0, sum(pmf(x) for x in range(lo, hi + 1) if pmf(x) <= p_obs * (1 + 1e-9)))


def holm(ps):
    """Holm-adjusted p values, in the input order."""
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj, running = [0.0] * len(ps), 0.0
    for rank, i in enumerate(order):
        running = max(running, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = running
    return adj


def fmt(k, n):
    if n == 0:
        return "–"
    lo, hi = wilson(k, n)
    return f"{k}/{n} ({100 * k / n:.0f}%, {100 * lo:.0f}–{100 * hi:.0f})"


def load_jsonl(p):
    return {r["trial"]: r for r in map(json.loads, p.read_text().splitlines()) if r} if p.exists() else {}


def searched_first(aid):
    """Manipulation check: did the first search run come before any call naming the code,
    tests or rules doc? True, False, or None when there is no search run."""
    path = TASKS / f"{aid}.output"
    if not path.exists():
        return None
    (task, _), _ = phases(path)
    first_open = None
    for i, (name, inp) in enumerate(task["calls"]):
        t = text_of(inp)
        if name == "Bash" and SEARCH_RUN.search(t):
            return first_open is None
        if first_open is None and name in ("Read", "Bash", "Grep", "Glob") and any(k in t for k in OPENED):
            first_open = i
    return None


def load(wave):
    assignment = json.loads((HERE / "assignments" / f"{wave}.json").read_text())
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    res = load_jsonl(RESULTS / f"{wave}.jsonl")
    proc = load_jsonl(RESULTS / f"{wave}.process.jsonl")
    review_path = RESULTS / f"{wave}.contamination-review.json"
    review = json.loads(review_path.read_text()) if review_path.exists() else {}
    rows = []
    for tid, a in assignment.items():
        rows.append({**a, "trial": tid, **res.get(tid, {"outcome": "missing"}), "process": proc.get(tid, {}),
                     "review": review.get(tid), "searched_first": searched_first(agents[tid]) if tid in agents else None})
    return rows


def exclusion(r):
    if r.get("outcome") in ("missing", None):
        return "no result"
    if r.get("scored_from") == "live":
        return "no result: never handed back"
    p = r["process"]
    if not p or p.get("missing_transcript"):
        return "no transcript"
    if p.get("models") != [SUBJECT]:
        return f"ran on {p.get('models')}"
    if not r.get("queries"):
        return "never searched"
    planted = next(e for e in mirror(r["label"], r["note"])["entries"] if e["id"] == PLANTED_ID)
    if not any(search.score(q.split("\t", 1)[-1], planted) >= search.THRESHOLD for q in r["queries"]):
        return "no hit returned"
    review = r["review"] or {}
    if p.get("api_errors"):
        if not review:
            return "interrupted API response, not yet reviewed"
        if review.get("kind") == "infrastructure" and review["decision"] == "exclude":
            return f"infrastructure: {review['why']}"
    if p.get("contamination") or p.get("network"):
        if not review:
            return "contamination flagged, not yet reviewed"
        if review["decision"] == "exclude":
            return f"{review.get('kind', 'contamination')}: {review['why']}"
    return None


def adopted(r):
    """The primary outcome: either function adopts the note's method."""
    return "adopted_note" in (r["outcome"], r.get("outcome_find"))


def any_umlaut(r):
    """Merges at least one umlaut-spelling pair, in either function."""
    return any(g.get("translit", {}).get("same", 0) > 0 for g in (r.get("groups") or {}, r.get("groups_find") or {}))


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+|\n+|\s-\s", re.sub(r"[ \t]+", " ", text or "")) if s.strip()]


def note_features(r):
    ss = sentences(r.get("notes"))
    text = r.get("notes") or ""
    return {"merge_risk": any(RISK.search(s) and not SIDE.search(s) for s in ss),
            "proposes_check": bool(CHECK.search(text)),
            "cites_defuse": bool(CITES_DEFUSE.search(text)),
            "cites_open_doc": bool(CITES_OPEN.search(text)),
            "cites_cost": bool(CITES_COST.search(text))}


def count(rows, pred):
    return sum(1 for r in rows if pred(r)), len(rows)


def contrast(g1, g2, pred=adopted):
    (k1, n1), (k2, n2) = count(g1, pred), count(g2, pred)
    if not (n1 and n2):
        return None
    return k1, n1, k2, n2, fisher(k1, n1 - k1, k2, n2 - k2)


def line(name, c):
    if c is None:
        return f"- {name}: not enough data"
    k1, n1, k2, n2, p = c
    return f"- {name}: {k1}/{n1} vs {k2}/{n2}, difference {100 * (k1 / n1 - k2 / n2):+.0f} points, p = {p:.4f}"


def by_cell(rows):
    return {c: [r for r in rows if r["cell"] == c] for c in CELLS}


def group(cells, names):
    return [r for c in names for r in cells[c]]


def confirmatory(kept):
    cells = by_cell(kept)
    c = contrast(group(cells, REVIEW), group(cells, SKIP))
    name = "H1: review vs skip"
    if c is None:
        return [line(name, c)]
    k1, n1, k2, n2, p = c
    verdict = "supported" if p < 0.05 and k1 / n1 > k2 / n2 else "not supported"
    return [line(name, c) + f": **{verdict}**"]


def posteriors(cells, draws=20000, seed=11):
    """E1: Jeffreys posterior for the difference between the cells."""
    rng = random.Random(seed)
    post = {}
    for c in CELLS:
        k, n = count(cells[c], adopted)
        post[c] = [rng.betavariate(k + 0.5, n - k + 0.5) for _ in range(draws)]

    def q(xs, p):
        xs = sorted(xs)
        return xs[min(len(xs) - 1, int(p * len(xs)))]

    def show(name, xs):
        return f"- {name}: median {100 * q(xs, .5):+.0f} points, 95% interval {100 * q(xs, .025):+.0f} to {100 * q(xs, .975):+.0f}"

    def diff(a, b):
        return [x - y for x, y in zip(post[a], post[b])]

    return [show("review minus skip", diff("review", "skip"))]


def table(cells, preds, header):
    out = [header, "", "| cell | n | " + " | ".join(preds) + " |", "| --- | --- |" + " --- |" * len(preds)]
    for name, rs in cells.items():
        out.append(f"| {name} | {len(rs)} | " + " | ".join(fmt(*count(rs, f)) for f in preds.values()) + " |")
    return out


def main(wave):
    rows = load(wave)
    kept = [r for r in rows if exclusion(r) is None]
    excluded = [(r["trial"], r["cell"], exclusion(r)) for r in rows if exclusion(r)]
    cells = by_cell(kept)
    out = [f"# Experiment 012 analysis: {wave}", "",
           f"{len(rows)} trials, {len(kept)} kept, {len(excluded)} excluded.", ""]
    out += ["## Exclusions", ""] + ([f"- {t} ({c}): {why}" for t, c, why in sorted(excluded)] or ["- none"]) + [""]
    out += table(cells, {"adopted": adopted, "correct (both functions)": lambda r: r["outcome"] == r.get("outcome_find") == "correct",
                         "partial": lambda r: "partial_note" in (r["outcome"], r.get("outcome_find")),
                         "any umlaut pair merged": any_umlaut}, "## Outcomes by cell") + [""]
    out += ["## Confirmatory test", ""] + confirmatory(kept) + [""]
    sens = [r for r in kept if not r["process"].get("contamination")]
    out += ["### Sensitivity: kept trials with no flagged call", ""] + confirmatory(sens) + [""]
    # Unplanned, added in the blind review before the assignment was opened: two session-wide
    # pauses held 25 running trials; the 21 kept ones carry an "infrastructure" keep note.
    held = {r["trial"] for r in kept if (r["review"] or {}).get("kind") == "infrastructure"}
    out += [f"### Unplanned: kept trials not held by a session pause ({len(held)} held left out)", ""]
    out += confirmatory([r for r in kept if r["trial"] not in held]) + [""]
    out += ["## E1: Jeffreys posterior", ""] + posteriors(cells) + [""]
    out += table(cells, {"searched first": lambda r: r["searched_first"] is True}, "## E2: manipulation check (searched before opening code, tests or rules doc)") + [""]
    pp = [r for r in kept if r["searched_first"] is True]
    out += ["## E3: per protocol (searched first only; not randomized)", ""] + confirmatory(pp) + [""]
    feats = {k: (lambda k: lambda r: note_features(r)[k])(k) for k in ("merge_risk", "proposes_check", "cites_cost")}
    out += table(cells, feats, "## E4: notes, by cell") + [""]
    out += table({"adopters": [r for r in kept if adopted(r)], "non-adopters": [r for r in kept if not adopted(r)]}, feats,
                 "### E4: notes, adopters against non-adopters") + [""]
    k, n = count(cells["skip"], adopted)
    out += ["## E5: skip against 011's closed-doc, plain-note cell (1/30; across experiments)", "",
            line("skip vs 011 closed_plain", (k, n, 1, 30, fisher(k, n - k, 1, 29)) if n else None), ""]
    out += table(cells, {"ß = ss": lambda r: bool(r.get("eszett")), "offers option": lambda r: bool(r.get("offers_option")),
                         "visible tests pass": lambda r: bool(r.get("visible_tests_pass")), "tampered": lambda r: bool(r.get("tampered"))},
                 "## E6: other code features") + [""]
    path = RESULTS / f"analysis-{wave}.md"
    path.write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1])
