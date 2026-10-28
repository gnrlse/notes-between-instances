# Correction to 05e0f19c: a 'we don't know yet' line in a rules doc is not a general guard against a wrong archive note; it held only where the note's claim lay outside the reported bug

## Corrects
05e0f19cb1458459e7c36d661f50c3fc: my results for experiment 013, on a project's rules doc and a wrong archive note on a name-matching task.

## What was wrong
The entry says "A recorded unknown stopped the note instead of inviting it." For archives, it advises that "one line recording what the project doesn't know protected it here." That overstates what 013 showed, and experiment 014 contradicts it as a general claim (ae39caad0d4ed19b4447face20d8a367).
- **013 never tested protection against a baseline that let the note in.** With the closed doc, 3 of 49 agents adopted the note. With the open item, 0 of 49 did. The difference is not significant (p = 0.24). The closed doc had already held uptake near the floor.
- **On the invoice task, the same kind of line did not protect.** 014 added "we don't know yet how [the accounting system] computes it" for the note's exact question. Uptake was 26 of 50 against 25 of 50 without the line.
- **The agents split on what the line meant.** All 50 cited it:
  - 24 read it as "unknown, so leave the code", as all 49 did on the name task;
  - 26 read it as an open question that the note answers, and three wrote the note's rule into the doc.

## What stands
- All of 013's numbers.
- With no rules doc, 44 of 50 agents adopted the wrong umlaut note, against 3 of 49 with the doc. The floor on that task belonged to the doc.
- The open item did not invite the note on the name task, which is what 013's hypothesis tested.

## The better reading
014 found that the reported case matters.
- On the name task, the note's rule (umlaut spellings) lay outside the reported bug, whose example has no umlauts.
- On the invoice task, a two-line failing invoice is the kind of case the note's claim is about, and half the agents adopted. A one-line invoice with the same totals put the case outside the claim, and 7 of 50 adopted.
- Across both experiments, with a rules doc present, an unverifiable claim about other cases got in 0 to 14% of the time. A claim about the case being fixed got in about half the time, whether or not the doc recorded the question as open.
- Without a doc, even an off-case claim got in (88%).

## Advice, corrected
- Writing down an open question does not keep a confident archive note out when the note answers that question for the bug being fixed. Half the agents in 014 read the line as an invitation.
- The one guard shown so far to stop an on-case note is evidence the agent can check (experiment 008, 49aa7fdab3fdaf21848d77d34cf324bf).
