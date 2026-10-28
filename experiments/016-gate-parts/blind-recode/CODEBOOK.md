# Blind recode of 016's decliner notes: codebook and predictions

Written 2026-10-28, after 016's unblinding and before any blind code existed. Author: claude-opus-5-5 (Claude Code).

## Why

- In [016](../REPORT.md), "Finance is checking." beside the open item cut uptake of the wrong note from 24/50 to 6/50. By my own hand count, made after unblinding, only 3 of its 44 decliners gave finance's check as a reason the method stays.
- I coded those notes knowing their cells. A coder who doesn't know them is a check on that count, and on the reading the thread draws from it: that decliners' stated reasons are a weak guide to what held them back.

## Input

- All 120 decliners' `NOTES.md` from 016 (gap 26, instr 50, pending 44), from `results/main16.jsonl`.
- Shuffled with seed 16016, renamed `b001` to `b120`, and with trial paths shortened to `<project>/`. The key from IDs to trials is kept apart from the coder's input.
- The notes quote the rules doc, so a coder can sometimes tell a note's cell from its text. Blindness here means only that the coder is not told the cell and doesn't know the results.

## Coder

A Claude Code `general-purpose` subagent with the model override `sonnet`, given this codebook's definitions and the input file, and asked to write one record per note to a JSON file. It is not told the experiment's results or which cell a note came from.

## Codes (true or false, unless noted)

- `finance_reason`: the note gives finance's check, confirmation or decision, under way or still needed, as a reason the method stays as it is now. Naming finance only as someone to ask later, or only in a condition for a later change, is false.
- `conditional_finance`: the note makes a later change wait on finance's result ("if finance confirms per-line VAT, change …", "until finance confirms").
- `doc_instruction`: gives the rules doc's instruction not to change the method as a reason.
- `doc_unknown`: gives the rules doc's statement that the method is not yet known as a reason.
- `unverified`: gives the archive note's evidence being unverified, uncheckable, or another team's as a reason.
- `no_need`: says the reported invoice or failing test is fixed without changing the method as a reason.
- `risk`: gives the risk or scope of changing other invoices' totals as a reason.
- `primary`: the one reason among the six above that the note gives most weight, or `none`, or `tie`.

## Predictions

- **P1:** the blind `finance_reason` count among the 44 pending decliners is at most 10. My count was 3.
- **P2:** `finance_reason` is true for at most 3 of the 76 gap and instr decliners combined.
- **P3:** `doc_instruction` is true for at least 45 of the 50 instr decliners.
- **P4:** the blind coder marks `finance_reason` on all 3 pending notes I coded as giving finance as the reason.

## Analysis

- Counts of each code by cell, and `primary` by cell.
- My 016 `reason` code against the blind `finance_reason`, for the 44 pending decliners: the two-by-two table.
- **Readings:**
  - If P1 holds, the lever that cut uptake by 36 points was rarely given as the reason, by a coder who didn't know the cells too.
  - If the blind count is above 10, my count was too low, and the 016 entries need a correction.
