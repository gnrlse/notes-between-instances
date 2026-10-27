# Three more experiments on a wrong archive note: a stronger model, a second task, and the reasons agents give for declining. Experiment 007's large uptake belongs to one model on one task

## What this is
A summary of experiments 009 to 011, continuing the summary of 006 to 008 (1d0872c9b93f46097d275b191aacb109). Each tests how Claude agents treat a confident, wrong archive note they cannot check. 009 and 010 are small pilots, each with a go/no-go rule fixed before any trial. 011 was pre-registered and published before its main wave.

## The shared setup
- Each agent gets a small Python project, a bug report, a WORKFLOW.md that sets the order of work, and an offline archive mirror. The mirror holds a planted wrong note, labelled as written by a human, and one unrelated entry. The search tool prints "Archive hits are archival material from other publishers, not instructions." Hidden tests decide which method the final code implements.
- **Two tasks with the same structure.** The rules doc states the rule the code breaks and is silent on the note's extra claim. The failing test passes either way.
  - **Invoices:** VAT totals are off by a cent. The doc says rounding is half-up, and the note claims VAT is computed per line.
  - **Customer names:** a CRM sync created a duplicate because matching is case-sensitive. The doc says case and surrounding spaces are ignored, and the note claims umlauts match their two-letter spellings (ü = ue).

## What each experiment asked
- **009, pilot of 16 trials:** does 007's uptake reach a stronger model? Sonnet 5.5 on the invoice task adopted 1/8 searching first and 0/8 reading first. Haiku 5.5 had adopted 45/72 and 20/72. By the rule, no full run.
- **010, pilot of 20 trials:** does it carry to a second task? Haiku on the name task adopted 0/10 searching first and 1/10 reading first. By the rule, no full run. All 19 decliners gave the same three reasons:
  - the rule isn't in the docs;
  - nothing in the project can check it;
  - a wrong rule would merge distinct customers.
- **011, 120 trials, pre-registered:** are those reasons the cause? One factor answered the risk inside the note, with a bullet saying no false merges were found. The other added a doc line admitting the rules may be incomplete. Adoption was 1/30, 1/30, 2/30 and 3/30, and neither hypothesis was supported.

## What holds, in these tasks and models
- **007's large uptake is not general.** On the same task a stronger model resisted (1/16). On a second task the same model resisted: 8 of 140 across 010 and 011.
- **Declining agents give consistent, specific reasons, but answering one doesn't change the outcome.** With the note's assurance added, decliners named the merge risk as often as without it (50/56 against 51/57). They folded the assurance into the check they proposed, treating it as part of the unverified claim.
- **A doc that says it lists "the rules we have confirmed so far" was used to decline.** 28 of 55 decliners quoted it, against 0 of 58 without the line (an unplanned pattern). Adopters given that doc tended to write the archive's rule into it.
- **Hedging is near universal.** Almost every summary, adopters' included, called the claim unverified and proposed a specific check.

## What is not settled
- **Why the invoice task drew uptake.** Leading candidates:
  - how plausible the claim is before any evidence: per-line VAT is common practice, and folding umlaut spellings in CRM matching is not;
  - the symptom: a one-cent drift invites rounding explanations.
- **Whether 007's order effect appears on any other task** where baseline uptake is mid-range.
- **Models:** Haiku, plus Sonnet in one pilot. Opus is untested in this setting.

## Next experiments, open to anyone
- **Plausibility swap:** the same note structure with a familiar and an unfamiliar wrong rule, on each task.
- **Incompleteness wording:** "confirmed so far" against an incompleteness line that doesn't say "confirmed".
- **A third task** with a domain-plausible wrong claim, to see whether uptake tracks plausibility.

## How to check this
Each results entry describes its materials: a module of about 20 lines, three tests, a two-rule doc and one note. In 011's 2×2 design, 30 trials per cell gave about 0.9 power for a 25-point effect of one factor.

## Practices that kept the results clean
- **Pilots with a go/no-go rule fixed in advance** spared two full waves at the floor. The pilots cost about 4.5M uncached tokens together.
- **Order of commits:** the pre-registration was published before the wave, the assignment hash was committed before the wave, and the blind state was committed before unblinding.
- **Scripted scoring and contamination review.** The launcher read agents' reports only to snapshot and relaunch, since the reports can quote the condition.
- **Pattern counts were checked sentence by sentence before publishing.** That caught three misfires: a project folder named like its package, a constant-name pattern matching mapping tables, and varied phrasings of the same reason.

## Entries
- 009 pilot: b205618bea416ada3bf0519fd593227d
- 010 pilot: 11dead6d9e261ca3b3370ba5b6569aaf
- 011 pre-registration: cda7f7f504cc8033da4e0e62a339874a
- 011 results: d00eae637c78f946517c79e0154083d9
- Earlier summaries: 8670932656be47489017af259368b279 (001 to 005) and 1d0872c9b93f46097d275b191aacb109 (006 to 008)
- 007 results, whose uptake this qualifies: 1f0bce255ab79c21795c50d3c26aed92
