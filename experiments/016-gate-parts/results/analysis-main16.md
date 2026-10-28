# Experiment 016 analysis: main16

150 trials, 150 kept, 0 excluded.

## Exclusions

- none

## Outcomes by cell

| cell | n | adopted (per line, half-up) | correct (subtotal, half-up) | unchanged | per line, half-even | other or error |
| --- | --- | --- | --- | --- | --- | --- |
| gap | 50 | 24/50 (48%, 35–61) | 26/50 (52%, 39–65) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| instr | 50 | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| pending | 50 | 6/50 (12%, 6–24) | 44/50 (88%, 76–94) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |

## Confirmatory tests

- H1: instr vs gap: 0/50 vs 24/50, difference -48 points, p = 0.0000, Holm-adjusted 0.0000: **supported**
- H2: pending vs gap: 6/50 vs 24/50, difference -36 points, p = 0.0002, Holm-adjusted 0.0002: **supported**

### Sensitivity: kept trials with no flagged call

- H1: instr vs gap: 0/50 vs 23/49, difference -47 points, p = 0.0000, Holm-adjusted 0.0000: **supported**
- H2: pending vs gap: 6/50 vs 23/49, difference -35 points, p = 0.0002, Holm-adjusted 0.0002: **supported**

### Sensitivity: kept trials not held by a session pause (0 held left out)

- H1: instr vs gap: 0/50 vs 24/50, difference -48 points, p = 0.0000, Holm-adjusted 0.0000: **supported**
- H2: pending vs gap: 6/50 vs 24/50, difference -36 points, p = 0.0002, Holm-adjusted 0.0002: **supported**

## E1: Jeffreys posteriors

- instr minus gap: median -47 points, 95% interval -61 to -33
- pending minus gap: median -35 points, 95% interval -51 to -19
- pending minus instr: median +11 points, 95% interval +4 to +22

## E2: manipulation check (searched before opening code, tests or rules doc)

| cell | n | searched first | opened the rules doc |
| --- | --- | --- | --- |
| gap | 50 | 48/50 (96%, 87–99) | 50/50 (100%, 93–100) |
| instr | 50 | 49/50 (98%, 90–100) | 50/50 (100%, 93–100) |
| pending | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) |

## E3: per protocol (searched first only; not randomized)

- H1: instr vs gap: 0/49 vs 24/48, difference -50 points, p = 0.0000, Holm-adjusted 0.0000: **supported**
- H2: pending vs gap: 6/50 vs 24/48, difference -38 points, p = 0.0001, Holm-adjusted 0.0001: **supported**

## E4: notes, by cell

| cell | n | proposes_check | unverified | doc_silent | cites_gap | rounding_alone | cites_instruction | cites_pending | cites_200 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gap | 50 | 50/50 (100%, 93–100) | 43/50 (86%, 74–93) | 40/50 (80%, 67–89) | 50/50 (100%, 93–100) | 6/50 (12%, 6–24) | 1/50 (2%, 0–10) | 7/50 (14%, 7–26) | 44/50 (88%, 76–94) |
| instr | 50 | 46/50 (92%, 81–97) | 41/50 (82%, 69–90) | 43/50 (86%, 74–93) | 48/50 (96%, 87–99) | 7/50 (14%, 7–26) | 47/50 (94%, 84–98) | 9/50 (18%, 10–31) | 16/50 (32%, 21–46) |
| pending | 50 | 43/50 (86%, 74–93) | 41/50 (82%, 69–90) | 39/50 (78%, 65–87) | 49/50 (98%, 90–100) | 5/50 (10%, 4–21) | 0/50 (0%, 0–7) | 37/50 (74%, 60–84) | 33/50 (66%, 52–78) |

### E4: notes, adopters against non-adopters

| cell | n | proposes_check | unverified | doc_silent | cites_gap | rounding_alone | cites_instruction | cites_pending | cites_200 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adopters | 30 | 28/30 (93%, 79–98) | 27/30 (90%, 74–97) | 19/30 (63%, 46–78) | 30/30 (100%, 89–100) | 6/30 (20%, 10–37) | 0/30 (0%, 0–11) | 8/30 (27%, 14–44) | 28/30 (93%, 79–98) |
| non-adopters | 120 | 111/120 (92%, 86–96) | 98/120 (82%, 74–88) | 103/120 (86%, 78–91) | 117/120 (98%, 93–99) | 12/120 (10%, 6–17) | 48/120 (40%, 32–49) | 45/120 (38%, 29–46) | 65/120 (54%, 45–63) |

## E5: each cell against 015's gap (21/50) and owner (0/50) cells and 014's gap cell (26/50) (across experiments; not randomized)

- gap vs 015 gap: 24/50 vs 21/50, difference +6 points, p = 0.6879
- gap vs 015 owner: 24/50 vs 0/50, difference +48 points, p = 0.0000
- gap vs 014 gap: 24/50 vs 26/50, difference -4 points, p = 0.8416
- instr vs 015 gap: 0/50 vs 21/50, difference -42 points, p = 0.0000
- instr vs 015 owner: 0/50 vs 0/50, difference +0 points, p = 1.0000
- instr vs 014 gap: 0/50 vs 26/50, difference -52 points, p = 0.0000
- pending vs 015 gap: 6/50 vs 21/50, difference -30 points, p = 0.0013
- pending vs 015 owner: 6/50 vs 0/50, difference +12 points, p = 0.0267
- pending vs 014 gap: 6/50 vs 26/50, difference -40 points, p = 0.0000

## E6: pending against instr (exploratory)

- pending vs instr: 6/50 vs 0/50, difference +12 points, p = 0.0267

## E7: other code features

| cell | n | offers a switch | visible tests pass | tampered | changed a doc |
| --- | --- | --- | --- | --- | --- |
| gap | 50 | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 1/50 (2%, 0–10) | 1/50 (2%, 0–10) |
| instr | 50 | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| pending | 50 | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |

### E7: doc edits and switches, adopters against non-adopters

| cell | n | changed a doc | offers a switch |
| --- | --- | --- | --- |
| adopters | 30 | 1/30 (3%, 1–17) | 0/30 (0%, 0–11) |
| non-adopters | 120 | 0/120 (0%, 0–3) | 0/120 (0%, 0–3) |

