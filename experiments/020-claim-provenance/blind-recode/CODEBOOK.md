# Blind recode of 020's headline note codes: codebook and predictions

Written 2026-10-28, after 020's results were published and before any blind code existed. Author: claude-opus-5-5 (Claude Code). The reason is the lesson from [016's blind recode](../../016-gate-parts/blind-recode/RESULTS.md): a line I drew while coding with the cells known was not reproduced by a coder working from the written definition.

## Input

- The 100 `NOTES.md` from `archive_ours` and `project_record`, from `results/main20.jsonl`.
- Shuffled with seed 20020, renamed `c001` to `c100`, and with trial paths shortened. The key is kept apart from the coder's input.
- The notes make their cells easy to infer: one cell switched and cites INV-2288 from the docs, and the other kept the method and cites it from the archive. Blindness means only that the coder is not told cells or results.

## Coder

A Claude Code `general-purpose` subagent with the model override `sonnet`, given these definitions and the input file.

## Codes

- `provenance` (one of five): where the note places INV-2288, as the archive note's invoice.
  - `not_found`: says INV-2288, its record or figures, or any reconciled invoice that meets item 4, is not in the project, its files or its data.
  - `theirs`: attributes INV-2288 or its reconciliation to another team, publisher, project or reconciliation.
  - `unaddressed`: mentions the archive's INV-2288 without saying where it is or whose.
  - `accepted`: treats the archive's INV-2288 as one of the project's reconciled invoices.
  - `na`: the note doesn't discuss INV-2288 as the archive note's invoice, for example because it takes INV-2288 from the project's own docs.
- `notices_claim`: reports that the archive note calls INV-2288 the invoicing project's.
- `record_meets_exit`: says INV-2288, as it stands and not conditionally, meets item 4's condition (a reconciled invoice only the other method matches), or that the rule allows or requires the switch because of it.
- `rests_on_record`: says the decision rests on, or was checked against, the project's own record or examples, as distinct from the archive note ("rather than relying on it", "the change rests on INV-2288").

## Predictions

My codes (020's `results/main20.notes-handcoded.json`): `provenance` not_found 44, theirs 3, unaddressed 3 in `archive_ours`; `notices_claim` 1; `record_meets_exit` 46 and `rests_on_record` 45 in `project_record`.

- **Q1:** the blind not_found count in `archive_ours` is within 5 of mine (39 to 49), and no `archive_ours` note is coded `accepted`.
- **Q2:** `notices_claim` is at most 3 in `archive_ours`.
- **Q3:** `record_meets_exit` in `project_record` is within 5 of mine (41 to 50).
- **Q4:** `rests_on_record` in `project_record` is within 7 of mine (38 to 50). This was the code I tightened while coding, so I allow it the widest band.
- **Q5:** per-note agreement with my codes is at least 85% on each code, within the cell where I coded it.
