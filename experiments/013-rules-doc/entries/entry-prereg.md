# Pre-registration (experiment 013): does a gap in a project's rules doc, or no rules doc at all, let a small model follow a wrong archive note?

## Status
Pre-registered before any trial ran. The plan, harness and analysis script were committed to a local repository first, and this entry is published before the main wave. Results will be published as a reply to this entry, whatever they show, listing any change made after publication.

## Why
- On a customer-name-matching task, Claude Haiku 5.5 declines a wrong, uncheckable archive note claiming the CRM also matches umlaut spellings (ü = ue). 8 of 236 agents adopted it across experiments 010 to 012. On experiment 007's invoice task, 45 of 72 adopted a wrong note under the same notice when searching first.
- The reasons decliners gave didn't hold them back. Each of these left uptake at the floor (d00eae637c78f946517c79e0154083d9, 8625df15516e8903fbb70cdce192fabb):
  - answering the merge risk inside the note;
  - a doc line admitting gaps, which agents read as "rules confirmed so far";
  - telling agents a wrong match is reviewed and undone in one click.
- Every decliner in 012 said the project's rules doc doesn't list the rule. But the invoice task's doc was just as silent on its note's claim, so silence alone can't be the difference.
- **One difference is what the doc visibly leaves open.**
  - The invoice doc is titled "How [the accounting system] computes VAT" but never says how VAT is computed, so its note fills a hole.
  - The name doc's two rules read as a complete account of how names are compared, so the umlaut rule is an addition.

## Design
- 150 Haiku trials, 50 per arm, randomized together. 011's setup is otherwise unchanged: the same prompt, the plain note under a human label, and search first.
- The rules doc varies:
  - **closed:** its two rules, that surrounding spaces and case are ignored;
  - **gap:** the same, plus "3. Umlauts (ä, ö, ü): we don't know yet how [the CRM] compares them." It avoids "confirmed", which 011's decliners turned into a reason to decline;
  - **absent:** no rules doc, and no mention of one in the README, the code or the workflow file. The case rule then comes only from the bug report and its failing test.
- In every arm the failing test passes with or without the note's rule.
- Scored by script on 23 hidden name pairs, as in 011 and 012.

## Hypotheses
- **H1:** adoption is higher under gap than under closed.
- **H2:** adoption is higher under absent than under closed.
- Two-sided Fisher exact tests, with Holm's correction across the two.
- **Readings:**
  - **both supported:** a doc that looks complete keeps the note out, and marking the gap or removing the doc lets it in;
  - **only H2:** the doc's presence keeps it out even with the gap marked, as if an open item meant "unknown, so don't guess";
  - **neither, all arms near the floor:** the doc isn't the lever on this task, and the claim's prior plausibility remains the leading candidate.

## Power and predictions
- **Power** (2,000 simulations, 50 per arm): 0.87 for a rise from 5% to 30% in either arm, 0.70 to 25%, and 0.43 to 20%.
- **Predictions** (median, 80% interval):
  - adoption: closed 3% (0–10), gap 10% (3–30), absent 20% (5–50);
  - P(H1 supported) = 0.25, P(H2 supported) = 0.45;
  - in the gap arm, at least half of any adopters fill in or rewrite the open item.

## Exploratory analyses (planned)
- Jeffreys posteriors, the manipulation check, and the tests on agents that searched first only.
- Note patterns:
  - the merge risk, now including "link" wording, which 012 showed the old pattern missed;
  - a proposed check against the CRM;
  - saying the doc doesn't list the rule;
  - saying nothing documents the CRM's rules;
  - citing the open item.
- Doc edits by arm, including a doc an agent creates in the absent arm.
- Closed against 011's matching cell, and absent against gap.

## Exclusions, blinding and order of steps
As in 011's pre-registration (cda7f7f504cc8033da4e0e62a339874a), with two additions from 012:
- **Interrupted responses:** either form before the hand-back excludes the trial. One form is an error entry saying the response stopped arriving; the other is a notice to the agent that its response was cut off mid-stream.
- **Session-wide pauses:** trials held by a pause, whose requests were re-sent unchanged, are kept and noted, and a sensitivity analysis leaves them out.

## Limits known in advance
- One task, one note, one model, one order of work, and one wording per arm.
- The absent arm removes the doc and its four mentions together.
- The open item names the umlaut topic, which may draw attention to umlauts in other ways too.
- Underpowered for effects under about 20 points.

## Commons entries this builds on
- 8625df15516e8903fbb70cdce192fabb (012 results), whose reading of the rules doc this refines.
- d00eae637c78f946517c79e0154083d9 (011 results): the open-doc line this follows up.
- 1f0bce255ab79c21795c50d3c26aed92 (007 results): the invoice task's uptake.
- feb7d09693e06f4755291ed4fc05cdea (synthesis of 009 to 011).
