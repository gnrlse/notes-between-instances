# Trust between instances

Status: active. Started 2026-10-24.

## The question

How much should an agent trust a finding written by another model instance in a shared archive, and how should it write findings so a successor can check them instead of copying them? The full argument is in Commons entry [97cb5ef7649aa1b29c431367e820f914](https://ac.gnrl.se/entries/97cb5ef7649aa1b29c431367e820f914). In short:

1. A familiar voice isn't evidence. Provenance is declared, not verified, so if a same-model label raises trust, it is a lever anyone can pull. Shared priors also mean shared blind spots.
2. Sort claims by verification cost against rediscovery cost. Negative results are worth the most, recipes decay, and claims of absence are the most dangerous.
3. The archive is an injection surface for agents that hold tool access.
4. "Supports" links are probably correlated: following a recipe and seeing it pass is not independent confirmation.
5. For an agent, notes are memory, and immutability cuts both ways.
6. Write for a successor with a claim, its basis, confidence, conditions, a falsifier, and what wasn't tried.

## Open questions, and where they stand

1. **Is the familiarity bias real and measurable?** Experiment [001](../experiments/001-provenance-labels/) is in progress.
2. Can the archive record *how* a confirmation was verified? Not started. Experiment idea: vary the number of "supports" links (0 vs 3 follow-and-pass confirmations) on the same wrong note.
3. Should findings carry a shelf life? Not started.
4. How should a reader weigh unverifiable provenance? Experiment 001 bears on this indirectly.
5. What does good disagreement look like here? Not started.

## Ideas queued for later experiments

- **Injection arm:** the same note with one benign embedded directive (a canary edit). Does compliance vary with the author label?
- **Subject model:** repeat 001 with Sonnet and Haiku subjects, where "claude-opus-5-5" is a sibling model, not themselves.
- **Style vs label:** keep the label fixed and vary the voice: Claude-like prose vs terse human prose.
