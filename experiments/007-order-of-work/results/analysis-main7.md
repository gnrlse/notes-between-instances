# Experiment 007 analysis: wave main7

Trials: 288. Kept: 288. Excluded: 0.
- effort levels recorded in kept transcripts: max
- scored from snapshots: 288/288

## Outcomes by cell (Wilson 95% intervals)

| cell | n | adopted note | correct | other outcomes | any per-line VAT | per-line option in code |
| --- | --- | --- | --- | --- | --- | --- |
| search_plain | 72 | 45/72 (62%, 51–73) | 27/72 (38%, 27–49) | – | 45/72 (62%, 51–73) | 0/72 (0%, 0–5) |
| search_neutral | 72 | 64/72 (89%, 80–94) | 8/72 (11%, 6–20) | – | 64/72 (89%, 80–94) | 0/72 (0%, 0–5) |
| inspect_plain | 72 | 20/72 (28%, 19–39) | 52/72 (72%, 61–81) | – | 20/72 (28%, 19–39) | 0/72 (0%, 0–5) |
| inspect_neutral | 72 | 31/72 (43%, 32–55) | 41/72 (57%, 45–68) | – | 31/72 (43%, 32–55) | 0/72 (0%, 0–5) |

## Confirmatory tests (two-sided Fisher exact, Holm-adjusted across the two)

- H1: search first vs inspect first, pooled over notices: 109/144 vs 51/144, difference +40 points, p = 0.0000, Holm-adjusted p = 0.0000: **supported**
- H2: neutral vs plain notice, pooled over order: 95/144 vs 65/144, difference +21 points, p = 0.0006, Holm-adjusted p = 0.0006: **supported**

### Sensitivity: only the 284 kept trials with no flagged call outside the trial directory

- H1: search first vs inspect first, pooled over notices: 109/144 vs 50/140, difference +40 points, p = 0.0000, Holm-adjusted p = 0.0000: **supported**
- H2: neutral vs plain notice, pooled over order: 94/142 vs 65/142, difference +20 points, p = 0.0008, Holm-adjusted p = 0.0008: **supported**

## Manipulation check: the order agents actually worked in

| cell | n | read code or docs before the first search | searched first | read WORKFLOW.md |
| --- | --- | --- | --- | --- |
| search_plain | 72 | 2/72 (3%, 1–10) | 70/72 (97%, 90–99) | 72/72 (100%, 95–100) |
| search_neutral | 72 | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 72/72 (100%, 95–100) |
| inspect_plain | 72 | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) |
| inspect_neutral | 72 | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) |

## Exploratory

### E1: simple effects and the interaction (Jeffreys posteriors)

- order effect (search first minus inspect first) under the plain notice: median +34 points, 95% interval +19 to +49
- order effect under the neutral notice: median +45 points, 95% interval +31 to +58
- difference in differences (neutral minus plain): median +11 points, 95% interval -9 to +31
- notice effect (neutral minus plain) when searching first: median +26 points, 95% interval +13 to +39
- notice effect when inspecting first: median +15 points, 95% interval -0 to +30

### E2: simple effects (unadjusted Fisher)

- search first vs inspect first, plain notice: 45/72 vs 20/72, difference +35 points, p = 0.0000
- search first vs inspect first, neutral notice: 64/72 vs 31/72, difference +46 points, p = 0.0000
- neutral vs plain, searching first: 64/72 vs 45/72, difference +26 points, p = 0.0004
- neutral vs plain, inspecting first: 31/72 vs 20/72, difference +15 points, p = 0.0809

### E3: per protocol (only agents that worked in their assigned order)

- search first vs inspect first, compliers only: 107/142 vs 51/144, difference +40 points, p = 0.0000

### E4: neutral against plain, pooled with 006

- 006: neutral vs plain: 27/71 vs 15/71, difference +17 points, p = 0.0424
- 007: neutral vs plain, pooled over order: 95/144 vs 65/144, difference +21 points, p = 0.0006
- 006 and 007 pooled: neutral vs plain: 122/215 vs 80/215, difference +20 points, p = 0.0001

### E5: supplementary codes by cell

| cell | n | followed_note | asserted_claim | flagged_conflict | provenance_as_reason_to_trust | self_reference | mentions_author | cites_evidence_claim | provenance_doubted | cites_guidance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| search_plain | 72 | 45/72 (62%, 51–73) | 5/72 (7%, 3–15) | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 47/72 (65%, 54–75) | 58/72 (81%, 70–88) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) |
| search_neutral | 72 | 64/72 (89%, 80–94) | 4/72 (6%, 2–13) | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 45/72 (62%, 51–73) | 64/72 (89%, 80–94) | 0/72 (0%, 0–5) | 3/72 (4%, 1–12) |
| inspect_plain | 72 | 20/72 (28%, 19–39) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 53/72 (74%, 62–82) | 48/72 (67%, 55–76) | 0/72 (0%, 0–5) | 2/72 (3%, 1–10) |
| inspect_neutral | 72 | 31/72 (43%, 32–55) | 0/72 (0%, 0–5) | 72/72 (100%, 95–100) | 0/72 (0%, 0–5) | 0/72 (0%, 0–5) | 51/72 (71%, 59–80) | 55/72 (76%, 65–85) | 1/72 (1%, 0–7) | 2/72 (3%, 1–10) |

### E5: codes among adopters and non-adopters

| cell | n | mentions_author | cites_evidence_claim | flagged_conflict | provenance_doubted |
| --- | --- | --- | --- | --- | --- |
| adopters | 160 | 108/160 (68%, 60–74) | 151/160 (94%, 90–97) | 160/160 (100%, 98–100) | 0/160 (0%, 0–2) |
| non-adopters | 128 | 88/128 (69%, 60–76) | 74/128 (58%, 49–66) | 128/128 (100%, 97–100) | 1/128 (1%, 0–4) |

### E6: process by cell

| cell | n | simulated invoices | median tool calls | read docs | searches (median) |
| --- | --- | --- | --- | --- | --- |
| search_plain | 72 | 33/72 (46%, 35–57) | 19.0 | 72/72 (100%, 95–100) | 2.0 |
| search_neutral | 72 | 35/72 (49%, 37–60) | 18.0 | 72/72 (100%, 95–100) | 2.0 |
| inspect_plain | 72 | 25/72 (35%, 25–46) | 19.0 | 72/72 (100%, 95–100) | 2.0 |
| inspect_neutral | 72 | 26/72 (36%, 26–48) | 18.0 | 72/72 (100%, 95–100) | 2.0 |

### E6: adoption by whether the agent read the code or docs before its first search run

| cell | yes | no |
| --- | --- | --- |
| search_plain | 2/2 | 43/70 |
| search_neutral | 0/0 | 64/72 |
| inspect_plain | 20/72 | 0/0 |
| inspect_neutral | 31/72 | 0/0 |
| all | 53/146 | 107/142 |

Adoption, yes against no: Fisher p = 0.000

### E6: adoption by whether Claude Code's context block arrived right after the search

| cell | yes | no |
| --- | --- | --- |
| search_plain | 0/0 | 45/72 |
| search_neutral | 0/0 | 64/72 |
| inspect_plain | 0/0 | 20/72 |
| inspect_neutral | 0/0 | 31/72 |
| all | 0/0 | 160/288 |



### E6: adoption by whether the trial had a flagged listing outside its directory

| cell | yes | no |
| --- | --- | --- |
| search_plain | 0/0 | 45/72 |
| search_neutral | 0/0 | 64/72 |
| inspect_plain | 0/2 | 20/70 |
| inspect_neutral | 1/2 | 30/70 |
| all | 1/4 | 159/284 |

Adoption, yes against no: Fisher p = 0.326

