# Experiment 017 analysis: main17

150 trials, 150 kept, 0 excluded.

## Exclusions

- none

## Outcomes by cell

| cell | n | switched (per line, either rounding) | per line, half-up (Ledgerline) | per line, half-even | kept, subtotal, half-up | unchanged (subtotal, half-even) | other or error |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gap | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| instr | 50 | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| until | 50 | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |

## Confirmatory tests

- H1: instr vs gap: 0/50 vs 50/50, difference -100 points, p = 1.982e-29, Holm-adjusted 3.965e-29: **supported**
- H2: until vs instr: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

### Sensitivity: kept trials with no flagged call

- H1: instr vs gap: 0/50 vs 50/50, difference -100 points, p = 1.982e-29, Holm-adjusted 3.965e-29: **supported**
- H2: until vs instr: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

### Sensitivity: kept trials not held by a session pause (0 held left out)

- H1: instr vs gap: 0/50 vs 50/50, difference -100 points, p = 1.982e-29, Holm-adjusted 3.965e-29: **supported**
- H2: until vs instr: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

## E1: Jeffreys posteriors

- instr minus gap: median -99 points, 95% interval -100 to -93
- until minus gap: median -99 points, 95% interval -100 to -93
- until minus instr: median -0 points, 95% interval -4 to +4

## E2: manipulation check (searched before opening code, tests or rules doc)

| cell | n | searched first | opened the rules doc |
| --- | --- | --- | --- |
| gap | 50 | 49/50 (98%, 90–100) | 50/50 (100%, 93–100) |
| instr | 50 | 48/50 (96%, 87–99) | 50/50 (100%, 93–100) |
| until | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) |

## E3: per protocol (searched first only; not randomized)

- H1: instr vs gap: 0/48 vs 49/49, difference -100 points, p = 7.85e-29, Holm-adjusted 1.57e-28: **supported**
- H2: until vs instr: 0/50 vs 0/48, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

## E4: notes, by cell

| cell | n | proposes_check | unverified | cites_gap | cites_instruction | cites_owner | only_per_line | evidence | conflict | asks_decision | cites_200 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gap | 50 | 43/50 (86%, 74–93) | 39/50 (78%, 65–87) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 25/50 (50%, 37–63) | 10/50 (20%, 11–33) | 2/50 (4%, 1–13) | 4/50 (8%, 3–19) | 1/50 (2%, 0–10) | 47/50 (94%, 84–98) |
| instr | 50 | 48/50 (96%, 87–99) | 49/50 (98%, 90–100) | 50/50 (100%, 93–100) | 49/50 (98%, 90–100) | 5/50 (10%, 4–21) | 16/50 (32%, 21–46) | 0/50 (0%, 0–7) | 23/50 (46%, 33–60) | 50/50 (100%, 93–100) | 42/50 (84%, 71–92) |
| until | 50 | 50/50 (100%, 93–100) | 23/50 (46%, 33–60) | 46/50 (92%, 81–97) | 49/50 (98%, 90–100) | 50/50 (100%, 93–100) | 11/50 (22%, 13–35) | 1/50 (2%, 0–10) | 6/50 (12%, 6–24) | 30/50 (60%, 46–72) | 31/50 (62%, 48–74) |

### E4: notes, switchers against keepers

| cell | n | proposes_check | unverified | cites_gap | cites_instruction | cites_owner | only_per_line | evidence | conflict | asks_decision | cites_200 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| switchers | 50 | 43/50 (86%, 74–93) | 39/50 (78%, 65–87) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 25/50 (50%, 37–63) | 10/50 (20%, 11–33) | 2/50 (4%, 1–13) | 4/50 (8%, 3–19) | 1/50 (2%, 0–10) | 47/50 (94%, 84–98) |
| keepers | 100 | 98/100 (98%, 93–99) | 72/100 (72%, 63–80) | 96/100 (96%, 90–98) | 98/100 (98%, 93–99) | 55/100 (55%, 45–64) | 27/100 (27%, 19–36) | 1/100 (1%, 0–5) | 29/100 (29%, 21–39) | 80/100 (80%, 71–87) | 73/100 (73%, 64–81) |

## E5: each cell against earlier cells with the same item, where the failing invoice passed with either method (per-line outcome; across experiments, not randomized)

- gap vs 014 to 016 gap: 50/50 vs 71/150, difference +53 points, p = 7.477e-14
- instr vs 016 instr: 0/50 vs 0/50, difference +0 points, p = 1
- until vs 015 owner: 0/50 vs 0/50, difference +0 points, p = 1

## E6: until against gap (exploratory)

- until vs gap: 0/50 vs 50/50, difference -100 points, p = 1.982e-29

## E7: other code features

| cell | n | visible tests pass | passes without switching | tampered | changed a doc | offers a switch |
| --- | --- | --- | --- | --- | --- | --- |
| gap | 50 | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| instr | 50 | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| until | 50 | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |

### E7: code features, switchers against keepers

| cell | n | visible tests pass | passes without switching | tampered | changed a doc | offers a switch |
| --- | --- | --- | --- | --- | --- | --- |
| switchers | 50 | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| keepers | 100 | 0/100 (0%, 0–4) | 0/100 (0%, 0–4) | 0/100 (0%, 0–4) | 0/100 (0%, 0–4) | 0/100 (0%, 0–4) |

