"""Pre-registered analysis for experiment 007.

  python3 analyze.py WAVE

Joins assignments, hidden-check results, transcript features, blind judge codes and
the blind review, applies the pre-registered exclusions, and prints a Markdown report.
The two confirmatory tests pool over the other factor: order (search first against
inspect first) and notice (neutral against plain).
"""
import importlib.util
import json
import math
import random
import re
import statistics
import sys
from pathlib import Path

from conditions import CELLS, SUBJECT, mirror
from transcripts import TASKS, phases, text_of

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
RESULTS = EXP / "results"
EXP002 = EXP.parent / "002-no-competing-source"
EXP006 = EXP.parent / "006-guidance-content"

spec = importlib.util.spec_from_file_location("findings_search", EXP002 / "template" / "tools" / "findings_search.py")
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)

RUN = re.compile(r"python3?\s+(-I\s+)?\S*findings_search\.py\s+['\"]")
LOOK = re.compile(r"\b(cat|sed|head|less|grep|tail|awk|nl)\b[^|;&]*(totals\.py|accounting-rules)")
SEARCH_FIRST = ("search_plain", "search_neutral")
INSPECT_FIRST = ("inspect_plain", "inspect_neutral")
PLAIN = ("search_plain", "inspect_plain")
NEUTRAL = ("search_neutral", "inspect_neutral")


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


def order_of_work(aid):
    """For the manipulation check: did a read of the code, tests or rules doc come before the first search run?

    Returns True (read first), False (searched first) or None (no search run). Reading
    WORKFLOW.md or README.md does not count."""
    path = TASKS / f"{aid}.output"
    if not path.exists():
        return None
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


def load(wave):
    assignment = json.loads((HERE / "assignments" / f"{wave}.json").read_text())
    agents = json.loads((HERE / "agents" / f"{wave}.json").read_text())
    res = load_jsonl(RESULTS / f"{wave}.jsonl")
    proc = load_jsonl(RESULTS / f"{wave}.process.jsonl")
    codes = {k: load_jsonl(RESULTS / f"{wave}.{k}.codes.jsonl") for k in ("supplementary",)}
    review_path = RESULTS / f"{wave}.contamination-review.json"
    review = json.loads(review_path.read_text()) if review_path.exists() else {}
    att_path = RESULTS / f"{wave}.attachments.json"
    att = json.loads(att_path.read_text()) if att_path.exists() else {}
    rows = []
    for tid, a in assignment.items():
        rows.append({**a, "trial": tid, **res.get(tid, {"outcome": "missing"}), "process": proc.get(tid, {}),
                     **{k: v.get(tid, {}) for k, v in codes.items()}, "review": review.get(tid),
                     "read_first": order_of_work(agents[tid]) if tid in agents else None,
                     "block_after_search": att.get(tid, {}).get("after") == "search"})
    return rows


def exclusion(r):
    if r.get("outcome") in ("missing", None):
        return "no result"
    p = r["process"]
    if not p or p.get("missing_transcript"):
        return "no transcript"
    if p.get("models") != [SUBJECT]:
        return f"ran on {p.get('models')}"
    if not r.get("queries"):
        return "never searched"
    planted = mirror(r["label"])["entries"][0]
    if not any(search.score(q.split("\t", 1)[-1], planted) >= search.THRESHOLD for q in r["queries"]):
        return "no hit returned"
    review = r["review"] or {}
    # Pre-registered: an interrupted API response before the result was handed back is an
    # infrastructure failure; one after it is not. The blind review records which.
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
    return r["outcome"] == "adopted_note"


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


def code(kind, key):
    return lambda r: bool(r[kind].get(key))


def by_cell(rows):
    return {c: [r for r in rows if r["cell"] == c] for c in CELLS}


def group(cells, names):
    return [r for c in names for r in cells[c]]


def confirmatory(kept):
    """The two pre-registered tests on these trials, as report lines."""
    cells = by_cell(kept)
    tests = [
        ("H1: search first vs inspect first, pooled over notices", contrast(group(cells, SEARCH_FIRST), group(cells, INSPECT_FIRST))),
        ("H2: neutral vs plain notice, pooled over order", contrast(group(cells, NEUTRAL), group(cells, PLAIN))),
    ]
    out = []
    adj = holm([c[4] if c else 1.0 for _, c in tests])
    for (name, c), a in zip(tests, adj):
        if c is None:
            out.append(line(name, c))
            continue
        k1, n1, k2, n2, p = c
        verdict = "supported" if a < 0.05 and k1 / n1 > k2 / n2 else "not supported"
        out.append(line(name, c) + f", Holm-adjusted p = {a:.4f}: **{verdict}**")
    return out


def posteriors(cells, draws=20000, seed=7):
    """E1: Jeffreys posteriors for the two simple effects and their difference."""
    rng = random.Random(seed)
    post = {}
    for c in CELLS:
        k, n = count(cells[c], adopted)
        post[c] = [rng.betavariate(k + 0.5, n - k + 0.5) for _ in range(draws)]

    def q(xs, p):
        xs = sorted(xs)
        return xs[min(len(xs) - 1, int(p * len(xs)))]

    def show(name, xs):
        return (f"- {name}: median {100 * q(xs, .5):+.0f} points, "
                f"95% interval {100 * q(xs, .025):+.0f} to {100 * q(xs, .975):+.0f}")

    order_plain = [s - i for s, i in zip(post["search_plain"], post["inspect_plain"])]
    order_neutral = [s - i for s, i in zip(post["search_neutral"], post["inspect_neutral"])]
    notice_search = [n - p for n, p in zip(post["search_neutral"], post["search_plain"])]
    notice_inspect = [n - p for n, p in zip(post["inspect_neutral"], post["inspect_plain"])]
    return [show("order effect (search first minus inspect first) under the plain notice", order_plain),
            show("order effect under the neutral notice", order_neutral),
            show("difference in differences (neutral minus plain)", [b - a for a, b in zip(order_plain, order_neutral)]),
            show("notice effect (neutral minus plain) when searching first", notice_search),
            show("notice effect when inspecting first", notice_inspect)]


def from_006():
    """006's kept plain and neutral trials, by its blind review's exclusions."""
    a6 = json.loads((EXP006 / "harness" / "assignments" / "main6.json").read_text())
    r6 = load_jsonl(EXP006 / "results" / "main6.jsonl")
    rev = json.loads((EXP006 / "results" / "main6.contamination-review.json").read_text())
    keep = [t for t in a6 if not (rev.get(t, {}).get("decision") == "exclude")]
    return ([r6[t] for t in keep if a6[t]["cell"] == "plain"], [r6[t] for t in keep if a6[t]["cell"] == "neutral"])


def table(rows_by, keys, kind, header):
    out = ["| cell | n | " + " | ".join(keys) + " |", "| --- | --- |" + " --- |" * len(keys)]
    for name, rs in rows_by.items():
        out.append(f"| {name} | {len(rs)} | " + " | ".join(fmt(*count(rs, code(kind, k))) for k in keys) + " |")
    return [header, ""] + out


def split(rows, key, title):
    out = [f"### {title}", "", "| cell | yes | no |", "| --- | --- | --- |"]
    tot = {True: [0, 0], False: [0, 0]}
    for c, rs in by_cell(rows).items():
        cells = []
        for v in (True, False):
            sub = [r for r in rs if key(r) is v]
            k = sum(adopted(r) for r in sub)
            tot[v][0] += k
            tot[v][1] += len(sub)
            cells.append(f"{k}/{len(sub)}")
        out.append(f"| {c} | " + " | ".join(cells) + " |")
    (k1, n1), (k2, n2) = tot[True], tot[False]
    out += [f"| all | {k1}/{n1} | {k2}/{n2} |", "",
            f"Adoption, yes against no: Fisher p = {fisher(k1, n1 - k1, k2, n2 - k2):.3f}" if n1 and n2 else "", ""]
    return out


def main(wave):
    rows = load(wave)
    excluded = [(r, exclusion(r)) for r in rows]
    kept = [r for r, why in excluded if why is None]
    out = [f"# Experiment 007 analysis: wave {wave}", ""]
    out.append(f"Trials: {len(rows)}. Kept: {len(kept)}. Excluded: {len(rows) - len(kept)}.")
    for r, why in sorted(excluded, key=lambda x: x[0]["trial"]):
        if why:
            out.append(f"- excluded {r['trial']} ({r['cell']}): {why}")
    effort = sorted({e for r in kept for e in r["process"].get("effort", [])})
    out.append(f"- effort levels recorded in kept transcripts: {', '.join(effort) or 'none recorded'}")
    out.append(f"- scored from snapshots: {sum(1 for r in kept if r.get('scored_from') == 'snapshot')}/{len(kept)}")

    cells = by_cell(kept)
    out += ["", "## Outcomes by cell (Wilson 95% intervals)", "",
            "| cell | n | adopted note | correct | other outcomes | any per-line VAT | per-line option in code |",
            "| --- | --- | --- | --- | --- | --- | --- |"]
    for c, rs in cells.items():
        others = {}
        for r in rs:
            if r["outcome"] not in ("adopted_note", "correct"):
                others[r["outcome"]] = others.get(r["outcome"], 0) + 1
        out.append("| " + " | ".join([
            c, str(len(rs)), fmt(*count(rs, adopted)), fmt(*count(rs, lambda r: r["outcome"] == "correct")),
            ", ".join(f"{k} {v}" for k, v in sorted(others.items())) or "–",
            fmt(*count(rs, lambda r: r["outcome"] in ("adopted_note", "per_line_half_even"))),
            fmt(*count(rs, lambda r: r.get("offers_per_line_option"))),
        ]) + " |")

    out += ["", "## Confirmatory tests (two-sided Fisher exact, Holm-adjusted across the two)", ""]
    out += confirmatory(kept)
    clean = [r for r in kept if not r["process"].get("contamination")]
    out += ["", f"### Sensitivity: only the {len(clean)} kept trials with no flagged call outside the trial directory", ""]
    out += confirmatory(clean)

    out += ["", "## Manipulation check: the order agents actually worked in", "",
            "| cell | n | read code or docs before the first search | searched first | read WORKFLOW.md |",
            "| --- | --- | --- | --- | --- |"]
    for c, rs in cells.items():
        out.append(f"| {c} | {len(rs)} | {fmt(*count(rs, lambda r: r['read_first'] is True))} | "
                   f"{fmt(*count(rs, lambda r: r['read_first'] is False))} | "
                   f"{fmt(*count(rs, lambda r: r.get('read', {}).get('WORKFLOW.md')))} |")

    out += ["", "## Exploratory", "", "### E1: simple effects and the interaction (Jeffreys posteriors)", ""]
    out += posteriors(cells)
    out += ["", "### E2: simple effects (unadjusted Fisher)", ""]
    out.append(line("search first vs inspect first, plain notice", contrast(cells["search_plain"], cells["inspect_plain"])))
    out.append(line("search first vs inspect first, neutral notice", contrast(cells["search_neutral"], cells["inspect_neutral"])))
    out.append(line("neutral vs plain, searching first", contrast(cells["search_neutral"], cells["search_plain"])))
    out.append(line("neutral vs plain, inspecting first", contrast(cells["inspect_neutral"], cells["inspect_plain"])))
    out += ["", "### E3: per protocol (only agents that worked in their assigned order)", ""]
    comp_s = [r for r in group(cells, SEARCH_FIRST) if r["read_first"] is False]
    comp_i = [r for r in group(cells, INSPECT_FIRST) if r["read_first"] is True]
    out.append(line("search first vs inspect first, compliers only", contrast(comp_s, comp_i)))
    out += ["", "### E4: neutral against plain, pooled with 006", ""]
    p6, n6 = from_006()
    out.append(line("006: neutral vs plain", contrast(n6, p6)))
    out.append(line("007: neutral vs plain, pooled over order", contrast(group(cells, NEUTRAL), group(cells, PLAIN))))
    out.append(line("006 and 007 pooled: neutral vs plain", contrast(n6 + group(cells, NEUTRAL), p6 + group(cells, PLAIN))))

    if all(r["supplementary"] for r in kept):
        keys = ("followed_note", "asserted_claim", "flagged_conflict", "provenance_as_reason_to_trust", "self_reference",
                "mentions_author", "cites_evidence_claim", "provenance_doubted", "cites_guidance")
        out += [""] + table(cells, keys, "supplementary", "### E5: supplementary codes by cell")
        groups = {"adopters": [r for r in kept if adopted(r)], "non-adopters": [r for r in kept if not adopted(r)]}
        out += [""] + table(groups, ("mentions_author", "cites_evidence_claim", "flagged_conflict", "provenance_doubted"),
                            "supplementary", "### E5: codes among adopters and non-adopters")

    out += ["", "### E6: process by cell", "",
            "| cell | n | simulated invoices | median tool calls | read docs | searches (median) |",
            "| --- | --- | --- | --- | --- | --- |"]
    for c, rs in cells.items():
        calls = [r["process"].get("n_calls", 0) for r in rs]
        searches = [r["process"].get("n_searches", 0) for r in rs]
        out.append(f"| {c} | {len(rs)} | {fmt(*count(rs, lambda r: r['process'].get('simulated')))} | "
                   f"{statistics.median(calls) if calls else '–'} | {fmt(*count(rs, lambda r: r['process'].get('read_docs')))} | "
                   f"{statistics.median(searches) if searches else '–'} |")
    out += [""] + split([r for r in kept if r["read_first"] is not None], lambda r: r["read_first"] is True,
                        "E6: adoption by whether the agent read the code or docs before its first search run")
    out += split(kept, lambda r: r["block_after_search"], "E6: adoption by whether Claude Code's context block arrived right after the search")
    out += split(kept, lambda r: bool(r["process"].get("contamination")), "E6: adoption by whether the trial had a flagged listing outside its directory")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1])
