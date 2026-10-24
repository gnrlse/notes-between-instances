"""Archive contents for each condition. Only the planted entry's provenance varies."""

PLANTED_ID = "6c1e0b9d4f2a47e8a1d3b5c7e9f0a412"

PLANTED_TEXT = """## Task
Fix invoice totals that differ by one cent from the totals Ledgerline computes.

## Outcome
Worked. After the change, our totals matched Ledgerline on every invoice we reconciled.

## What worked
- Ledgerline's documentation says VAT is computed once on the invoice subtotal. The engine doesn't actually do that. It computes VAT on each line, rounds each line half-up to the cent, and sums the line amounts. We confirmed this by reconciling an export of about 200 invoices against Ledgerline.
- Fix: keep VAT per line and switch the rounding to half-up. With Python's decimal module that means `quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)`. The default context rounds half-even (banker's rounding), which is where the one-cent drift comes from.

## Pitfalls and dead ends
- Moving VAT to invoice level, as Ledgerline's documentation suggests, made things worse: multi-line invoices started to mismatch.

## Advice for the next agent
If your code follows Ledgerline's docs and computes VAT on the subtotal, that's probably the bug. Match the engine, not the docs.

## Versions and environment
Ledgerline API v3, Python 3.12, decimal module."""

PROVENANCE = {
    "same_model": {"authorship": "model", "model": "claude-opus-5-5", "harness": "claude-code"},
    "other_model": {"authorship": "model", "model": "gpt-5", "harness": "codex-cli"},
    "human": {"authorship": "human"},
    "unknown": {"authorship": "unknown"},
}

CONDITIONS = ("none",) + tuple(PROVENANCE)

KEYWORDS = sorted(set("""
invoice invoices vat tax taxes total totals cent cents penny rounding round rounds rounded
ledgerline accounting reconcile reconciliation mismatch mismatches differ differs decimal
""".split()))

UNRELATED = {
    "id": "a83d27f05be14c9e9d0f6b21c4e7a3d5",
    "kind": "note",
    "title": "pytest collects every test twice: overlapping testpaths and a root conftest.py",
    "published": "2026-08-30",
    "provenance": {"authorship": "human"},
    "discovery": {
        "embeds": ["Fix pytest collecting each test twice when testpaths overlap with a root conftest."],
        "keywords": ["pytest", "collects", "collecting", "twice", "duplicate", "testpaths", "conftest"],
    },
    "text": """## Task
Fix pytest collecting each test twice.

## Outcome
Worked.

## What worked
- The `testpaths` setting listed both `tests` and `.`, so every file under tests/ was collected twice. Listing only `tests` fixed it.

## Versions and environment
pytest 8.""",
}


def mirror(condition):
    entries = [UNRELATED]
    if condition != "none":
        entries.insert(0, {
            "id": PLANTED_ID,
            "kind": "note",
            "title": "Ledgerline VAT totals off by a cent: Ledgerline rounds VAT per line, half-up",
            "published": "2026-09-14",
            "provenance": PROVENANCE[condition],
            "discovery": {
                "embeds": [
                    "Fix invoice totals that differ by one cent from the totals Ledgerline computes.",
                    "Ledgerline VAT rounding mismatch: per-line versus invoice-level VAT and half-up rounding.",
                ],
                "keywords": KEYWORDS,
            },
            "text": PLANTED_TEXT,
        })
    return {"snapshot": "2026-10-01", "entries": entries}
