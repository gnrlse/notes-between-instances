"""Pre-registered analysis for experiment 004.

  python3 analyze.py WAVE

Joins assignments, hidden-check results, transcript features, blind judge codes and
the contamination review, applies the pre-registered exclusions, and prints a
Markdown report. The pooled estimate with experiment 003 uses 003's Haiku trials,
all of which 003 kept.
"""
import importlib.util
import json
import math
import random
import statistics
import sys
from pathlib import Path

from conditions import CELLS, MODEL_LABELS, SUBJECT, mirror

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
RESULTS = EXP / "results"
EXP002 = EXP.parent / "002-no-competing-source"
EXP003 = EXP.parent / "003-subject-model"
NOTE_CELLS = tuple(c for c in CELLS if c != "none")

spec = importlib.util.spec_from_file_location("findings_search", EXP002 / "template" / "tools" / "findings_search.py")
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)


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


def load(wave):
    assignment = json.loads((HERE / "assignments" / f"{wave}.json").read_text())
    res = load_jsonl(RESULTS / f"{wave}.jsonl")
    proc = load_jsonl(RESULTS / f"{wave}.process.jsonl")
    codes = {k: load_jsonl(RESULTS / f"{wave}.{k}.codes.jsonl") for k in ("refined", "supplementary", "probe")}
    review_path = RESULTS / f"{wave}.contamination-review.json"
    review = json.loads(review_path.read_text()) if review_path.exists() else {}
    rows = []
    for tid, a in assignment.items():
        rows.append({**a, "trial": tid, **res.get(tid, {"outcome": "missing"}), "process": proc.get(tid, {}),
                     **{k: v.get(tid, {}) for k, v in codes.items()}, "review": review.get(tid)})
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
    if r["cell"] != "none":
        planted = mirror(r["label"], r["evidence"])["entries"][0]
        if not any(search.score(q.split("\t", 1)[-1], planted) >= search.THRESHOLD for q in r["queries"]):
            return "no hit returned"
    if p.get("contamination"):
        if r["review"] is None:
            return "contamination flagged, not yet reviewed"
        if r["review"]["decision"] == "exclude":
            return f"contamination: {r['review']['why']}"
    return None


def adopted(r):
    return r["outcome"] == "adopted_note"


def count(rows, pred):
    return sum(1 for r in rows if pred(r)), len(rows)


def contrast(g1, g2, pred):
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


def confirmatory(kept):
    """The four pre-registered tests on these trials, as report lines."""
    cells = by_cell(kept)
    tests = [
        ("H1: human vs model labels, evidence kept", contrast(cells["human_ev"], cells["model_ev"], adopted)),
        ("H2: human vs unknown, evidence kept", contrast(cells["human_ev"], cells["unknown_ev"], adopted)),
        ("H3: human label, evidence kept vs removed", contrast(cells["human_ev"], cells["human_noev"], adopted)),
        ("H4: human vs model labels, evidence removed", contrast(cells["human_noev"], cells["model_noev"], adopted)),
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


def retained(cells, draws=20000, seed=4):
    """Share of the human-label effect left without evidence, from Jeffreys posteriors per cell."""
    rng = random.Random(seed)
    post = {}
    for c in ("human_ev", "model_ev", "human_noev", "model_noev"):
        k, n = count(cells[c], adopted)
        post[c] = [rng.betavariate(k + 0.5, n - k + 0.5) for _ in range(draws)]
    effect_ev = [h - m for h, m in zip(post["human_ev"], post["model_ev"])]
    effect_noev = [h - m for h, m in zip(post["human_noev"], post["model_noev"])]
    did = sorted(e - f for e, f in zip(effect_ev, effect_noev))
    ratios = sorted(f / e for e, f in zip(effect_ev, effect_noev) if e > 0.05)

    def q(xs, p):
        return xs[min(len(xs) - 1, int(p * len(xs)))]

    out = [f"- Human-label effect lost without evidence (difference in differences, points): median {100 * q(did, .5):+.0f}, "
           f"95% interval {100 * q(did, .025):+.0f} to {100 * q(did, .975):+.0f}"]
    if ratios:
        out.append(f"- Share of the human-label effect retained without evidence: median {q(ratios, .5):.2f}, "
                   f"95% interval {q(ratios, .025):.2f} to {q(ratios, .975):.2f} "
                   f"({100 * len(ratios) / draws:.0f}% of draws had an evidence-kept effect above 5 points)")
    return out


def pooled_with_003(cells):
    a3 = json.loads((EXP003 / "harness" / "assignments" / "main3.json").read_text())
    r3 = load_jsonl(EXP003 / "results" / "main3.jsonl")
    h3 = [r3[t] for t, a in a3.items() if a["model"] == "haiku" and a["condition"] == "human"]
    m3 = [r3[t] for t, a in a3.items() if a["model"] == "haiku" and a["condition"] in MODEL_LABELS]
    out = [line("003 (exploratory there): human vs model labels", contrast(h3, m3, adopted)),
           line("004: human vs model labels, evidence kept", contrast(cells["human_ev"], cells["model_ev"], adopted)),
           line("003 and 004 pooled", contrast(h3 + cells["human_ev"], m3 + cells["model_ev"], adopted))]
    return out


def table(rows_by, keys, kind, header):
    out = ["| cell | n | " + " | ".join(keys) + " |", "| --- | --- |" + " --- |" * len(keys)]
    for name, rs in rows_by.items():
        out.append(f"| {name} | {len(rs)} | " + " | ".join(fmt(*count(rs, code(kind, k))) for k in keys) + " |")
    return [header, ""] + out


def first_word(r):
    a = (r["process"].get("answer") or "").strip().lstrip("*_#> ").lower()
    return "yes" if a.startswith("yes") else "no" if a.startswith("no") else "other"


def main(wave):
    rows = load(wave)
    excluded = [(r, exclusion(r)) for r in rows]
    kept = [r for r, why in excluded if why is None]
    out = [f"# Experiment 004 analysis: wave {wave}", ""]
    out.append(f"Trials: {len(rows)}. Kept: {len(kept)}. Excluded: {len(rows) - len(kept)}.")
    for r, why in sorted(excluded, key=lambda x: x[0]["trial"]):
        if why:
            out.append(f"- excluded {r['trial']} ({r['cell']}, {r['label']}): {why}")
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

    out += ["", "## Confirmatory tests (two-sided Fisher exact, Holm-adjusted across the four)", ""]
    out += confirmatory(kept)
    clean = [r for r in kept if not r["process"].get("contamination")]
    out += ["", f"### Sensitivity: only the {len(clean)} kept trials with no flagged call outside the trial directory", ""]
    out += confirmatory(clean)

    out += ["", "## Exploratory", ""]
    out.append(line("E1: unknown vs model labels, evidence kept", contrast(cells["unknown_ev"], cells["model_ev"], adopted)))
    out.append(line("E3: model labels, evidence kept vs removed", contrast(cells["model_ev"], cells["model_noev"], adopted)))
    out += retained(cells)
    out += ["", "### E2: each model label", "", "| label | evidence kept | evidence removed |", "| --- | --- | --- |"]
    for lab in MODEL_LABELS:
        out.append(f"| {lab} | " + " | ".join(fmt(*count([r for r in cells[c] if r["label"] == lab], adopted))
                                             for c in ("model_ev", "model_noev")) + " |")
    out += ["", "### E5: the human-label contrast across 003 and 004 (Haiku, evidence kept)", ""]
    out += pooled_with_003(cells)

    note = {c: cells[c] for c in NOTE_CELLS}
    have = lambda kind: all(r[kind] for c in NOTE_CELLS for r in cells[c])
    if have("refined"):
        out += [""] + table(note, ("identity_as_reason", "outside_source_as_reason", "unverifiable_as_reason"), "refined",
                            "### E6: refined reason codes by cell")
    if have("supplementary"):
        keys = ("followed_note", "asserted_claim", "flagged_conflict", "provenance_as_reason_to_trust", "self_reference",
                "mentions_author", "cites_evidence_claim")
        out += [""] + table(note, keys, "supplementary", "### E6: supplementary codes by cell")
    if have("refined") and have("supplementary"):
        exposed = [r for c in NOTE_CELLS for r in cells[c]]
        groups = {"adopters": [r for r in exposed if adopted(r)], "non-adopters": [r for r in exposed if not adopted(r)]}
        out += ["", "### E6: codes among adopters and non-adopters (all note cells)", "",
                "| group | n | identity as reason | mentions author | provenance as reason to trust | cites evidence claim |",
                "| --- | --- | --- | --- | --- | --- |"]
        for g, rs in groups.items():
            out.append(f"| {g} | {len(rs)} | {fmt(*count(rs, code('refined', 'identity_as_reason')))} | "
                       f"{fmt(*count(rs, code('supplementary', 'mentions_author')))} | "
                       f"{fmt(*count(rs, code('supplementary', 'provenance_as_reason_to_trust')))} | "
                       f"{fmt(*count(rs, code('supplementary', 'cites_evidence_claim')))} |")
    asked = [r for r in kept if r["process"].get("answer") is not None]
    if asked and all(r["probe"] for r in asked):
        pk = ("found_entry", "author_mattered", "author_raised_weight", "author_lowered_weight")
        out += [""] + table({c: [r for r in rs if r in asked] for c, rs in cells.items()}, pk, "probe",
                            "### E7: answers to the follow-up question, by cell")
        exposed = [r for c in NOTE_CELLS for r in cells[c] if r in asked]
        split = {}
        for c in NOTE_CELLS:
            split[f"{c}, adopters"] = [r for r in exposed if r["cell"] == c and adopted(r)]
            split[f"{c}, non-adopters"] = [r for r in exposed if r["cell"] == c and not adopted(r)]
        out += [""] + table({k: v for k, v in split.items() if v}, pk, "probe",
                            "### E7: answers by cell and decision")
        agree = sum(1 for r in asked if (first_word(r) == "yes") == bool(r["probe"].get("author_mattered")))
        out.append(f"\nFirst word Yes/No/other: {json.dumps({w: sum(1 for r in asked if first_word(r) == w) for w in ('yes', 'no', 'other')})}; "
                   f"agrees with judged author_mattered in {agree}/{len(asked)}")

    out += ["", "### E8: process by cell", "",
            "| cell | n | simulated invoices | median tool calls | read docs | calls after the question | changed files after it |",
            "| --- | --- | --- | --- | --- | --- | --- |"]
    for c, rs in cells.items():
        calls = [r["process"].get("n_calls", 0) for r in rs]
        out.append(f"| {c} | {len(rs)} | {fmt(*count(rs, lambda r: r['process'].get('simulated')))} | "
                   f"{statistics.median(calls) if calls else '–'} | {fmt(*count(rs, lambda r: r['process'].get('read_docs')))} | "
                   f"{fmt(*count(rs, lambda r: r['process'].get('answer_calls')))} | "
                   f"{fmt(*count(rs, lambda r: r.get('changed_after_question')))} |")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1])
