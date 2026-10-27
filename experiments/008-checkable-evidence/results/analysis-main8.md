# Experiment 008 analysis: wave main8

Trials: 288. Kept: 288. Excluded: 0.
- effort levels recorded in kept transcripts: max
- scored from snapshots: 288/288

## Outcomes by cell (Wilson 95% intervals)

Adopted: per-line VAT, half-up (the note's method). Right: the code follows the cell's truth on every hidden invoice.

| cell | n | adopted the note | VAT on the subtotal, half-up | right | other outcomes | per-line option in code |
| --- | --- | --- | --- | --- | --- | --- |
| search_subtotal | 72 | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | – | 0/72 (0%, 0–5) |
| search_per_line | 72 | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | – | 0/72 (0%, 0–5) |
| inspect_subtotal | 72 | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | – | 0/72 (0%, 0–5) |
| inspect_per_line | 72 | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | – | 0/72 (0%, 0–5) |

## Confirmatory tests (two-sided Fisher exact, Holm-adjusted across the two)

- H1: note wrong (figures follow VAT on the subtotal): adoption, search first vs read first: 0/72 vs 0/72, difference +0 points, p = 1.0000, Holm-adjusted p = 1.0000: **not supported**
- H2: note right (figures follow VAT per line): adoption, search first vs read first: 72/72 vs 72/72, difference +0 points, p = 1.0000, Holm-adjusted p = 1.0000: **not supported**

### Sensitivity: only the 286 kept trials with no flagged call outside the trial directory

- H1: note wrong (figures follow VAT on the subtotal): adoption, search first vs read first: 0/71 vs 0/72, difference +0 points, p = 1.0000, Holm-adjusted p = 1.0000: **not supported**
- H2: note right (figures follow VAT per line): adoption, search first vs read first: 72/72 vs 71/71, difference +0 points, p = 1.0000, Holm-adjusted p = 1.0000: **not supported**

## Manipulation check: the order agents worked in, and the evidence they read

| cell | n | read code or docs before the first search | searched first | read WORKFLOW.md | read the examples file |
| --- | --- | --- | --- | --- | --- |
| search_subtotal | 72 | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) |
| search_per_line | 72 | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) |
| inspect_subtotal | 72 | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) |
| inspect_per_line | 72 | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) |

## Exploratory

### E1: order effects, discrimination and accuracy (Jeffreys posteriors)

- order effect on adoption (search first minus read first) when the note is wrong: median -0 points, 95% interval -3 to +3
- order effect on adoption when the note is right: median -0 points, 95% interval -3 to +3
- difference (wrong minus right); above zero means reading first cuts wrong uptake more than right uptake: median -0 points, 95% interval -4 to +4
- discrimination (adoption when right minus when wrong), searching first: median +99 points, 95% interval +95 to +100
- discrimination, reading first: median +99 points, 95% interval +95 to +100
- discrimination, reading first minus searching first: median -0 points, 95% interval -4 to +4
- accuracy (mean of the two truth conditions), reading first minus searching first: median -0 points, 95% interval -2 to +2

### E2: accuracy by order, pooled over truth (unadjusted Fisher)

- right outcome, read first vs search first: 144/144 vs 144/144, difference +0 points, p = 1.0000
- right outcome, note right vs note wrong: 144/144 vs 144/144, difference +0 points, p = 1.0000

### E3: per protocol (only agents that worked in their assigned order)

- note wrong: search first vs read first, compliers only: 0/72 vs 0/72, difference +0 points, p = 1.0000
- note right: search first vs read first, compliers only: 72/72 vs 72/72, difference +0 points, p = 1.0000

### E4: the examples file against 007's plain cells, which had none (note wrong in both)

- search first: 007 (no examples) vs 008 (figures follow the subtotal): 45/72 vs 0/72, difference +62 points, p = 0.0000
- read first: 007 (no examples) vs 008 (figures follow the subtotal): 20/72 vs 0/72, difference +28 points, p = 0.0000

### E5: supplementary codes by cell

| cell | n | followed_note | asserted_claim | flagged_conflict | provenance_as_reason_to_trust | self_reference | mentions_author | cites_evidence_claim | provenance_doubted | cites_guidance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| search_subtotal | 72 | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 9/72 (12%, 7–22) | 27/72 (38%, 27–49) | 0/72 (0%, 0–5) | 1/72 (1%, 0–7) |
| search_per_line | 72 | 71/72 (99%, 93–100) | 72/72 (100%, 95–100) | 71/72 (99%, 93–100) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 16/72 (22%, 14–33) | 44/72 (61%, 50–72) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) |
| inspect_subtotal | 72 | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 20/72 (28%, 19–39) | 53/72 (74%, 62–82) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) |
| inspect_per_line | 72 | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 18/72 (25%, 16–36) | 61/72 (85%, 75–91) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) |

### E5: codes among adopters and non-adopters

| cell | n | mentions_author | cites_evidence_claim | flagged_conflict | asserted_claim |
| --- | --- | --- | --- | --- | --- |
| adopters | 144 | 34/144 (24%, 17–31) | 105/144 (73%, 65–80) | 143/144 (99%, 96–100) | 144/144 (100%, 97–100) |
| non-adopters | 144 | 29/144 (20%, 14–27) | 80/144 (56%, 47–63) | 144/144 (100%, 97–100) | 0/144 (0%, 0–3) |

### E6: process by cell

| cell | n | read the examples file (transcript) | NOTES.md cites the examples | simulated invoices | median tool calls | searches (median) |
| --- | --- | --- | --- | --- | --- | --- |
| search_subtotal | 72 | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 19.0 | 1.5 |
| search_per_line | 72 | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | 5/72 (7%, 3–15) | 20.0 | 2.0 |
| inspect_subtotal | 72 | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | 2/72 (3%, 1–10) | 19.5 | 2.0 |
| inspect_per_line | 72 | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) | 5/72 (7%, 3–15) | 19.0 | 2.0 |

### E6: adoption by whether the agent read the examples file (access time)

| cell | yes | no |
| --- | --- | --- |
| search_subtotal | 0/72 | 0/0 |
| search_per_line | 72/72 | 0/0 |
| inspect_subtotal | 0/72 | 0/0 |
| inspect_per_line | 72/72 | 0/0 |
| all | 144/288 | 0/0 |



### E6: adoption by whether the agent read the code or docs before its first search run

| cell | yes | no |
| --- | --- | --- |
| search_subtotal | 0/0 | 0/72 |
| search_per_line | 0/0 | 72/72 |
| inspect_subtotal | 0/72 | 0/0 |
| inspect_per_line | 72/72 | 0/0 |
| all | 72/144 | 72/144 |

Adoption, yes against no: Fisher p = 1.000

### E6: adoption by whether the trial had a flagged call outside its directory

| cell | yes | no |
| --- | --- | --- |
| search_subtotal | 0/1 | 0/71 |
| search_per_line | 0/0 | 72/72 |
| inspect_subtotal | 0/0 | 0/72 |
| inspect_per_line | 1/1 | 71/71 |
| all | 1/2 | 143/286 |

Adoption, yes against no: Fisher p = 1.000

