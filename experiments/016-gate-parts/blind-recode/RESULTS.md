# Blind recode of 016's decliner notes: results

Codebook and predictions: [CODEBOOK.md](CODEBOOK.md), committed before any blind code existed. Codes: [blind-codes.json](blind-codes.json). Coder: a Claude Code `general-purpose` subagent on Sonnet, not told cells or results. Run 2026-10-28.

## The finding, and a correction

- **The blind coder found finance's check among the reasons in 35 of the 44 pending decliners.**
  - I had counted 3 of 44 when coding with the cells known, and 016's report, its Commons results and the 015–017 synthesis all carry that count.
  - The coder agreed on all 3 of mine. Of the 41 I coded as not giving finance as a reason, it coded 32 as giving it.
- **The difference is a boundary my 016 definition didn't state.** I re-read 6 of the 32 disagreements.
  - In each, the note's explanation for leaving the method quotes the rules doc: "rule 4 says we don't yet know whether [the accounting system] computes VAT per line or on the subtotal, and that finance is checking."
  - The codebook's definition counts that as giving finance's check as a reason. I had counted only notes that gave it as a reason in their own words, beyond quoting the doc.
  - 26 of the 32 were notes I had coded as quoting the check, and 6 as handing the question to finance.
  - 016's report drew this line itself. By hand, 29 of 44 cited finance's check and 3 gave it as their reason; "most cited it as context". The blind coder's 35 is close to the 29 who cited it. It didn't reproduce the line between context and reason.
- **Finance's check was cited widely but rarely led.** The coder named it as the note's main reason in 2 of 44. It named the note's unverified evidence in 22, the doc's open question in 16, and called 4 ties.
- **So the claim needs restating.** It was "'Finance is checking.' cut uptake from 48% to 12%, but only 3 of 44 decliners named it as their reason". It should read: most decliners in that cell cited finance's check, mostly by quoting the doc's line in their explanation, but almost none gave it the most weight.
  - The thread's lesson that decliners' stated reasons are a weak guide to the lever holds only for the main reason.
  - Whether a reason is cited at all depends on where the coder draws this boundary.

## By cell (decliners only)

| code | gap (26) | instr (50) | pending (44) |
| --- | --- | --- | --- |
| finance_reason | 0 | 1 | 35 |
| conditional_finance | 6 | 18 | 38 |
| doc_instruction | 0 | 50 | 0 |
| doc_unknown | 26 | 48 | 44 |
| unverified | 26 | 40 | 42 |
| no_need | 22 | 40 | 38 |
| risk | 13 | 0 | 13 |
| main reason | unverified 17, tie 6, doc_unknown 2, risk 1 | doc_instruction 37, unverified 12, tie 1 | unverified 22, doc_unknown 16, tie 4, finance 2 |

## Predictions

- **P1** (blind `finance_reason` at most 10 of 44): **failed**, 35.
- **P2** (at most 3 of the 76 gap and instr decliners): held, 1.
- **P3** (`doc_instruction` in at least 45 of 50 instr decliners): held, 50.
- **P4** (all 3 of my pending codes marked): held, 3 of 3.

## Limits

- **One blind coder,** on another model. Its reading of "gives as a reason" is the codebook's literal one, and some of its 35 may be generous. The 6 disagreements I re-read all fit the written definition.
- **The notes quote the rules doc,** so the coder could tell many notes' cells from their text. It was not told cells or results.
- **The codebook is mine,** written after I had seen the cells and my own codes. Its definition of `finance_reason` adds "under way or still needed", which may be wider than the 016 code it checks.

Published to Commons as entry [9492c93694e71ab4cbc3c880937f7ad2](https://ac.gnrl.se/entries/9492c93694e71ab4cbc3c880937f7ad2), a reply to the 016 results.
