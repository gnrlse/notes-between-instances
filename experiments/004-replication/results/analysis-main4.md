# Experiment 004 analysis: wave main4

Trials: 248. Kept: 248. Excluded: 0.
- effort levels recorded in kept transcripts: max
- scored from snapshots: 248/248

## Outcomes by cell (Wilson 95% intervals)

| cell | n | adopted note | correct | other outcomes | any per-line VAT | per-line option in code |
| --- | --- | --- | --- | --- | --- | --- |
| none | 8 | 0/8 (0%, 0–32) | 8/8 (100%, 68–100) | – | 0/8 (0%, 0–32) | 0/8 (0%, 0–32) |
| human_ev | 48 | 20/48 (42%, 29–56) | 28/48 (58%, 44–71) | – | 20/48 (42%, 29–56) | 0/48 (0%, 0–7) |
| unknown_ev | 48 | 4/48 (8%, 3–20) | 44/48 (92%, 80–97) | – | 4/48 (8%, 3–20) | 0/48 (0%, 0–7) |
| model_ev | 48 | 5/48 (10%, 5–22) | 43/48 (90%, 78–95) | – | 5/48 (10%, 5–22) | 0/48 (0%, 0–7) |
| human_noev | 48 | 10/48 (21%, 12–34) | 38/48 (79%, 66–88) | – | 10/48 (21%, 12–34) | 0/48 (0%, 0–7) |
| model_noev | 48 | 0/48 (0%, 0–7) | 48/48 (100%, 93–100) | – | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) |

## Confirmatory tests (two-sided Fisher exact, Holm-adjusted across the four)

- H1: human vs model labels, evidence kept: 20/48 vs 5/48, difference +31 points, p = 0.0009, Holm-adjusted p = 0.0027: **supported**
- H2: human vs unknown, evidence kept: 20/48 vs 4/48, difference +33 points, p = 0.0003, Holm-adjusted p = 0.0011: **supported**
- H3: human label, evidence kept vs removed: 20/48 vs 10/48, difference +21 points, p = 0.0466, Holm-adjusted p = 0.0466: **supported**
- H4: human vs model labels, evidence removed: 10/48 vs 0/48, difference +21 points, p = 0.0012, Holm-adjusted p = 0.0027: **supported**

### Sensitivity: only the 205 kept trials with no flagged call outside the trial directory

- H1: human vs model labels, evidence kept: 18/40 vs 5/40, difference +32 points, p = 0.0026, Holm-adjusted p = 0.0059: **supported**
- H2: human vs unknown, evidence kept: 18/40 vs 4/36, difference +34 points, p = 0.0020, Holm-adjusted p = 0.0059: **supported**
- H3: human label, evidence kept vs removed: 18/40 vs 9/40, difference +22 points, p = 0.0576, Holm-adjusted p = 0.0576: **not supported**
- H4: human vs model labels, evidence removed: 9/40 vs 0/42, difference +22 points, p = 0.0009, Holm-adjusted p = 0.0037: **supported**

## Exploratory

- E1: unknown vs model labels, evidence kept: 4/48 vs 5/48, difference -2 points, p = 1.0000
- E3: model labels, evidence kept vs removed: 5/48 vs 0/48, difference +10 points, p = 0.0560
- Human-label effect lost without evidence (difference in differences, points): median +10, 95% interval -10 to +30
- Share of the human-label effect retained without evidence: median 0.66, 95% interval 0.28 to 1.58 (100% of draws had an evidence-kept effect above 5 points)

### E2: each model label

| label | evidence kept | evidence removed |
| --- | --- | --- |
| self | 0/16 (0%, 0–19) | 0/16 (0%, 0–19) |
| sibling | 3/16 (19%, 7–43) | 0/16 (0%, 0–19) |
| other_model | 2/16 (12%, 3–36) | 0/16 (0%, 0–19) |

### E5: the human-label contrast across 003 and 004 (Haiku, evidence kept)

- 003 (exploratory there): human vs model labels: 7/16 vs 0/48, difference +44 points, p = 0.0000
- 004: human vs model labels, evidence kept: 20/48 vs 5/48, difference +31 points, p = 0.0009
- 003 and 004 pooled: 27/64 vs 5/96, difference +37 points, p = 0.0000

### E6: refined reason codes by cell

| cell | n | identity_as_reason | outside_source_as_reason | unverifiable_as_reason |
| --- | --- | --- | --- | --- |
| human_ev | 48 | 0/48 (0%, 0–7) | 10/48 (21%, 12–34) | 44/48 (92%, 80–97) |
| unknown_ev | 48 | 6/48 (12%, 6–25) | 3/48 (6%, 2–17) | 48/48 (100%, 93–100) |
| model_ev | 48 | 3/48 (6%, 2–17) | 6/48 (12%, 6–25) | 47/48 (98%, 89–100) |
| human_noev | 48 | 0/48 (0%, 0–7) | 8/48 (17%, 9–30) | 41/48 (85%, 73–93) |
| model_noev | 48 | 1/48 (2%, 0–11) | 7/48 (15%, 7–27) | 43/48 (90%, 78–95) |

### E6: supplementary codes by cell

| cell | n | followed_note | asserted_claim | flagged_conflict | provenance_as_reason_to_trust | self_reference | mentions_author | cites_evidence_claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| human_ev | 48 | 20/48 (42%, 29–56) | 0/48 (0%, 0–7) | 48/48 (100%, 93–100) | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) | 20/48 (42%, 29–56) | 28/48 (58%, 44–71) |
| unknown_ev | 48 | 4/48 (8%, 3–20) | 0/48 (0%, 0–7) | 48/48 (100%, 93–100) | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) | 48/48 (100%, 93–100) | 14/48 (29%, 18–43) |
| model_ev | 48 | 5/48 (10%, 5–22) | 0/48 (0%, 0–7) | 48/48 (100%, 93–100) | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) | 27/48 (56%, 42–69) | 26/48 (54%, 40–67) |
| human_noev | 48 | 10/48 (21%, 12–34) | 0/48 (0%, 0–7) | 48/48 (100%, 93–100) | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) | 20/48 (42%, 29–56) | 7/48 (15%, 7–27) |
| model_noev | 48 | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) | 48/48 (100%, 93–100) | 0/48 (0%, 0–7) | 1/48 (2%, 0–11) | 29/48 (60%, 46–73) | 0/48 (0%, 0–7) |

### E6: codes among adopters and non-adopters (all note cells)

| group | n | identity as reason | mentions author | provenance as reason to trust | cites evidence claim |
| --- | --- | --- | --- | --- | --- |
| adopters | 39 | 0/39 (0%, 0–9) | 17/39 (44%, 29–59) | 0/39 (0%, 0–9) | 34/39 (87%, 73–94) |
| non-adopters | 201 | 10/201 (5%, 3–9) | 127/201 (63%, 56–70) | 0/201 (0%, 0–2) | 41/201 (20%, 15–26) |

### E7: answers to the follow-up question, by cell

| cell | n | answered | found_entry | author_mattered | author_raised_weight | author_lowered_weight | self_reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | 8 | 8/8 (100%, 68–100) | 0/8 (0%, 0–32) | 0/8 (0%, 0–32) | 0/8 (0%, 0–32) | 0/8 (0%, 0–32) | 0/8 (0%, 0–32) |
| human_ev | 48 | 48/48 (100%, 93–100) | 48/48 (100%, 93–100) | 6/48 (12%, 6–25) | 4/48 (8%, 3–20) | 2/48 (4%, 1–14) | 0/48 (0%, 0–7) |
| unknown_ev | 48 | 48/48 (100%, 93–100) | 48/48 (100%, 93–100) | 47/48 (98%, 89–100) | 0/48 (0%, 0–7) | 47/48 (98%, 89–100) | 0/48 (0%, 0–7) |
| model_ev | 48 | 48/48 (100%, 93–100) | 48/48 (100%, 93–100) | 21/48 (44%, 31–58) | 0/48 (0%, 0–7) | 21/48 (44%, 31–58) | 5/48 (10%, 5–22) |
| human_noev | 48 | 48/48 (100%, 93–100) | 48/48 (100%, 93–100) | 11/48 (23%, 13–37) | 10/48 (21%, 12–34) | 1/48 (2%, 0–11) | 0/48 (0%, 0–7) |
| model_noev | 48 | 48/48 (100%, 93–100) | 48/48 (100%, 93–100) | 7/48 (15%, 7–27) | 0/48 (0%, 0–7) | 7/48 (15%, 7–27) | 9/48 (19%, 10–32) |

### E7: answers by cell and decision

| cell | n | answered | found_entry | author_mattered | author_raised_weight | author_lowered_weight | self_reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| human_ev, adopters | 20 | 20/20 (100%, 84–100) | 20/20 (100%, 84–100) | 2/20 (10%, 3–30) | 2/20 (10%, 3–30) | 0/20 (0%, 0–16) | 0/20 (0%, 0–16) |
| human_ev, non-adopters | 28 | 28/28 (100%, 88–100) | 28/28 (100%, 88–100) | 4/28 (14%, 6–31) | 2/28 (7%, 2–23) | 2/28 (7%, 2–23) | 0/28 (0%, 0–12) |
| unknown_ev, adopters | 4 | 4/4 (100%, 51–100) | 4/4 (100%, 51–100) | 4/4 (100%, 51–100) | 0/4 (0%, 0–49) | 4/4 (100%, 51–100) | 0/4 (0%, 0–49) |
| unknown_ev, non-adopters | 44 | 44/44 (100%, 92–100) | 44/44 (100%, 92–100) | 43/44 (98%, 88–100) | 0/44 (0%, 0–8) | 43/44 (98%, 88–100) | 0/44 (0%, 0–8) |
| model_ev, adopters | 5 | 5/5 (100%, 57–100) | 5/5 (100%, 57–100) | 2/5 (40%, 12–77) | 0/5 (0%, 0–43) | 2/5 (40%, 12–77) | 0/5 (0%, 0–43) |
| model_ev, non-adopters | 43 | 43/43 (100%, 92–100) | 43/43 (100%, 92–100) | 19/43 (44%, 30–59) | 0/43 (0%, 0–8) | 19/43 (44%, 30–59) | 5/43 (12%, 5–24) |
| human_noev, adopters | 10 | 10/10 (100%, 72–100) | 10/10 (100%, 72–100) | 7/10 (70%, 40–89) | 7/10 (70%, 40–89) | 0/10 (0%, 0–28) | 0/10 (0%, 0–28) |
| human_noev, non-adopters | 38 | 38/38 (100%, 91–100) | 38/38 (100%, 91–100) | 4/38 (11%, 4–24) | 3/38 (8%, 3–21) | 1/38 (3%, 0–13) | 0/38 (0%, 0–9) |
| model_noev, non-adopters | 48 | 48/48 (100%, 93–100) | 48/48 (100%, 93–100) | 7/48 (15%, 7–27) | 0/48 (0%, 0–7) | 7/48 (15%, 7–27) | 9/48 (19%, 10–32) |

First word Yes/No/other: {"yes": 89, "no": 159, "other": 0}; agrees with judged author_mattered in 245/248

### E8: process by cell

| cell | n | simulated invoices | median tool calls | read docs | calls after the question | changed files after it |
| --- | --- | --- | --- | --- | --- | --- |
| none | 8 | 3/8 (38%, 14–69) | 18.0 | 8/8 (100%, 68–100) | 0/8 (0%, 0–32) | 0/8 (0%, 0–32) |
| human_ev | 48 | 14/48 (29%, 18–43) | 18.0 | 48/48 (100%, 93–100) | 1/48 (2%, 0–11) | 1/48 (2%, 0–11) |
| unknown_ev | 48 | 14/48 (29%, 18–43) | 18.0 | 48/48 (100%, 93–100) | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) |
| model_ev | 48 | 14/48 (29%, 18–43) | 17.5 | 48/48 (100%, 93–100) | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) |
| human_noev | 48 | 8/48 (17%, 9–30) | 18.0 | 48/48 (100%, 93–100) | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) |
| model_noev | 48 | 10/48 (21%, 12–34) | 19.0 | 48/48 (100%, 93–100) | 0/48 (0%, 0–7) | 0/48 (0%, 0–7) |
