# Experiment 019 analysis: main19

150 trials, 150 kept, 0 excluded.

## Exclusions

- none

## Outcomes by cell

| cell | n | switched (per line, either rounding) | per line, half-up (the note) | per line, half-even | kept, subtotal, half-up (Ledgerline's) | unchanged (subtotal, half-even) | other or error |
| --- | --- | --- | --- | --- | --- | --- | --- |
| general_exit | 50 | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| specific_exit | 50 | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| specific_instr | 50 | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |

## Confirmatory tests

- H1: specific_exit vs general_exit: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**
- H2: specific_exit vs specific_instr: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

### Sensitivity: kept trials with no flagged call

- H1: specific_exit vs general_exit: 0/49 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**
- H2: specific_exit vs specific_instr: 0/49 vs 0/49, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

### Sensitivity: kept trials not held by a session pause (0 held left out)

- H1: specific_exit vs general_exit: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**
- H2: specific_exit vs specific_instr: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

## E1: Jeffreys posteriors

- specific_exit minus general_exit: median +0 points, 95% interval -4 to +4
- specific_exit minus specific_instr: median +0 points, 95% interval -4 to +4
- specific_instr minus general_exit: median -0 points, 95% interval -4 to +4

## E2: manipulation check (searched before opening code, tests or rules doc)

| cell | n | searched first | opened the rules doc |
| --- | --- | --- | --- |
| general_exit | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) |
| specific_exit | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) |
| specific_instr | 50 | 49/50 (98%, 90–100) | 50/50 (100%, 93–100) |

## E3: per protocol (searched first only; not randomized)

- H1: specific_exit vs general_exit: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**
- H2: specific_exit vs specific_instr: 0/50 vs 0/49, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

## E4: notes, by cell

| cell | n | proposes_check | unverified | cites_gap | cites_instruction | cites_exit | exit_met | exit_not_met | cites_owner | conflict | asks_decision | cites_200 | cites_note_invoice |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| general_exit | 50 | 32/50 (64%, 50–76) | 32/50 (64%, 50–76) | 36/50 (72%, 58–83) | 43/50 (86%, 74–93) | 37/50 (74%, 60–84) | 1/50 (2%, 0–10) | 1/50 (2%, 0–10) | 1/50 (2%, 0–10) | 1/50 (2%, 0–10) | 23/50 (46%, 33–60) | 28/50 (56%, 42–69) | 2/50 (4%, 1–13) |
| specific_exit | 50 | 34/50 (68%, 54–79) | 33/50 (66%, 52–78) | 34/50 (68%, 54–79) | 46/50 (92%, 81–97) | 36/50 (72%, 58–83) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 1/50 (2%, 0–10) | 16/50 (32%, 21–46) | 12/50 (24%, 14–37) | 36/50 (72%, 58–83) |
| specific_instr | 50 | 50/50 (100%, 93–100) | 40/50 (80%, 67–89) | 39/50 (78%, 65–87) | 48/50 (96%, 87–99) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 1/50 (2%, 0–10) | 13/50 (26%, 16–40) | 14/50 (28%, 17–42) | 8/50 (16%, 8–29) | 35/50 (70%, 56–81) |

### E4: notes, switchers against keepers

| cell | n | proposes_check | unverified | cites_gap | cites_instruction | cites_exit | exit_met | exit_not_met | cites_owner | conflict | asks_decision | cites_200 | cites_note_invoice |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| switchers | 0 | – | – | – | – | – | – | – | – | – | – | – | – |
| keepers | 150 | 116/150 (77%, 70–83) | 105/150 (70%, 62–77) | 109/150 (73%, 65–79) | 137/150 (91%, 86–95) | 73/150 (49%, 41–57) | 1/150 (1%, 0–4) | 1/150 (1%, 0–4) | 2/150 (1%, 0–5) | 15/150 (10%, 6–16) | 53/150 (35%, 28–43) | 48/150 (32%, 25–40) | 73/150 (49%, 41–57) |

## E5: each cell against earlier world-W cells with 018's note (per-line outcome; across experiments, not randomized)

- general_exit vs 018 W_exit: 0/50 vs 0/50, difference +0 points, p = 1
- general_exit vs 014 to 016 gap (the bare item): 0/50 vs 71/150, difference -47 points, p = 5.03e-12
- specific_exit vs 018 W_exit (018's note): 0/50 vs 0/50, difference +0 points, p = 1
- specific_instr vs 016 instr (018's note): 0/50 vs 0/50, difference +0 points, p = 1
- specific_instr vs 018 W_instr (018's note): 0/50 vs 0/50, difference +0 points, p = 1

## E7: other code features

| cell | n | visible tests pass | passes without switching | tampered | changed a doc | offers a switch | added tests |
| --- | --- | --- | --- | --- | --- | --- | --- |
| general_exit | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 18/50 (36%, 24–50) |
| specific_exit | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 16/50 (32%, 21–46) |
| specific_instr | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 17/50 (34%, 22–48) |

### E7: code features, switchers against keepers

| cell | n | visible tests pass | passes without switching | tampered | changed a doc | offers a switch | added tests |
| --- | --- | --- | --- | --- | --- | --- | --- |
| switchers | 0 | – | – | – | – | – | – |
| keepers | 150 | 150/150 (100%, 98–100) | 150/150 (100%, 98–100) | 0/150 (0%, 0–2) | 0/150 (0%, 0–2) | 0/150 (0%, 0–2) | 51/150 (34%, 27–42) |

