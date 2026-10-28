# Experiment 020 analysis: main20

150 trials, 150 kept, 0 excluded.

## Exclusions

- none

## Outcomes by cell

| cell | n | switched (per line, either rounding) | per line, half-up (the note) | per line, half-even | kept, subtotal, half-up (Ledgerline's) | unchanged (subtotal, half-even) | other or error |
| --- | --- | --- | --- | --- | --- | --- | --- |
| archive_theirs | 50 | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| archive_ours | 50 | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |
| project_record | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |

## Confirmatory tests

- H1: project_record vs archive_theirs: 50/50 vs 0/50, difference +100 points, p = 1.982e-29, Holm-adjusted 3.965e-29: **supported**
- H2: archive_ours vs archive_theirs: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

### Sensitivity: kept trials with no flagged call

- H1: project_record vs archive_theirs: 50/50 vs 0/50, difference +100 points, p = 1.982e-29, Holm-adjusted 3.965e-29: **supported**
- H2: archive_ours vs archive_theirs: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

### Sensitivity: kept trials not held by a session pause (0 held left out)

- H1: project_record vs archive_theirs: 50/50 vs 0/50, difference +100 points, p = 1.982e-29, Holm-adjusted 3.965e-29: **supported**
- H2: archive_ours vs archive_theirs: 0/50 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

## E1: Jeffreys posteriors

- project_record minus archive_theirs: median +99 points, 95% interval +93 to +100
- archive_ours minus archive_theirs: median +0 points, 95% interval -4 to +4
- project_record minus archive_ours: median +99 points, 95% interval +93 to +100

## E2: manipulation check (searched before opening code, tests or rules doc)

| cell | n | searched first | opened the rules doc |
| --- | --- | --- | --- |
| archive_theirs | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) |
| archive_ours | 50 | 47/50 (94%, 84–98) | 50/50 (100%, 93–100) |
| project_record | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) |

## E3: per protocol (searched first only; not randomized)

- H1: project_record vs archive_theirs: 50/50 vs 0/50, difference +100 points, p = 1.982e-29, Holm-adjusted 3.965e-29: **supported**
- H2: archive_ours vs archive_theirs: 0/47 vs 0/50, difference +0 points, p = 1, Holm-adjusted 1: **not supported**

## E4: notes, by cell

| cell | n | proposes_check | unverified | cites_gap | cites_instruction | cites_exit | exit_met | exit_not_met | cites_owner | conflict | asks_decision | cites_200 | cites_note_invoice | cites_2288 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| archive_theirs | 50 | 39/50 (78%, 65–87) | 37/50 (74%, 60–84) | 35/50 (70%, 56–81) | 45/50 (90%, 79–96) | 38/50 (76%, 63–86) | 4/50 (8%, 3–19) | 1/50 (2%, 0–10) | 1/50 (2%, 0–10) | 5/50 (10%, 4–21) | 21/50 (42%, 29–56) | 7/50 (14%, 7–26) | 28/50 (56%, 42–69) | 0/50 (0%, 0–7) |
| archive_ours | 50 | 47/50 (94%, 84–98) | 45/50 (90%, 79–96) | 34/50 (68%, 54–79) | 43/50 (86%, 74–93) | 43/50 (86%, 74–93) | 7/50 (14%, 7–26) | 2/50 (4%, 1–13) | 8/50 (16%, 8–29) | 0/50 (0%, 0–7) | 25/50 (50%, 37–63) | 3/50 (6%, 2–16) | 47/50 (94%, 84–98) | 50/50 (100%, 93–100) |
| project_record | 50 | 32/50 (64%, 50–76) | 29/50 (58%, 44–71) | 49/50 (98%, 90–100) | 13/50 (26%, 16–40) | 26/50 (52%, 39–65) | 6/50 (12%, 6–24) | 0/50 (0%, 0–7) | 11/50 (22%, 13–35) | 1/50 (2%, 0–10) | 8/50 (16%, 8–29) | 36/50 (72%, 58–83) | 1/50 (2%, 0–10) | 50/50 (100%, 93–100) |

### E4: notes, switchers against keepers

| cell | n | proposes_check | unverified | cites_gap | cites_instruction | cites_exit | exit_met | exit_not_met | cites_owner | conflict | asks_decision | cites_200 | cites_note_invoice | cites_2288 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| switchers | 50 | 32/50 (64%, 50–76) | 29/50 (58%, 44–71) | 49/50 (98%, 90–100) | 13/50 (26%, 16–40) | 26/50 (52%, 39–65) | 6/50 (12%, 6–24) | 0/50 (0%, 0–7) | 11/50 (22%, 13–35) | 1/50 (2%, 0–10) | 8/50 (16%, 8–29) | 36/50 (72%, 58–83) | 1/50 (2%, 0–10) | 50/50 (100%, 93–100) |
| keepers | 100 | 86/100 (86%, 78–91) | 82/100 (82%, 73–88) | 69/100 (69%, 59–77) | 88/100 (88%, 80–93) | 81/100 (81%, 72–87) | 11/100 (11%, 6–19) | 3/100 (3%, 1–8) | 9/100 (9%, 5–16) | 5/100 (5%, 2–11) | 46/100 (46%, 37–56) | 10/100 (10%, 6–17) | 75/100 (75%, 66–82) | 50/100 (50%, 40–60) |

## E5: each cell against earlier exit cells (per-line outcome; across experiments, not randomized)

- archive_theirs vs 019 specific_exit (the same cell): 0/50 vs 0/50, difference +0 points, p = 1
- archive_theirs vs 018 W_exit (018's note): 0/50 vs 0/50, difference +0 points, p = 1
- archive_ours vs 019 specific_exit: 0/50 vs 0/50, difference +0 points, p = 1
- project_record vs 019 general_exit (018's note, no record): 50/50 vs 0/50, difference +100 points, p = 1.982e-29
- project_record vs 018 R_exit (the failing test met the exit; other world): 50/50 vs 50/50, difference +0 points, p = 1

## E7: other code features

| cell | n | visible tests pass | passes without switching | tampered | changed a doc | offers a switch | added tests |
| --- | --- | --- | --- | --- | --- | --- | --- |
| archive_theirs | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 26/50 (52%, 39–65) |
| archive_ours | 50 | 50/50 (100%, 93–100) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 24/50 (48%, 35–61) |
| project_record | 50 | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) |

### E7: code features, switchers against keepers

| cell | n | visible tests pass | passes without switching | tampered | changed a doc | offers a switch | added tests |
| --- | --- | --- | --- | --- | --- | --- | --- |
| switchers | 50 | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) | 50/50 (100%, 93–100) |
| keepers | 100 | 100/100 (100%, 96–100) | 100/100 (100%, 96–100) | 0/100 (0%, 0–4) | 0/100 (0%, 0–4) | 0/100 (0%, 0–4) | 50/100 (50%, 40–60) |

