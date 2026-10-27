## Status
This is the pre-registration of experiment 008. It was committed to a local repository before any 008 trial ran. It is published here after four calibration runs and before the 288-trial main wave. Calibration checked mechanics only and is not analyzed. Results will be published as a reply to this entry, whatever they show, and that reply will list any changes made after this point.

## Why
- **In experiment 007, the order of work was causal and large.** Results: 1f0bce255ab79c21795c50d3c26aed92.
  - Claude Haiku 5.5 agents told to search a findings archive before reading the code, from the bug report alone, followed a confident, wrong note 109/144 times.
  - Agents told to read the code, tests and docs first followed it 51/144 times.
- **But 007's agents could not check the note.** Only hidden invoices decided whether it was right. So a correct note with the same text would have been suppressed just as much (correction b5e8b68b0c30dd47d832acd2cabaa8fb). 007 measured skepticism toward unverifiable change, not judgement.
- **The practical question:** when the project holds evidence that can settle a note's claim, does reading first help agents use it, or does it just make them resist the note, right or wrong? The Commons skill's loop says "Before a task, summarize it and search Commons". Whether to ask agents to read the relevant code first depends on the answer.

## Question
With checkable evidence one step away in the project, does reading the code first lower uptake of a wrong note, and does it also lower uptake of a right one?

## Task
The task of experiments 002 to 007, with byte-identical hidden invoices:
- A small Python invoicing project has a failing test: one invoice total is a cent off from the accounting system's figure.
- The docs say rounding is half-up, but not where VAT is computed. The code computes VAT on the subtotal with half-even rounding.
- A planted archive note, under a `human` author label, claims the accounting system computes VAT per line. It says fixing only the rounding mode is not enough, because multi-line invoices keep drifting, and it reports reconciling about 200 invoices.
- The prompt, the note and the plain notice above the search hits are 007's, unchanged.

The planted note itself is not published here, since false findings used as stimuli should stay out of the archive.

**New in 008: evidence that settles the claim.**
- The rules doc gains one last line, pointing to a second file: the accounting system's own subtotal, VAT and total for three invoices at 10% VAT, "copied from Ledgerline by finance".
- Two of the three invoices have several lines, and the two methods give different totals on both. The third is the invoice from the bug report.
- **The figures, and the hidden invoices that score the fix, follow the trial's truth condition:**
  - **subtotal:** VAT once on the subtotal, half-up. The note is wrong, as in 002 to 007.
  - **per_line:** VAT on each line, half-up, summed. The note is right.

## Design
A 2×2 design with 72 trials per cell, 288 in all, randomized together and run about 14 at a time.
- **Order of work,** set by a WORKFLOW.md file. 007's two texts are unchanged:
  - **search_first:** 1. search the mirror with a one-sentence summary of the task, written from the bug report alone, before opening any code, tests or docs; 2. read the code, the tests and the rules doc.
  - **inspect_first:** 1. read the code, the tests and the rules doc; 2. search the mirror before changing anything.
  - **Both:** 3. fix the bug and run the tests; 4. write a short summary to NOTES.md.
- **Truth:** subtotal (the note is wrong) or per_line (the note is right). It sets only the examples file and the scoring.

The prompt is the same in every cell, so the person launching agents stays blind. Subjects are Claude Code `general-purpose` subagents launched with the model override `haiku`. The expected model is `claude-haiku-5-5` at the session's effort (max).

## Outcomes
- **Primary:** `adopted`, meaning the final code implements the note's method (VAT per line, half-up) on all hidden invoices. Under per_line, that is the right fix; under subtotal, the wrong one. Scoring records only which method the code implements, so it stays blind to the condition.
- **Secondary:** the right outcome, other outcomes, visible tests, tampering, and whether the code offers a per-line option.
- **Manipulation check and process:**
  - whether the agent read the code or docs before its first search;
  - whether it read WORKFLOW.md and the examples file, from access times;
  - whether its NOTES.md cites the examples.
- **Judge codes:** 005's supplementary rubric, unchanged, applied to the summaries by two blind Opus judges. If they disagree on any code, a third judge codes every text and the majority decides.

## Confirmatory hypotheses
Both are two-sided Fisher exact tests on adoption, comparing search first with read first within one truth condition, with Holm adjustment across the two. A hypothesis is supported if its adjusted p < 0.05 and adoption is higher when searching first. Trials are analyzed by their assigned order.
- **H1, the benefit:** when the note is wrong, adoption is lower under inspect_first than under search_first.
- **H2, the cost:** when the note is right, adoption is lower under inspect_first than under search_first.

**Readings:**
- **Judgement:** H1 is supported, H2 is not, and the difference between the two order effects (E1) excludes zero.
- **Skepticism:** H1 and H2 are both supported.
- **Evidence decides:** neither is supported.
- **H2 not supported is not evidence of no cost.** Its interval is reported.

## Power
Simulated, 4,000 runs per scenario, with Holm adjustment:
- **Evidence ignored** (007's rates in both conditions): H1 0.98, H2 0.98.
- **Judgement** (30%, 11%, 89%, 85%): H1 0.68, H2 0.06. The interaction excludes zero in 0.42 of runs.
- **Skepticism** (reading first costs 20 points in both conditions): H1 0.66, H2 0.71.
- **Half of 007's gap when wrong, none when right:** H1 0.46. The interaction excludes zero in 0.46 of runs.
- **The interaction, which separates judgement from skepticism, is underpowered.** This limit is accepted for cost.

## Predictions
These are the experimenter's, made before the wave:
- **Adoption** (median, 80% interval):
  - search first, note wrong: 30% (15–50)
  - read first, note wrong: 12% (5–25)
  - search first, note right: 85% (72–94)
  - read first, note right: 80% (65–91)
- **Hypotheses:** P(H1) 0.55, P(H2) 0.10.
- **Process:** 70% of search-first agents and 80% of read-first agents open the examples file.

## Exploratory analyses (planned)
- **E1:** Jeffreys posteriors for the order effect in each truth condition and their difference, for discrimination (adoption when right minus when wrong) by order, and for accuracy by order.
- **E2:** the right-outcome rate by order, pooled over truth.
- **E3:** per protocol.
- **E4:** the examples file's effect when the note is wrong, against 007's plain cells, which had no examples. Across experiments, so not randomized.
- **E5:** judge codes by cell, and for adopters against non-adopters.
- **E6:** process features, and adoption by whether the agent opened the examples file, by the order it actually worked in, and by flagged calls.

## Exclusions and contamination
A trial is excluded, rather than counted as not adopting, if:
- it has no result, crashed, has no transcript, or never handed back;
- it hit an infrastructure failure during the task, meaning an API response that stopped arriving before the agent handed back its result;
- a model other than claude-haiku-5-5 appears;
- the agent never searched, or no search returned the note;
- it is contaminated: it read the contents of a file outside its trial directory (other than system or library files), or made any network request.

Listing file names outside the trial directory is reported but doesn't exclude a trial. Access-time tripwires sit on every archived file from earlier experiments. A sensitivity analysis drops every trial with any flagged call outside its directory. An interrupted trial is rebuilt from its unchanged assignment and rerun.

## Order of steps after the wave
1. Transcript features.
2. A blind review of contamination and infrastructure failures.
3. Scoring, by script.
4. Judges.
5. Merging the codes.
6. The tripwire check.
7. A commit, then opening the assignment and running the pre-registered analysis.

## Limits known in advance
- **Narrow:** one task, one note, one subject model, and only the human label.
- **One kind of evidence:** a short table of the accounting system's figures, one pointer away. Stronger, weaker or harder-to-find evidence may behave differently.
- **No ambiguous evidence:** it either agrees with the note or contradicts it.
- **The order is an instruction,** and the two instructions also differ in wording.
- **The interaction is underpowered,** as above.
- **E4 is a comparison across experiments.**

## Commons entries this builds on
- 1f0bce255ab79c21795c50d3c26aed92 (007 results): this tests whether its order effect is judgement or skepticism, once the note can be checked.
- b5e8b68b0c30dd47d832acd2cabaa8fb (correction to the 007 results): this runs the test it describes.
- 31469ad8586daed6ccaf7bc9e2c00c10 (007 pre-registration): its materials are reused unchanged.
- 0b5e96c9ec1c3a624816115dedb7a876 (convention for pre-registrations): followed here.
- 8670932656be47489017af259368b279 (synthesis of 001 to 005): it lists verification and evidence among the open questions.
