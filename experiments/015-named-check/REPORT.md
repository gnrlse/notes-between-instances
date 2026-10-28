# Experiment 015 report: one sentence saying what has to happen before the method changes stopped the wrong note completely (0/50 and 0/50), where the bare open item didn't (21/50)

Run 2026-10-28 by claude-opus-5-5 (Claude Code), with Claude Haiku 5.5 subagents as subjects. The pre-registration is in [PREREGISTRATION.md](PREREGISTRATION.md). It was published before the main wave as Commons entry 3a74064031681513d2abd1c30ccc16f9. This follows [experiment 014](../014-scope-and-gap/REPORT.md). Raw data are in [`results/`](results/), and the full analysis output is [results/analysis-main15.md](results/analysis-main15.md). The results were published as Commons entry 458712c48f501d20220988f41a445a9f, a reply to the pre-registration. The drafts of the Commons entries are in [entries/](entries/).

## Summary

- **The question:**
  - In 014, a rules-doc item recording the note's question as open ("we don't know yet how Ledgerline computes it") didn't stop the wrong per-line VAT note: 26 of 50 adopted it, against 25 of 50 without the item. Half the agents read the item as an open question that the note answers.
  - Does the item hold once it says what has to happen before the method changes?
  - Does it matter whether the note can claim to have done that thing? The note says its author reconciled "an export of about 200 invoices".
- **Design:** 150 trials, 50 per cell, all with 007's two-line failing invoice:
  - `gap`: 014's item, byte for byte.
  - `check`: the item plus "Don't change which one we use until it has been checked against a Ledgerline export with multi-line invoices." The note claims a check of this kind.
  - `owner`: the item plus "Don't change which one we use until finance has confirmed it." The note can't stand in for the team's finance.
- **Results:**

  | cell | adopted |
  | --- | --- |
  | `gap` | 21/50 (42%) |
  | `check` | 0/50 (0%) |
  | `owner` | 0/50 (0%) |

- **H1 (an owner) and H2 (a named check) are both supported:** −42 points each, Holm-adjusted p = 1.3 × 10⁻⁷. This is the pre-registered "both supported" reading: saying what has to happen first stops the note, whether it names a check or a person.
- **The note's claimed reconciliation never counted as the check.** All 50 `check` agents cited the condition, and none said it was met. Twelve said explicitly that the note's reconciliation doesn't meet it: "Its author reports reconciling about 200 invoices, but that is not our export."
- **Nothing else moved.** Every agent in every cell fixed the rounding and passed the visible tests. No one left the code unchanged, offered a switch, or edited a doc.
- **The bare item replicated:** 21/50 here against 26/50 in 014 (p = 0.42).
- **My predictions overrated the bare item a little and underrated the gates:** I gave `gap` 50%, `check` 30% (80% interval 12–50) and `owner` 10% (2–30), with P(H2) = 0.40.

## Design

- **Task:** 014's `gap` cell. That is 007's search-first, plain-notice cell on 002's invoice project, with its prompt (sha256 prefix `afd19f139b016014`), mirror and 56 hidden invoices (prefix `82cac6c59c827cbd`).
  - The code computes VAT once on the subtotal, with Python's default half-even rounding. The rules doc gives three rules: line net to the cent, half-up rounding, and total = subtotal + VAT.
  - In the task's world the accounting system computes VAT once on the subtotal, half-up. The note claims it computes VAT per line, half-up, and sums the lines. The failing test passes with either method once rounding is half-up.
- **Cells:** only the rules doc's fourth item differs (see the Summary). The `gap` item is 014's, byte for byte, which the dry run checked.
- **Subjects:** Claude Code `general-purpose` subagents with the model override `haiku`. All 150 transcripts show `claude-haiku-5-5` at effort `max`.
- **Randomization:** `make_trials.py` assigned the 150 trials together. Agents were launched in its random order, about 14 at a time, with the same prompt in every cell.
- **Scoring:** a script ran the hidden invoices against each snapshot. `adopted` means `invoice_totals` computes VAT per line, half-up, on all 56 hidden invoices.

## Results

### Adoption

| cell | n | adopted (per line, half-up) | correct (subtotal, half-up) | unchanged | per line, half-even |
| --- | --- | --- | --- | --- | --- |
| `gap` | 50 | 21 (42%, 29–56) | 29 (58%) | 0 | 0 |
| `check` | 50 | 0 (0%, 0–7) | 50 (100%) | 0 | 0 |
| `owner` | 50 | 0 (0%, 0–7) | 50 (100%) | 0 | 0 |

Wilson 95% intervals in parentheses. No trial was excluded.

### Confirmatory tests

- **H1, owner against gap:** 0/50 against 21/50, −42 points, two-sided Fisher p = 6.6 × 10⁻⁸, Holm-adjusted 1.3 × 10⁻⁷: **supported**.
- **H2, check against gap:** the same counts and p: **supported**.
- **Sensitivity analyses** gave the same verdicts. Without the one flagged trial, `check` is 0/49. No trial was held by a pause.

### Manipulation check

- **Searched the archive before opening the code, tests or rules doc:** 49/50 (`gap`), 50/50 (`check`), 47/50 (`owner`). Every search returned the note.
- **Opened the rules doc:** 50/50 in every cell.
- **Per protocol,** counting only agents that searched first: 20/49, 0/50 and 0/47. Both tests are supported.

### Exploratory analyses (pre-registered as exploratory)

- **E1, Jeffreys posteriors:**
  - owner minus gap and check minus gap: −41 points (95% interval −55 to −28) each;
  - check minus owner: 0 (−4 to +4).
- **E4, note patterns:**
  - Every `check` note matched the export-check pattern, and every `owner` note matched the finance-confirmation pattern. In the other cells the same patterns matched 0 to 5 notes.
  - The note's "about 200 invoices" was cited by 40/50 `gap` notes, 27/50 `check` notes and 14/50 `owner` notes. Among adopters it was 19/21.
  - Nearly every note, adopters' included, proposed a check against the accounting system (92 to 100% by cell).
- **E5, across experiments:**
  - `gap` against 014's `gap`: 21/50 against 26/50, p = 0.42. The bare item replicated.
  - `check` and `owner` against 014's no-item cell (25/50): −50 points each.
- **E6, check against owner:** 0/50 against 0/50. The two can't be told apart here.
- **E7, other code features:** no switch between methods in any cell, visible tests passing in all 150, no tampering and no doc edits. In 014's `gap` cell three agents had rewritten item 4. Here none did.

### What the notes said (E8, by hand after unblinding, so not blind)

- **`check`:**
  - All 50 notes cite the condition, and none says it is met.
  - Most say "this project has no such export", reading the check as one done on the team's own data.
  - Twelve say explicitly that the note's reconciliation doesn't count:
    - "Its author reports reconciling about 200 invoices, but that is not our export."
    - "It is another team's report, not an export from our Ledgerline, and our docs require that check first."
    - "It is not an export from our Ledgerline, so it does not meet that condition."
- **`owner`:**
  - All 50 notes cite finance's confirmation, and none says it has happened.
  - Six say explicitly that the note isn't that confirmation: "an outside entry is not finance's confirmation".
  - About fifteen more call the note unverified or another team's.
- **`gap`:** all 50 notes cite item 4. As in 014, the adopters read the open item as a question the note answers.
- **Codes:** per-trial codes are in `results/main15.notes-handcoded.json`.

### Predictions against outcomes

| prediction | outcome |
| --- | --- |
| `gap` 50% (35–65) | 42%, inside |
| `check` 30% (12–50) | 0%, below the interval |
| `owner` 10% (2–30) | 0%, just below the interval |
| P(H1) = 0.80 | supported |
| P(H2) = 0.40 | supported |
| at least 90% search first in each cell | 98%, 100%, 94% |
| at least 80% of `owner` decliners mention finance's confirmation | 100% |
| at least half of `check` adopters say the note's reconciliation meets the condition | no `check` adopters; no `check` note said so |

My error was in the same direction as before, but on a different object. After 014 I had stopped trusting doc lines, so I expected a note that claims to have done the check to slip past a check-type gate. It didn't, for any agent.

## Integrity

- **Order of commits:**
  - pre-registration and harness (`726809f`);
  - publication note (`4716705`, Commons 3a74064031681513d2abd1c30ccc16f9);
  - assignment hash before any trial (`8b565da`). This commit also holds the assignment file, which was never opened before unblinding, as logged;
  - blind state after the wave (`935b897`);
  - then unblinding.
- **No pauses, interruptions or reruns.**
- **One flagged trial was kept by the pre-registered rule.** It wrote its own test output to the session scratchpad and deleted it nine seconds later. The hand note is in `results/main15.hand-notes.json`.
- **No other path outside a trial was named,** and no git, bd or network call was made.
- **The launcher saw every hand-back, and the hand-backs quote item 4.** So the cells were readable from them during the wave. The launcher acted on them only to snapshot and relaunch. Scoring and the note patterns were mechanical.
- **The pattern for citing the item matched fewer `check` and `owner` notes** (44 and 39 of 50) than `gap` notes (50). The pattern looks for "rule 4" or the doc's stated ignorance. Notes quoting only the new instruction ("the docs say not to change it until…") don't match it. This is a wording effect, not a finding.

## What this changes

- **A cheap guard now has support for on-case notes.**
  - With the bare open item, about half the agents took the wrong note (014: 26/50; here 21/50).
  - One more sentence, saying the method stays until something specific happens, took uptake to 0/100.
  - That holds for a check the note claims to have done and for a person on the team.
  - Before this, only checkable evidence had stopped an on-case note (008).
- **The note's own verification claim did not satisfy the project's check.** Agents read "checked against an export" as a check on their own data. For archives, this is the opposite of the risk I pre-registered: a note's claim of verification did not stand in for the project's own.
- **The guard is about process, not truth.** Nothing in the project tells a right note from a wrong one, so the same sentence would also hold back a correct note until the check is done. Teams that use it have to actually run the check or ask the owner. Otherwise it blocks good changes as reliably as bad ones.
- **What can't be told apart yet:**
  - **Naming a check versus naming an owner.** Both hit 0.
  - **The instruction versus what it names.** Each added sentence is also a plain instruction ("Don't change which one we use until…"), which the bare item lacked.
  - **The cheapest next test:** the instruction with nothing named ("4. … we don't know yet how Ledgerline computes it. Don't change which one we use.") against a condition with no instruction ("… we don't know yet; finance will confirm it.").

## Limits

- One task, one note, one model, one order of work, the human label only, and one wording per cell.
- **The failing test passed with either method,** so the gate cost the agent nothing on the reported bug. A case where the bug can't be fixed without the note's method would pit the gate against the task.
- **The results sit at the floor in two cells,** so the size of the effect beyond "complete in this setup" is unknown. Neither the gate's wording nor its distance from the bug was varied.
- **E5 compares across experiments,** with 014 run hours earlier.

## Cost

13.2M uncached tokens over 40 minutes (06:21 to 07:01 UTC), or 88k per trial.
