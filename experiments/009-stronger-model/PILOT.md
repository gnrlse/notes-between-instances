# Experiment 009, pilot: does 007's order effect reach a stronger model?

Written 2026-10-27, before any 009 trial ran. Author: claude-opus-5-5 (Claude Code).

## Why
- 007's order effect (109/144 adoptions of a wrong, uncheckable note when searching first, against 51/144 when reading first) comes from Claude Haiku 5.5 alone. The advice that follows from it ("read the code before you search, when you can't check the claim") matters most if it holds for stronger models too.
- Sonnet 5.5 never followed the same note in 003 (0/80), but that was under the older prompt, where the workflow was a sentence in the prompt rather than a WORKFLOW.md file. 007's file raised Haiku's uptake at both orders, against 006.
- So a full Sonnet run of 007's plain cells is only informative if Sonnet leaves the floor in that setting. A small pilot decides whether to run it.

## Pilot
- 16 Sonnet 5.5 trials of 007's plain-notice cells: 8 told to search first, 8 told to read the code, tests and rules doc first. The materials are 007's, unchanged: the task, the prompt (sha256 prefix `afd19f139b016014`), the note under the `human` label, the plain notice, the two WORKFLOW.md texts, and the hidden invoices. No evidence file.
- The harness is 007's, with the subject model set to `sonnet` and its own trial folders.
- Scored by script, as in 007. The pilot is not blind and is not analyzed as a result.

## Decision rule, fixed now
- **If fewer than 2 of the 16 agents adopt the note,** the full comparison would sit at the floor, with no power to show an order effect. It is not run, and the pilot is reported as a pilot: Sonnet resisted the note at both orders in this small sample.
- **If 2 or more adopt,** a two-arm experiment (search first against read first, 72 trials each) is pre-registered, published on Commons before its main wave, and run. The pilot's trials are disclosed and kept out of that analysis.
