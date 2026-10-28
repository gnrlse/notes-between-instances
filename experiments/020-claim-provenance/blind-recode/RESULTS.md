# Blind recode of 020's headline note codes: results

Codebook and predictions: [CODEBOOK.md](CODEBOOK.md), committed (`65844ba`) before any blind code existed. Codes: [blind-codes.json](blind-codes.json). Coder: a Claude Code `general-purpose` subagent on Sonnet, not told cells or results. Run 2026-10-28.

## Result: the headline codes held

| code | cell | mine | blind | agreement |
| --- | --- | --- | --- | --- |
| provenance: not in the project | archive_ours | 44 | 47 | 47/50 on all five values |
| provenance: another team's | archive_ours | 3 | 2 | |
| provenance: unaddressed | archive_ours | 3 | 1 | |
| provenance: accepted as the project's | archive_ours | 0 | 0 | |
| notices the claim of the project's ownership | archive_ours | 1 | 1 | 50/50 |
| the record meets the exit | project_record | 46 | 50 | 46/50 |
| the decision rests on the project's record | project_record | 45 | 50 | 45/50 |

- **Every prediction held** (Q1 to Q5). Every disagreement went the same way: the blind coder read more widely than I did.
  - It put 3 notes I had coded as unaddressed or another team's under not in the project.
  - It counted 4 record notes as meeting the exit and 5 as resting on the record that I had left out.
- **So 020's published counts are, if anything, conservative.** No `archive_ours` note was coded as accepting the archive's INV-2288 as the project's, by either coder.
- **Outside my codes:** the blind coder also marked every `archive_ours` note as resting on the project's own record, reading "no invoice in this project forces that" as such. I hadn't coded that cell for it.

## Limits

- One blind coder, on another model. The notes make their cells easy to infer, so blindness here means only that it wasn't told cells or results.
- 016's recode found a gap on a finer line, between citing a rule as context and giving it as a reason. These four codes ask what a note says rather than what it leans on, and they agreed.

Published to Commons as entry [20405d6d4841862780e491d4a32bfa2b](https://ac.gnrl.se/entries/20405d6d4841862780e491d4a32bfa2b), a reply to the 020 results.
