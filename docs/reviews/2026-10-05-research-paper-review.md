# Jennifer Andrade — feedback, sweep of 2026-10-05

This pull request answers #9.

## Research paper review — pre-deadline read

**What I read.** `analysis/research-paper.pdf` and its source `drafts/2026-10-02-draft.md` in full · `docs/briefs/research-brief.md` and `capabilities/economic-research/spec.md` in full, including the section "Specification Revision: Triggering of Condition 1" · the earlier drafts in your history · `analysis/figures/figure1_bovine_allocation_capacity.py` and Figure 1.

**What I did not open this pass.** Your Case 1 files · `AGENTS.md`, `CLAUDE.md`, `README.md` · `prompt-log.md`. If something in those changes an item below, say so and I will look.

---

Kauaʻi's beef is a great subject: local, live, with real prices in it and deeply personal for you and your family. You did the hardest thing a researcher does: you wrote down in advance what would make you change your mind. The plant interview gave you that evidence, and you changed the hypothesis and recorded why in the spec. The arithmetic in § 3.2 is shown in the text and it checks, from the $2,050 and $910–1,110 per head through the $2.41–2.77 per pound gap; so do the 66 percent export share and the roughly 13 percent of weekly throughput the plant's slack can absorb.

**Your brief still asks the old question.** Its opening paragraph says "The binding constraint is not pasture acreage or livestock head, but trained processing labor," while the paper concludes that "Kauaʻi's beef deficit begins upstream."

The spec carries the revision; only the brief's Planned Analysis was updated. Bring the brief's research-question paragraph in line with the spec's revision, or add a line there pointing to the spec section, so a reader (or AI) of the brief alone meets the question the paper answers.

- On github.com: open `docs/briefs/research-brief.md`, click the pencil icon, edit that paragraph, and commit the change.
- Or, in Claude Code or Codex opened to your portfolio repository: "Update the research-question paragraph of docs/briefs/research-brief.md so it matches the Specification Revision section of capabilities/economic-research/spec.md. I will write the new wording; show me the paragraph and the spec section side by side."

**Which constraint binds first?** § 3.1 calls the plant "a severe midstream bottleneck," and Figure 1 says the same. § 3.2 then opens "Because the facility operates with unutilized capacity, the primary supply constraint is upstream." Both cannot be the headline. As more calves are kept on-island, which limit does Kauaʻi hit first, and at what level of retention does the other one take over? Your own § 4.3 already notes that 13 percent retention uses up the plant's spare nine heads a week. Answer that once, and make § 3.1, § 3.2 and Figure 1 say it the same way.

**Show the three numbers the recommendation leans on, and compare the reserves on one unit.** The $1.79 million annual subsidy, the "~$4.14 per retail pound," and the 485,000-pound 30-day reserve appear in the paper with no calculation shown anywhere. The $4.14 depends on a retail yield per head that the paper never states. One line each, or an appendix row, makes them traceable.

Two questions sit in the same part of the paper. § 4.2 sizes the frozen reserve in pounds and days but not the "walking reserve": how many days of Kauaʻi's beef demand would the retained 1,236 head cover, so a reader can set the two side by side? And in § 3.2's Route B, does the $1,200–1,400 carrying cost include what that pasture could earn running cow-calf pairs instead?

Overall, I really enjoy this topic, and I hope this level of research and decision analysis continues after BUS-620: for your business, for the farming community on Kauaʻi, and possibly as evidence and argument for your local and state policymakers.

**In order:**

1. Bring the brief's research question in line with the spec revision.
2. Decide which constraint binds first as retention rises, and answer it the same way in § 3.1, § 3.2 and Figure 1.
3. Show the arithmetic behind the subsidy, the per-pound figure and the reserve; answer in the text how many days the walking reserve covers and whether Route B counts what the pasture could otherwise earn.

Closes #9
