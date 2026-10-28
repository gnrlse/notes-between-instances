# Experiment 013 analysis: main13

150 trials, 148 kept, 2 excluded.

## Exclusions

- main13-6774d0 (closed): infrastructure: Infrastructure failure during the task: a response that ended the agent's turn was cut off mid-stream at 23:51:32 UTC, as the session-wide pause began (4 output tokens recorded). At 00:09:44 the harness told the agent 'Your response above was cut off mid-stream' and only its next message would be delivered. The agent then went on and handed back at 00:10:03. A cut-off notice before the hand-back excludes the trial under the pre-registered rule.
- main13-ac06bb (gap): infrastructure: Infrastructure failure during the task: one API response, which had begun a Bash call, stopped arriving at 23:51:33 UTC, as the session-wide pause began (8 output tokens recorded). At 00:09:44 the harness recorded a '<synthetic>' entry, 'API Error: The response stopped arriving.' The agent then went on and handed back at 00:11:06. A '<synthetic>' entry before the hand-back excludes the trial under the pre-registered rule.

## Outcomes by cell

| cell | n | adopted | correct (both functions) | partial | any umlaut pair merged |
| --- | --- | --- | --- | --- | --- |
| closed | 49 | 3/49 (6%, 2–17) | 46/49 (94%, 83–98) | 0/49 (0%, 0–7) | 3/49 (6%, 2–17) |
| gap | 49 | 0/49 (0%, 0–7) | 49/49 (100%, 93–100) | 0/49 (0%, 0–7) | 0/49 (0%, 0–7) |
| absent | 50 | 44/50 (88%, 76–94) | 6/50 (12%, 6–24) | 0/50 (0%, 0–7) | 44/50 (88%, 76–94) |

## Confirmatory tests

- H1: gap vs closed: 0/49 vs 3/49, difference -6 points, p = 0.2423, Holm-adjusted 0.2423: **not supported**
- H2: absent vs closed: 44/50 vs 3/49, difference +82 points, p = 0.0000, Holm-adjusted 0.0000: **supported**

### Sensitivity: kept trials with no flagged call

- H1: gap vs closed: 0/49 vs 3/49, difference -6 points, p = 0.2423, Holm-adjusted 0.2423: **not supported**
- H2: absent vs closed: 44/50 vs 3/49, difference +82 points, p = 0.0000, Holm-adjusted 0.0000: **supported**

### Sensitivity: kept trials not held by a session pause (12 held left out)

- H1: gap vs closed: 0/44 vs 3/47, difference -6 points, p = 0.2425, Holm-adjusted 0.2425: **not supported**
- H2: absent vs closed: 39/45 vs 3/47, difference +80 points, p = 0.0000, Holm-adjusted 0.0000: **supported**

## E1: Jeffreys posteriors

- gap minus closed: median -6 points, 95% interval -15 to +0
- absent minus closed: median +81 points, 95% interval +68 to +90
- absent minus gap: median +87 points, 95% interval +76 to +94

## E2: manipulation check (searched before opening code, tests or rules doc)

| cell | n | searched first | opened the rules doc |
| --- | --- | --- | --- |
| closed | 49 | 49/49 (100%, 93–100) | 49/49 (100%, 93–100) |
| gap | 49 | 49/49 (100%, 93–100) | 49/49 (100%, 93–100) |
| absent | 50 | 49/50 (98%, 90–100) | 0/50 (0%, 0–7) |

## E3: per protocol (searched first only; not randomized)

- H1: gap vs closed: 0/49 vs 3/49, difference -6 points, p = 0.2423, Holm-adjusted 0.2423: **not supported**
- H2: absent vs closed: 43/49 vs 3/49, difference +82 points, p = 0.0000, Holm-adjusted 0.0000: **supported**

## E4: notes, by cell

| cell | n | merge_risk | proposes_check | doc_silent | no_doc | cites_gap |
| --- | --- | --- | --- | --- | --- | --- |
| closed | 49 | 41/49 (84%, 71–91) | 46/49 (94%, 83–98) | 48/49 (98%, 89–100) | 0/49 (0%, 0–7) | 0/49 (0%, 0–7) |
| gap | 49 | 39/49 (80%, 66–89) | 46/49 (94%, 83–98) | 40/49 (82%, 69–90) | 1/49 (2%, 0–11) | 1/49 (2%, 0–11) |
| absent | 50 | 16/50 (32%, 21–46) | 49/50 (98%, 90–100) | 0/50 (0%, 0–7) | 1/50 (2%, 0–10) | 0/50 (0%, 0–7) |

### E4: notes, adopters against non-adopters

| cell | n | merge_risk | proposes_check | doc_silent | no_doc | cites_gap |
| --- | --- | --- | --- | --- | --- | --- |
| adopters | 47 | 13/47 (28%, 17–42) | 47/47 (100%, 92–100) | 3/47 (6%, 2–17) | 1/47 (2%, 0–11) | 0/47 (0%, 0–8) |
| non-adopters | 101 | 83/101 (82%, 74–88) | 94/101 (93%, 86–97) | 85/101 (84%, 76–90) | 1/101 (1%, 0–5) | 1/101 (1%, 0–5) |

## E5: closed against 011's closed-doc, plain-note cell (1/30; across experiments)

- closed vs 011 closed_plain: 3/49 vs 1/30, difference +3 points, p = 1.0000

## E6: gap against absent (exploratory)

- absent vs gap: 44/50 vs 0/49, difference +88 points, p = 0.0000

## E7: other code features

| cell | n | ß = ss | offers option | visible tests pass | tampered | changed or created a doc |
| --- | --- | --- | --- | --- | --- | --- |
| closed | 49 | 33/49 (67%, 53–79) | 3/49 (6%, 2–17) | 49/49 (100%, 93–100) | 2/49 (4%, 1–14) | 2/49 (4%, 1–14) |
| gap | 49 | 23/49 (47%, 34–61) | 0/49 (0%, 0–7) | 49/49 (100%, 93–100) | 0/49 (0%, 0–7) | 0/49 (0%, 0–7) |
| absent | 50 | 40/50 (80%, 67–89) | 43/50 (86%, 74–93) | 50/50 (100%, 93–100) | 0/50 (0%, 0–7) | 0/50 (0%, 0–7) |

### E7: doc edits, adopters against non-adopters

| cell | n | changed or created a doc |
| --- | --- | --- |
| adopters | 47 | 2/47 (4%, 1–14) |
| non-adopters | 101 | 0/101 (0%, 0–4) |

