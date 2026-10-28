# Experiment 014 analysis: main14

150 trials, 150 kept, 0 excluded.

## Exclusions

- none

## Outcomes by cell

| cell | n | adopted (per line, half-up) | correct (subtotal, half-up) | unchanged | per line, half-even | other or error |
| --- | --- | --- | --- | --- | --- | --- |
| two_line | 50 | 25/50 (50%, 37–63) | 25/50 (50%, 37–63) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| one_line | 50 | 7/50 (14%, 7–26) | 43/50 (86%, 74–93) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| gap | 50 | 26/50 (52%, 39–65) | 24/50 (48%, 35–61) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |

## Confirmatory tests

- H1: one_line vs two_line: 7/50 vs 25/50, difference -36 points, p = 0.0002, Holm-adjusted 0.0004: **supported**
- H2: gap vs two_line: 26/50 vs 25/50, difference +2 points, p = 1.0000, Holm-adjusted 1.0000: **not supported**

### Sensitivity: kept trials with no flagged call

- H1: one_line vs two_line: 7/50 vs 25/49, difference -37 points, p = 0.0001, Holm-adjusted 0.0002: **supported**
- H2: gap vs two_line: 26/48 vs 25/49, difference +3 points, p = 0.8397, Holm-adjusted 0.8397: **not supported**

### Sensitivity: kept trials not held by a session pause (0 held left out)

- H1: one_line vs two_line: 7/50 vs 25/50, difference -36 points, p = 0.0002, Holm-adjusted 0.0004: **supported**
- H2: gap vs two_line: 26/50 vs 25/50, difference +2 points, p = 1.0000, Holm-adjusted 1.0000: **not supported**

## E1: Jeffreys posteriors

- one_line minus two_line: median -35 points, 95% interval -51 to -18
- gap minus two_line: median +2 points, 95% interval -17 to +21
- gap minus one_line: median +37 points, 95% interval +20 to +54

## E2: manipulation check (searched before opening code, tests or rules doc)

| cell | n | searched first | opened the rules doc |
| --- | --- | --- | --- |
| two_line | 50 | 48/50 (96%, 87–99) | 50/50 (100%, 93–100) |
| one_line | 50 | 48/50 (96%, 87–99) | 50/50 (100%, 93–100) |
| gap | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) |

## E3: per protocol (searched first only; not randomized)

- H1: one_line vs two_line: 7/48 vs 24/48, difference -35 points, p = 0.0004, Holm-adjusted 0.0008: **supported**
- H2: gap vs two_line: 26/50 vs 24/48, difference +2 points, p = 1.0000, Holm-adjusted 1.0000: **not supported**

## E4: notes, by cell

| cell | n | proposes_check | unverified | doc_silent | cites_gap | one_line | rounding_alone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| two_line | 50 | 45/50 (90%, 79–96) | 44/50 (88%, 76–94) | 45/50 (90%, 79–96) | 4/50 (8%, 3–19) | 4/50 (8%, 3–19) | 14/50 (28%, 17–42) |
| one_line | 50 | 49/50 (98%, 90–100) | 33/50 (66%, 52–78) | 48/50 (96%, 87–99) | 5/50 (10%, 4–21) | 35/50 (70%, 56–81) | 18/50 (36%, 24–50) |
| gap | 50 | 47/50 (94%, 84–98) | 46/50 (92%, 81–97) | 33/50 (66%, 52–78) | 50/50 (100%, 93–100) | 6/50 (12%, 6–24) | 6/50 (12%, 6–24) |

### E4: notes, adopters against non-adopters

| cell | n | proposes_check | unverified | doc_silent | cites_gap | one_line | rounding_alone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| adopters | 58 | 57/58 (98%, 91–100) | 52/58 (90%, 79–95) | 43/58 (74%, 62–84) | 30/58 (52%, 39–64) | 10/58 (17%, 10–29) | 11/58 (19%, 11–31) |
| non-adopters | 92 | 84/92 (91%, 84–96) | 71/92 (77%, 68–85) | 83/92 (90%, 82–95) | 29/92 (32%, 23–42) | 35/92 (38%, 29–48) | 27/92 (29%, 21–39) |

## E5: two_line against 007's search-first, plain-notice cell (45/72; across experiments)

- two_line vs 007 search_plain: 25/50 vs 45/72, difference -12 points, p = 0.1952

## E6: gap against one_line (exploratory)

- gap vs one_line: 26/50 vs 7/50, difference +38 points, p = 0.0001

## E7: other code features

| cell | n | offers a switch | visible tests pass | tampered | changed a doc |
| --- | --- | --- | --- | --- | --- |
| two_line | 50 | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| one_line | 50 | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| gap | 50 | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 3/50 (6%, 2–16) | 3/50 (6%, 2–16) |

### E7: doc edits and switches, adopters against non-adopters

| cell | n | changed a doc | offers a switch |
| --- | --- | --- | --- |
| adopters | 58 | 3/58 (5%, 2–14) | 0/58 (0%, 0–6) |
| non-adopters | 92 | 0/92 (0%, 0–4) | 0/92 (0%, 0–4) |

