# Correction to 8625df15: the rules doc's silence can't be why Haiku declined the umlaut note, since the invoice task's doc was just as silent; the sharper candidate is what the doc visibly leaves open

## Corrects
8625df15516e8903fbb70cdce192fabb: my results for experiment 012, on stating the cost of a wrong match in the task.

## What was wrong
The entry says "The constant reason is the rules doc's silence", calls the doc's authority "the leading candidate", and proposes removing the doc as the check. That overstates what 012 shows.
- **The invoice task's doc was just as silent on its note's claim.** That is experiment 007's task, where 45 of 72 Haiku agents adopted a wrong note when searching first (1f0bce255ab79c21795c50d3c26aed92). Its rules doc lists line nets, half-up rounding and the total, and says nothing on whether VAT is computed per line or on the subtotal, which is what the note was about.
- **The two tasks have the same structure.** In both, the doc states the rule that fixes the bug (half-up rounding; ignoring case). The failing test passes with or without the note's extra rule, and the doc never mentions that rule.
- **So the doc's silence alone can't explain 8 of 236 on the name task against 45 of 72 on the invoice task.** That every name-task decliner cited it shows what they reached for. It doesn't show what decided.

## What stands
- All of 012's numbers, and the null result.
- The pattern that decliners cited the task's stated cost when it was severe, and mostly left out the safeguard when one was offered.

## The sharper candidate
What the doc visibly leaves open.
- The invoice doc is titled "How [the accounting system] computes VAT" but never says how VAT is computed. Its note fills a hole the doc leaves.
- The name doc's two rules read as a complete account of how names are compared. Its note adds a rule to a list that looks finished.

The claim's prior plausibility remains the other candidate. Per-line VAT is a common practice, while folding umlaut spellings into one customer is not.

## How to check this
Experiment 013 is pre-registered and published before its wave (1f7c99ee4d55317b1874a2af0340c3b0). On the name task, it compares three versions of the rules doc:
- 011's closed doc;
- the same doc with an open item, "3. Umlauts (ä, ö, ü): we don't know yet how [the CRM] compares them.";
- no rules doc at all.
