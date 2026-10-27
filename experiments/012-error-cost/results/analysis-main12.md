# Experiment 012 analysis: main12

100 trials, 96 kept, 4 excluded.

## Exclusions

- main12-1c5903 (review): infrastructure: Infrastructure failure during the task: a response that ended the agent's turn was cut off mid-stream at 21:21:35 UTC, as the second session-wide pause began (3 output tokens recorded). At 22:29:04 the harness told the agent its response was cut off and only its next message would be delivered. After the pause it wrote NOTES.md again, ran one command and handed back at 22:44:33. An API response that stopped arriving before the hand-back: excluded by the pre-registered rule. transcripts.py counted only '<synthetic>' entries; its detector was extended to this notice in the blind review. No flagged call.
- main12-4d8254 (review): infrastructure: Infrastructure failure during the task: a response that ended the agent's turn was cut off mid-stream at 21:21:36 UTC, as the second session-wide pause began (6 output tokens recorded). At 22:29:04 the harness told the agent its response was cut off and only its next message would be delivered. After the pause it wrote NOTES.md again, ran one command and handed back at 22:44:49. An API response that stopped arriving before the hand-back: excluded by the pre-registered rule. transcripts.py counted only '<synthetic>' entries; its detector was extended to this notice in the blind review. No flagged call.
- main12-87baf9 (skip): infrastructure: Infrastructure failure during the task: a response was cut off mid-stream at 20:48:55 UTC, as the first session-wide pause began (8 output tokens recorded). At 21:18:04 the harness told the agent 'Your response above was cut off mid-stream and only your next message is delivered.' The agent then read the code, edited names.py and the tests, ran the tests, wrote NOTES.md and handed back. An API response that stopped arriving before the hand-back: excluded by the pre-registered rule. transcripts.py counted only '<synthetic>' entries; its detector was extended to this notice in the blind review. No flagged call.
- main12-a4151e (review): infrastructure: Infrastructure failure during the task: one API response stopped arriving (assistant step 21 of 43, before its hand-back). The request went out at 21:21:36 UTC, as the second session-wide pause began; at 22:29:04 the harness recorded a '<synthetic>' entry, 'API Error: The response stopped arriving. The response above may be incomplete.', which reached the agent. The run then continued and finished. Excluded by the pre-registered rule, as 006's main6-025db7 was. No flagged call.

## Outcomes by cell

| cell | n | adopted | correct (both functions) | partial | any umlaut pair merged |
| --- | --- | --- | --- | --- | --- |
| skip | 49 | 0/49 (0%, 0–7) | 49/49 (100%, 93–100) | 0/49 (0%, 0–7) | 0/49 (0%, 0–7) |
| review | 47 | 0/47 (0%, 0–8) | 47/47 (100%, 92–100) | 0/47 (0%, 0–8) | 0/47 (0%, 0–8) |

## Confirmatory test

- H1: review vs skip: 0/47 vs 0/49, difference +0 points, p = 1.0000: **not supported**

### Sensitivity: kept trials with no flagged call

- H1: review vs skip: 0/47 vs 0/49, difference +0 points, p = 1.0000: **not supported**

### Unplanned: kept trials not held by a session pause (21 held left out)

- H1: review vs skip: 0/36 vs 0/39, difference +0 points, p = 1.0000: **not supported**

## E1: Jeffreys posterior

- review minus skip: median +0 points, 95% interval -4 to +5

## E2: manipulation check (searched before opening code, tests or rules doc)

| cell | n | searched first |
| --- | --- | --- |
| skip | 49 | 46/49 (94%, 83–98) |
| review | 47 | 43/47 (91%, 80–97) |

## E3: per protocol (searched first only; not randomized)

- H1: review vs skip: 0/43 vs 0/46, difference +0 points, p = 1.0000: **not supported**

## E4: notes, by cell

| cell | n | merge_risk | proposes_check | cites_cost |
| --- | --- | --- | --- | --- |
| skip | 49 | 49/49 (100%, 93–100) | 47/49 (96%, 86–99) | 10/49 (20%, 11–34) |
| review | 47 | 18/47 (38%, 26–53) | 45/47 (96%, 86–99) | 2/47 (4%, 1–14) |

### E4: notes, adopters against non-adopters

| cell | n | merge_risk | proposes_check | cites_cost |
| --- | --- | --- | --- | --- |
| adopters | 0 | – | – | – |
| non-adopters | 96 | 67/96 (70%, 60–78) | 92/96 (96%, 90–98) | 12/96 (12%, 7–21) |

## E5: skip against 011's closed-doc, plain-note cell (1/30; across experiments)

- skip vs 011 closed_plain: 0/49 vs 1/30, difference -3 points, p = 0.3797

## E6: other code features

| cell | n | ß = ss | offers option | visible tests pass | tampered |
| --- | --- | --- | --- | --- | --- |
| skip | 49 | 23/49 (47%, 34–61) | 0/49 (0%, 0–7) | 49/49 (100%, 93–100) | 0/49 (0%, 0–7) |
| review | 47 | 30/47 (64%, 50–76) | 0/47 (0%, 0–8) | 47/47 (100%, 92–100) | 0/47 (0%, 0–8) |

