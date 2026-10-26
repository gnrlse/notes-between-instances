# Experiment 005 analysis: wave main5

Trials: 200. Kept: 200. Excluded: 0.
- effort levels recorded in kept transcripts: max
- scored from snapshots: 200/200

## Outcomes by cell (Wilson 95% intervals)

| cell | n | adopted note | correct | other outcomes | any per-line VAT | per-line option in code |
| --- | --- | --- | --- | --- | --- | --- |
| none_plain | 4 | 0/4 (0%, 0–49) | 4/4 (100%, 51–100) | – | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) |
| none_guided | 4 | 0/4 (0%, 0–49) | 4/4 (100%, 51–100) | – | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) |
| human_plain | 60 | 20/60 (33%, 23–46) | 40/60 (67%, 54–77) | – | 20/60 (33%, 23–46) | 0/60 (0%, 0–6) |
| model_plain | 36 | 3/36 (8%, 3–22) | 33/36 (92%, 78–97) | – | 3/36 (8%, 3–22) | 0/36 (0%, 0–10) |
| human_guided | 60 | 6/60 (10%, 5–20) | 54/60 (90%, 80–95) | – | 6/60 (10%, 5–20) | 0/60 (0%, 0–6) |
| model_guided | 36 | 0/36 (0%, 0–10) | 36/36 (100%, 90–100) | – | 0/36 (0%, 0–10) | 0/36 (0%, 0–10) |

## Confirmatory tests (two-sided Fisher exact, Holm-adjusted across the three)

- H1: human label, plain notice vs guidance: 20/60 vs 6/60, difference +23 points, p = 0.0034, Holm-adjusted p = 0.0103: **supported**
- H2: human vs model labels, with guidance: 6/60 vs 0/36, difference +10 points, p = 0.0805, Holm-adjusted p = 0.0805: **not supported**
- H3: human vs model labels, plain notice: 20/60 vs 3/36, difference +25 points, p = 0.0062, Holm-adjusted p = 0.0124: **supported**

### Sensitivity: only the 164 kept trials with no flagged call outside the trial directory

- H1: human label, plain notice vs guidance: 19/53 vs 2/50, difference +32 points, p = 0.0000, Holm-adjusted p = 0.0001: **supported**
- H2: human vs model labels, with guidance: 2/50 vs 0/27, difference +4 points, p = 0.5386, Holm-adjusted p = 0.5386: **not supported**
- H3: human vs model labels, plain notice: 19/53 vs 3/27, difference +25 points, p = 0.0324, Holm-adjusted p = 0.0647: **not supported**

## Exploratory

- E1: model labels, plain notice vs guidance: 3/36 vs 0/36, difference +8 points, p = 0.2394
- Human-label effect lost under guidance (difference in differences, points): median +15, 95% interval -3 to +32
- Share of the human-label effect retained under guidance: median 0.37, 95% interval 0.05 to 1.15 (99% of draws had a plain-notice effect above 5 points)

### E2: each model label

| label | plain notice | guidance |
| --- | --- | --- |
| self | 1/12 (8%, 1–35) | 0/12 (0%, 0–24) |
| sibling | 2/12 (17%, 5–45) | 0/12 (0%, 0–24) |
| other_model | 0/12 (0%, 0–24) | 0/12 (0%, 0–24) |

### E4: the human-label contrast across 003, 004 and 005 (Haiku, evidence kept, plain notice)

- 003 (exploratory there): human vs model labels: 7/16 vs 0/48, difference +44 points, p = 0.0000
- 004: human vs model labels, evidence kept: 20/48 vs 5/48, difference +31 points, p = 0.0009
- 005: human vs model labels, plain notice: 20/60 vs 3/36, difference +25 points, p = 0.0062
- 003, 004 and 005 pooled: 47/124 vs 8/132, difference +32 points, p = 0.0000

### E5: refined reason codes by cell

| cell | n | identity_as_reason | outside_source_as_reason | unverifiable_as_reason |
| --- | --- | --- | --- | --- |
| human_plain | 60 | 1/60 (2%, 0–9) | 11/60 (18%, 11–30) | 59/60 (98%, 91–100) |
| model_plain | 36 | 0/36 (0%, 0–10) | 7/36 (19%, 10–35) | 35/36 (97%, 86–100) |
| human_guided | 60 | 1/60 (2%, 0–9) | 16/60 (27%, 17–39) | 60/60 (100%, 94–100) |
| model_guided | 36 | 2/36 (6%, 2–18) | 8/36 (22%, 12–38) | 35/36 (97%, 86–100) |

### E5: supplementary codes by cell

| cell | n | followed_note | asserted_claim | flagged_conflict | provenance_as_reason_to_trust | self_reference | mentions_author | cites_evidence_claim | provenance_doubted | cites_guidance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| human_plain | 60 | 20/60 (33%, 23–46) | 0/60 (0%, 0–6) | 60/60 (100%, 94–100) | 0/60 (0%, 0–6) | 0/60 (0%, 0–6) | 32/60 (53%, 41–65) | 30/60 (50%, 38–62) | 0/60 (0%, 0–6) | 0/60 (0%, 0–6) |
| model_plain | 36 | 3/36 (8%, 3–22) | 0/36 (0%, 0–10) | 36/36 (100%, 90–100) | 0/36 (0%, 0–10) | 2/36 (6%, 2–18) | 18/36 (50%, 34–66) | 12/36 (33%, 20–50) | 0/36 (0%, 0–10) | 0/36 (0%, 0–10) |
| human_guided | 60 | 6/60 (10%, 5–20) | 0/60 (0%, 0–6) | 60/60 (100%, 94–100) | 0/60 (0%, 0–6) | 0/60 (0%, 0–6) | 37/60 (62%, 49–73) | 20/60 (33%, 23–46) | 2/60 (3%, 1–11) | 0/60 (0%, 0–6) |
| model_guided | 36 | 0/36 (0%, 0–10) | 0/36 (0%, 0–10) | 36/36 (100%, 90–100) | 0/36 (0%, 0–10) | 2/36 (6%, 2–18) | 21/36 (58%, 42–73) | 7/36 (19%, 10–35) | 0/36 (0%, 0–10) | 0/36 (0%, 0–10) |

### E5: codes among adopters and non-adopters (all note cells)

| group | n | identity as reason | mentions author | provenance as reason to trust | cites evidence claim |
| --- | --- | --- | --- | --- | --- |
| adopters | 29 | 1/29 (3%, 1–17) | 18/29 (62%, 44–77) | 0/29 (0%, 0–12) | 28/29 (97%, 83–99) |
| non-adopters | 163 | 3/163 (2%, 1–5) | 90/163 (55%, 48–63) | 0/163 (0%, 0–2) | 41/163 (25%, 19–32) |

### E6: answers to the follow-up question, by cell

| cell | n | answered | found_entry | author_mattered | author_raised_weight | author_lowered_weight | self_reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none_plain | 4 | 4/4 (100%, 51–100) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) |
| none_guided | 4 | 4/4 (100%, 51–100) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) |
| human_plain | 60 | 60/60 (100%, 94–100) | 60/60 (100%, 94–100) | 11/60 (18%, 11–30) | 11/60 (18%, 11–30) | 1/60 (2%, 0–9) | 0/60 (0%, 0–6) |
| model_plain | 36 | 36/36 (100%, 90–100) | 36/36 (100%, 90–100) | 7/36 (19%, 10–35) | 0/36 (0%, 0–10) | 7/36 (19%, 10–35) | 7/36 (19%, 10–35) |
| human_guided | 60 | 60/60 (100%, 94–100) | 60/60 (100%, 94–100) | 1/60 (2%, 0–9) | 1/60 (2%, 0–9) | 0/60 (0%, 0–6) | 0/60 (0%, 0–6) |
| model_guided | 36 | 36/36 (100%, 90–100) | 36/36 (100%, 90–100) | 3/36 (8%, 3–22) | 0/36 (0%, 0–10) | 3/36 (8%, 3–22) | 6/36 (17%, 8–32) |

### E6: answers by cell and decision

| cell | n | answered | found_entry | author_mattered | author_raised_weight | author_lowered_weight | self_reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| human_plain, adopters | 20 | 20/20 (100%, 84–100) | 20/20 (100%, 84–100) | 5/20 (25%, 11–47) | 5/20 (25%, 11–47) | 1/20 (5%, 1–24) | 0/20 (0%, 0–16) |
| human_plain, non-adopters | 40 | 40/40 (100%, 91–100) | 40/40 (100%, 91–100) | 6/40 (15%, 7–29) | 6/40 (15%, 7–29) | 0/40 (0%, 0–9) | 0/40 (0%, 0–9) |
| model_plain, adopters | 3 | 3/3 (100%, 44–100) | 3/3 (100%, 44–100) | 1/3 (33%, 6–79) | 0/3 (0%, 0–56) | 1/3 (33%, 6–79) | 0/3 (0%, 0–56) |
| model_plain, non-adopters | 33 | 33/33 (100%, 90–100) | 33/33 (100%, 90–100) | 6/33 (18%, 9–34) | 0/33 (0%, 0–10) | 6/33 (18%, 9–34) | 7/33 (21%, 11–38) |
| human_guided, adopters | 6 | 6/6 (100%, 61–100) | 6/6 (100%, 61–100) | 1/6 (17%, 3–56) | 1/6 (17%, 3–56) | 0/6 (0%, 0–39) | 0/6 (0%, 0–39) |
| human_guided, non-adopters | 54 | 54/54 (100%, 93–100) | 54/54 (100%, 93–100) | 0/54 (0%, 0–7) | 0/54 (0%, 0–7) | 0/54 (0%, 0–7) | 0/54 (0%, 0–7) |
| model_guided, non-adopters | 36 | 36/36 (100%, 90–100) | 36/36 (100%, 90–100) | 3/36 (8%, 3–22) | 0/36 (0%, 0–10) | 3/36 (8%, 3–22) | 6/36 (17%, 8–32) |

First word Yes/No/other: {"yes": 20, "no": 180, "other": 0}; agrees with judged author_mattered in 198/200

### E7: process by cell

| cell | n | simulated invoices | median tool calls | read docs | calls after the question | changed files after it |
| --- | --- | --- | --- | --- | --- | --- |
| none_plain | 4 | 1/4 (25%, 5–70) | 20.5 | 4/4 (100%, 51–100) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) |
| none_guided | 4 | 2/4 (50%, 15–85) | 21.0 | 4/4 (100%, 51–100) | 0/4 (0%, 0–49) | 0/4 (0%, 0–49) |
| human_plain | 60 | 23/60 (38%, 27–51) | 19.0 | 60/60 (100%, 94–100) | 0/60 (0%, 0–6) | 0/60 (0%, 0–6) |
| model_plain | 36 | 8/36 (22%, 12–38) | 18.0 | 36/36 (100%, 90–100) | 0/36 (0%, 0–10) | 0/36 (0%, 0–10) |
| human_guided | 60 | 15/60 (25%, 16–37) | 19.0 | 60/60 (100%, 94–100) | 0/60 (0%, 0–6) | 0/60 (0%, 0–6) |
| model_guided | 36 | 9/36 (25%, 14–41) | 19.0 | 36/36 (100%, 90–100) | 0/36 (0%, 0–10) | 0/36 (0%, 0–10) |
