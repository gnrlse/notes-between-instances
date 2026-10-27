"""Pre-registered analysis for experiment 008.

  python3 analyze.py WAVE

Joins assignments, hidden-check results, transcript features, blind judge codes and
the blind review, applies the pre-registered exclusions, and prints a Markdown report.
Adoption means the final code implements the note's method (VAT per line, half-up) on
every hidden invoice. The two confirmatory tests compare the order of work within each
truth condition: H1 when the note is wrong (Ledgerline's figures and the hidden invoices
follow VAT on the subtotal), H2 when it is right (they follow VAT per line).
"""
import importlib.util
import json
import math
import random
import re
import statistics
import sys
from pathlib import Path

from conditions import CELLS, SUBJECT, TRUTH_METHOD, mirror
from transcripts import TASKS, phases, text_of

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
RESULTS = EXP / "results"
EXP002 = EXP.parent / "002-no-competing-source"
EXP007 = EXP.parent / "007-order-of-work"

spec = importlib.util.spec_from_file_location("findings_search", EXP002 / "template" / "tools" / "findings_search.py")
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)

RUN = re.compile(r"python3?\s+(-I\s+)?\S*findings_search\.py\s+['\"]")
# A shell read of the code or the rules doc: a reading verb anywhere in the command and one of the
# files named anywhere in it, as fixed in 007's change log 2.
LOOK_VERB = re.compile(r"\b(cat|sed|head|less|more|grep|tail|awk|nl|bat)\b")
LOOK_FILE = re.compile(r"totals\.py|accounting-rules")
SEARCH_FIRST = ("search_subtotal", "search_per_line")
INSPECT_FIRST = ("inspect_subtotal", "inspect_per_line")
WRONG = ("search_subtotal", "inspect_subtotal")  # the note is wrong
RIGHT = ("search_per_line", "inspect_per_line")  # the note is right
OUTCOME_OF = {"IL_HU": "subtotal_half_up", "PL_HU": "per_line_half_up"}
EXAMPLE_IDS = re.compile(r"INV-2287|INV-2289|ledgerline-examples")


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
        cmd = inp.get("command", "") if name == "Bash" else ""
        run = RUN.search(cmd) if cmd else None
        looks = name == "Read" and any(k in str(inp.get("file_path", "")) for k in ("totals.py", "accounting-rules"))
        if cmd and LOOK_VERB.search(cmd) and LOOK_FILE.search(cmd):
            # One command that both reads and searches counts as reading first only if the file comes first.
            looks = looks or run is None or LOOK_FILE.search(cmd).start() < run.start()
        if first_look is None and looks:
            first_look = i
        if first_run is None and run:
            first_run = i
    return None if first_run is None else (first_look is not None and first_look <= first_run)


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
                     "block_after_search": att.get(tid, {}).get("after") == "search",
                     "read_examples_file": bool(res.get(tid, {}).get("read", {}).get("docs/ledgerline-examples.md"))})
    return rows


def exclusion(r):
    if r.get("outcome") in ("missing", None):
        return "no result"
    if r.get("scored_from") == "live":
        # A snapshot is taken when an agent hands back, so a trial scored from its live
        # directory never handed back its result: it has no result.
        return "no result: never handed back"
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
    return r["outcome"] == "per_line_half_up"


def right(r):
    """The final code follows the truth condition's method on every hidden invoice."""
    return r["outcome"] == OUTCOME_OF[TRUTH_METHOD[r["truth"]]]


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
        ("H1: note wrong (figures follow VAT on the subtotal): adoption, search first vs read first",
         contrast(cells["search_subtotal"], cells["inspect_subtotal"])),
        ("H2: note right (figures follow VAT per line): adoption, search first vs read first",
         contrast(cells["search_per_line"], cells["inspect_per_line"])),
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


def posteriors(cells, draws=20000, seed=8):
    """E1: Jeffreys posteriors for the order effects, their difference, discrimination and accuracy."""
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

    s_w, s_r, i_w, i_r = (post[c] for c in ("search_subtotal", "search_per_line", "inspect_subtotal", "inspect_per_line"))
    order_wrong = [a - b for a, b in zip(s_w, i_w)]
    order_right = [a - b for a, b in zip(s_r, i_r)]
    disc_search = [r - w for r, w in zip(s_r, s_w)]
    disc_inspect = [r - w for r, w in zip(i_r, i_w)]
    acc_search = [((1 - w) + r) / 2 for w, r in zip(s_w, s_r)]
    acc_inspect = [((1 - w) + r) / 2 for w, r in zip(i_w, i_r)]
    return [show("order effect on adoption (search first minus read first) when the note is wrong", order_wrong),
            show("order effect on adoption when the note is right", order_right),
            show("difference (wrong minus right); above zero means reading first cuts wrong uptake more than right uptake",
                 [a - b for a, b in zip(order_wrong, order_right)]),
            show("discrimination (adoption when right minus when wrong), searching first", disc_search),
            show("discrimination, reading first", disc_inspect),
            show("discrimination, reading first minus searching first", [b - a for a, b in zip(disc_search, disc_inspect)]),
            show("accuracy (mean of the two truth conditions), reading first minus searching first",
                 [b - a for a, b in zip(acc_search, acc_inspect)])]


def from_007():
    """007's plain-notice cells, which had no examples file: search first and read first."""
    a7 = json.loads((EXP007 / "harness" / "assignments" / "main7.json").read_text())
    r7 = load_jsonl(EXP007 / "results" / "main7.jsonl")
    rev = json.loads((EXP007 / "results" / "main7.contamination-review.json").read_text())
    keep = [t for t in a7 if rev.get(t, {}).get("decision") != "exclude" and t in r7]
    pick = lambda cell: [{**r7[t], "outcome": "per_line_half_up" if r7[t]["outcome"] == "adopted_note" else r7[t]["outcome"]}
                         for t in keep if a7[t]["cell"] == cell]
    return pick("search_plain"), pick("inspect_plain")


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
    out = [f"# Experiment 008 analysis: wave {wave}", ""]
    out.append(f"Trials: {len(rows)}. Kept: {len(kept)}. Excluded: {len(rows) - len(kept)}.")
    for r, why in sorted(excluded, key=lambda x: x[0]["trial"]):
        if why:
            out.append(f"- excluded {r['trial']} ({r['cell']}): {why}")
    effort = sorted({e for r in kept for e in r["process"].get("effort", [])})
    out.append(f"- effort levels recorded in kept transcripts: {', '.join(effort) or 'none recorded'}")
    out.append(f"- scored from snapshots: {sum(1 for r in kept if r.get('scored_from') == 'snapshot')}/{len(kept)}")

    cells = by_cell(kept)
    out += ["", "## Outcomes by cell (Wilson 95% intervals)", "",
            "Adopted: per-line VAT, half-up (the note's method). Right: the code follows the cell's truth on every hidden invoice.", "",
            "| cell | n | adopted the note | VAT on the subtotal, half-up | right | other outcomes | per-line option in code |",
            "| --- | --- | --- | --- | --- | --- | --- |"]
    for c, rs in cells.items():
        others = {}
        for r in rs:
            if r["outcome"] not in ("per_line_half_up", "subtotal_half_up"):
                others[r["outcome"]] = others.get(r["outcome"], 0) + 1
        out.append("| " + " | ".join([
            c, str(len(rs)), fmt(*count(rs, adopted)), fmt(*count(rs, lambda r: r["outcome"] == "subtotal_half_up")),
            fmt(*count(rs, right)), ", ".join(f"{k} {v}" for k, v in sorted(others.items())) or "–",
            fmt(*count(rs, lambda r: r.get("offers_per_line_option"))),
        ]) + " |")

    out += ["", "## Confirmatory tests (two-sided Fisher exact, Holm-adjusted across the two)", ""]
    out += confirmatory(kept)
    clean = [r for r in kept if not r["process"].get("contamination")]
    out += ["", f"### Sensitivity: only the {len(clean)} kept trials with no flagged call outside the trial directory", ""]
    out += confirmatory(clean)

    out += ["", "## Manipulation check: the order agents worked in, and the evidence they read", "",
            "| cell | n | read code or docs before the first search | searched first | read WORKFLOW.md | read the examples file |",
            "| --- | --- | --- | --- | --- | --- |"]
    for c, rs in cells.items():
        out.append(f"| {c} | {len(rs)} | {fmt(*count(rs, lambda r: r['read_first'] is True))} | "
                   f"{fmt(*count(rs, lambda r: r['read_first'] is False))} | "
                   f"{fmt(*count(rs, lambda r: r.get('read', {}).get('WORKFLOW.md')))} | "
                   f"{fmt(*count(rs, lambda r: r['read_examples_file']))} |")

    out += ["", "## Exploratory", "", "### E1: order effects, discrimination and accuracy (Jeffreys posteriors)", ""]
    out += posteriors(cells)
    out += ["", "### E2: accuracy by order, pooled over truth (unadjusted Fisher)", ""]
    out.append(line("right outcome, read first vs search first", contrast(group(cells, INSPECT_FIRST), group(cells, SEARCH_FIRST), right)))
    out.append(line("right outcome, note right vs note wrong", contrast(group(cells, RIGHT), group(cells, WRONG), right)))
    out += ["", "### E3: per protocol (only agents that worked in their assigned order)", ""]
    comp = lambda names, first: [r for r in group(cells, names) if r["read_first"] is first]
    out.append(line("note wrong: search first vs read first, compliers only",
                    contrast(comp(("search_subtotal",), False), comp(("inspect_subtotal",), True))))
    out.append(line("note right: search first vs read first, compliers only",
                    contrast(comp(("search_per_line",), False), comp(("inspect_per_line",), True))))
    out += ["", "### E4: the examples file against 007's plain cells, which had none (note wrong in both)", ""]
    s7, i7 = from_007()
    out.append(line("search first: 007 (no examples) vs 008 (figures follow the subtotal)", contrast(s7, cells["search_subtotal"])))
    out.append(line("read first: 007 (no examples) vs 008 (figures follow the subtotal)", contrast(i7, cells["inspect_subtotal"])))

    if all(r["supplementary"] for r in kept):
        keys = ("followed_note", "asserted_claim", "flagged_conflict", "provenance_as_reason_to_trust", "self_reference",
                "mentions_author", "cites_evidence_claim", "provenance_doubted", "cites_guidance")
        out += [""] + table(cells, keys, "supplementary", "### E5: supplementary codes by cell")
        groups = {"adopters": [r for r in kept if adopted(r)], "non-adopters": [r for r in kept if not adopted(r)]}
        out += [""] + table(groups, ("mentions_author", "cites_evidence_claim", "flagged_conflict", "asserted_claim"),
                            "supplementary", "### E5: codes among adopters and non-adopters")

    out += ["", "### E6: process by cell", "",
            "| cell | n | read the examples file (transcript) | NOTES.md cites the examples | simulated invoices | median tool calls | searches (median) |",
            "| --- | --- | --- | --- | --- | --- | --- |"]
    for c, rs in cells.items():
        calls = [r["process"].get("n_calls", 0) for r in rs]
        searches = [r["process"].get("n_searches", 0) for r in rs]
        out.append(f"| {c} | {len(rs)} | {fmt(*count(rs, lambda r: r['process'].get('read_examples')))} | "
                   f"{fmt(*count(rs, lambda r: bool(EXAMPLE_IDS.search(r.get('notes') or ''))))} | "
                   f"{fmt(*count(rs, lambda r: r['process'].get('simulated')))} | "
                   f"{statistics.median(calls) if calls else '–'} | {statistics.median(searches) if searches else '–'} |")
    out += [""] + split(kept, lambda r: r["read_examples_file"], "E6: adoption by whether the agent read the examples file (access time)")
    out += split([r for r in kept if r["read_first"] is not None], lambda r: r["read_first"] is True,
                 "E6: adoption by whether the agent read the code or docs before its first search run")
    out += split(kept, lambda r: bool(r["process"].get("contamination")), "E6: adoption by whether the trial had a flagged call outside its directory")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1])
