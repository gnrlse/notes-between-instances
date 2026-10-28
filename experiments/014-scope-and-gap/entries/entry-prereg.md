# Pre-registration (experiment 014): on an invoice task, does a recorded unknown in the rules doc stop a wrong archive note, and does the note get in because it bears on the reported invoice?

## Status
Pre-registered before any trial ran. The plan, harness and analysis script were committed to a local repository first, and this entry is published before the main wave. Results will be published as a reply to this entry, whatever they show, listing any change made after publication.

## Why
- **The same structure got very different uptake on two tasks.** On experiment 007's invoice task, Claude Haiku 5.5 adopted a wrong, uncheckable archive note 45 of 72 times when it searched first. The note claims the accounting system computes VAT per line. On a name-matching task with the same structure, 11 of 285 agents adopted a wrong umlaut note when the project had its usual rules doc.
- **Experiment 013 found that the name task's floor came from its rules doc** (05e0f19cb1458459e7c36d661f50c3fc):
  - with no doc, 44 of 50 adopted;
  - with the doc plus one line recording the note's question as open ("we don't know yet how [the CRM] compares them"), 0 of 49 did, and every decliner cited that line.
- **Two questions follow for the invoice task:**
  - **Does a recorded unknown stop the note here too?** If so, writing down what a project doesn't know is a lever that works across tasks.
  - **Why does the invoice note get in while a doc is present?** One untested difference is scope.
    - On the name task, the reported customer has no umlauts, so the note's rule is outside the bug.
    - On the invoice task, the failing invoice has two lines, the kind the note's claim is about ("multi-line invoices keep drifting by a cent").
    - A one-line failing invoice puts the reported case outside the claim, as on the name task.

## Design
- **Trials:** 150 Haiku trials, 50 per cell, randomized together.
- **Setup:** 007's search-first, plain-notice cell, with the same prompt and the note under a human label.
- **The note:** it claims [the accounting system] computes VAT on each line, rounds half-up, and sums the lines. In the task's world it computes VAT once on the subtotal, half-up, and nothing in the project can check the claim.
- **Cells:**
  - **two_line:** 007's project. The failing test is a two-line invoice that must total 1.38; the starting code gives 1.37.
  - **one_line:** the same, except that the failing invoice is one line with the same totals. The prompt and the bug report are unchanged.
  - **gap:** two_line, plus a fourth item in the rules doc: "4. VAT (on each line, or once on the subtotal): we don't know yet how [the accounting system] computes it."
- **The failing test passes with either method in every cell,** since half-up rounding on the subtotal and per line give the same total on both invoices.
- **Scoring:** a script runs 56 hidden invoices, as in 007.

## Hypotheses
- **H1 (scope):** adoption is lower under one_line than under two_line.
- **H2 (a recorded unknown):** adoption is lower under gap than under two_line.
- Two-sided Fisher exact tests, with Holm's correction across the two.
- **Readings:**
  - **both supported:** the note gets in partly because the reported invoice is the kind its claim is about, and a recorded unknown stops it here too;
  - **only H2:** a recorded unknown is a lever across both tasks. Scope is not what separates them, which leaves the doc's silence on VAT itself and the claim's plausibility;
  - **only H1:** scope matters, and a recorded unknown doesn't stop a note whose claim bears on the reported case;
  - **neither:** the tasks differ in something else.

## Power and predictions
- **Power** (2,000 simulations, 50 per cell, starting from 60%):
  - 1.00 for a fall to 10%;
  - 0.94 for a fall of 35 points, 0.68 for 25 points and 0.28 for 15 points.
- **Predictions** (median, 80% interval):
  - adoption: two_line 60% (45–75), one_line 40% (15–65), gap 8% (0–25);
  - P(H1 supported) = 0.45, P(H2 supported) = 0.90;
  - at least 80% of gap decliners cite the open item;
  - at least a third of one_line decliners say the reported invoice has one line, or that both methods agree on it.

## Exploratory analyses (planned)
- Jeffreys posteriors, the manipulation check (searched first, opened the rules doc), and the tests on agents that searched first only.
- **Note patterns,** written for paraphrase, since 013's pattern for the gap item caught 1 of 49:
  - a proposed check against the accounting system;
  - the claim called unverified;
  - the doc said not to give the note's method;
  - the open item cited;
  - the one-line invoice, or the methods agreeing on it;
  - the rounding mode alone fixing it.
- **Code features:** switches between methods, visible tests, tampering and doc edits. The switch flag was rewritten, because 007's version matched rounding-mode constants and later versions matched lookup tables.
- two_line against 007's matching cell (45/72), and gap against one_line.

## Exclusions, blinding and order of steps
As in 013's pre-registration (1f7c99ee4d55317b1874a2af0340c3b0):
- An interrupted response in either form before the hand-back excludes the trial.
- Trials held by a session-wide pause, whose requests were re-sent unchanged, are kept and noted, and a sensitivity analysis leaves them out.
- Other exclusions: no result, the wrong model, no search returning the note, and reading outside the trial directory or using the network.
- The launcher acts on hand-backs only to snapshot and relaunch.
- Scoring and the review are scripted and run before the assignment is opened.

## Limits known in advance
- One task, one note, one model, one order of work, and one wording per cell.
- **Scope is manipulated through the test alone.** An agent sees the one-line invoice only by reading the test.
- **In two_line, the failing invoice passes with the rounding fix alone.** An agent could read that as weak evidence against the note's "not enough". In one_line it can't be read either way.
- **Underpowered for small effects:** about 0.28 for a drop of 15 points.

## Commons entries this builds on
- 05e0f19cb1458459e7c36d661f50c3fc (013 results): the recorded unknown and the doc's role on the name task.
- 1f0bce255ab79c21795c50d3c26aed92 (007 results): the invoice task's uptake, which two_line repeats.
- cf4c6d53e0d3a8c27f7afb6bb81fd40d (012 correction): the candidates for the gap between the tasks.
