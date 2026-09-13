# Prompt Log

A running record of AI sessions that mattered — what I asked, what it got wrong, how I caught it.

## 2026-08-22 — Portfolio repo setup
- **Tool:** Claude
- **What I asked:** Help setting up the Stage 0 portfolio repo skeleton (AGENTS.md,
  CLAUDE.md, .gitignore, prompt-log.md, folder structure).
- **What it got right/wrong:** Claude built the Stage 0 skeleton correctly overall, but misplaced AGENTS.md, CLAUDE.md, .gitignore, and prompt-log.md inside docs/decisions/ instead of the repo root.
- **How I caught it:** I went back and checked its work myself and noticed some files were in the wrong folders.

## 2026-08-30 — Exploration sandbox for the marginal-analysis model
- **Tool:** Claude
- **What I asked:** Build a working Excel model of the farm decision so I could run
  Solver myself and see the mechanism before writing my Stage 2 spec.
- **What it got right/wrong:** It reproduced all four published check figures — season
  profit $42,761.66 against $42,762, q=1 tomatoes at 99 hours, standalone P=MC at
  10/10/6 beds, and tomato marginal cost of $8,248.59 at bed 10 rising to $9,390.72 at
  bed 11. Its first crossing-point formula was wrong: it took the last bed where
  marginal cost stayed under price instead of the last bed before marginal cost first
  exceeds price, returning 10/20/30. Because marginal cost does not rise monotonically
  in this model, that wrong formula still matched the tomato check figure while failing
  for carrots and mesclun. It also force-closed Excel while I had the workbook open,
  losing unsaved changes.
- **How I caught it:** Claude flagged the formula error itself when its output
  disagreed with the published standalone check figures. I kept the file outside the
  repository — it is not the Stage 2 deliverable, which has to be built from my
  committed spec, and its Assumptions sheet lists ten conventions the case never states
  that Claude chose on its own.

## 2026-08-30 — Stage 1 brief revision after feedback
- **Tool:** Claude
- **What I asked:** Run the labor-capacity arithmetic my instructor asked for, correct
  the labor sentence in both places it appeared, and help me write the "How I Would
  Know I Was Wrong" bullets.
- **What it got right/wrong:** The arithmetic held: capacity is 720 + (4 x 1,440) =
  6,480 hours, my predicted 10/20/30 mix needs about 5,277, and even an eleventh tomato
  bed still fits on four workers — so labor was never the binding constraint and the
  claim came out of both the Problem and Hypothesis sections. It refused to write the
  three falsification bullets and handed the question back to me four times. It
  corrected two things I had wrong on the way: fertilizer is flat per bed rather than
  subject to diminishing returns, and this model has no demand side, so a crop cannot
  "sell out."
- **How I caught it:** The three bullets are my own words; Claude
  only told me which of them could actually come out false.

## 2026-09-03 — Stage 1.1 tolerance bands and review response
- **Tool:** Claude
- **What I asked:** Help deciding whether to put a tolerance band on my first
  falsification condition, then review my revised brief and my replies to two review
  pull requests.
- **What it got right/wrong:** It laid out the trade honestly — a band buys robustness
  by giving up sharpness, and a wider target carries less information in the one section
  whose purpose is being killable — and I chose to decline the band. My instructor
  overruled that with a better argument: under "more than 10," an 11-bed result and an
  18-bed result falsify me identically, when one is a calibration error and the other
  means the mechanism is wrong. I conceded and set the band at more than 13, with a
  one-bed margin on the second condition for the near-optimal integer solutions GRG
  branch-and-bound can return. Claude caught three things in my drafts: I had deleted
  the "cost driver rather than a binding limit" clause that had just earned the rubric
  point, my band prose said "one or two beds" while my threshold allowed three, and a
  merged sentence in my pull request reply left the solver as the subject of "before
  concluding." It also inspected the review file the second pull request proposed to add
  and found it named a classmate, which is why I closed rather than merged.
- **How I caught it:** The band decision was mine both times — first to decline it, then
  to concede when the counter-argument beat my reason for holding out. I disclosed in
  both review threads that I had known the published check figures the whole time, so
  the bands were set on principle rather than as a blind calibration. I did not
  independently verify Claude's three flags; I took them at face value and made the
  edits.

## 2026-09-08 — Stage 1.2 workbook audit and Solver persistence fix
- **Tool:** Claude
- **What I asked:** My instructor's review found the committed workbook's decision cells
  at 0/0/0 despite my having run Solver — help resolve it and verify the fix.
- **What it got right/wrong:** My instructor's review caught that the committed workbook
  asserted its own failure — correct formulas, but decision cells all zero, almost
  certainly Solver's "Restore Original Values" or an unsaved solve. Claude proposed an
  independent Python brute-force search over the integer solution space so the fix
  could be verified without relying on the Excel GUI alone.
- **How I caught it:** I re-ran Solver myself, kept the solution this time, and
  confirmed the result matched both my instructor's recomputation and the brute-force
  script exactly across all four scenarios — Primary $42,761.66 (10/20/30), Isolated
  Carrot $43,114.16, Isolated Mesclun $43,008.14, Joint $43,900.49 (10/23/31) — before
  we committed.

## 2026-09-11 to 2026-09-13 — Stage 1.3 analysis, figures, and memo
- **Tool:** Claude
- **What I asked:** Assemble the analysis document, generate the two required figures,
  resolve the "grow at a loss" paradox, and draft the recommendation memo.
- **What it got right/wrong:** Claude generated the MC-vs-price figures and verified
  them against nine already-established check figures before plotting. My instructor's
  Stage 1.3 review then caught that my draft resolution of the "grow at a loss" paradox
  had tested marginal cost at the last bed rather than average variable cost across the
  whole block — the correct statistic for a shutdown decision. Separately, Claude caught
  an overstatement in my own rewritten conclusion, which implied AVC crossing price was
  what stopped production, when tomato actually stops on P=MC and carrots/mesclun stop
  on their bed caps.
- **How I caught it:** I independently recomputed the AVC figures myself (Carrot
  $1,918.45, Mesclun $2,430.74) rather than taking my instructor's numbers on faith,
  confirming both crops clear price on the correct test.

## 2026-09-13 — Stage 3 Reflection: AI Collaboration, External Review, and Verification

Across Stages 1.2 and 1.3, AI functioned effectively as a calculation engine and structural editor, but maintaining analytical precision required active verification at every handoff.

AI proved most valuable for technical execution: generating the Python brute-force script to evaluate the integer solution space and rendering high-resolution Matplotlib curves for analysis/figures/. Rather than accepting Solver outputs blindly, I used this script to verify each scenario's profit independently—confirming the $42,761.66 primary baseline, $43,114.16 for isolated carrots, $43,008.14 for isolated mesclun, and $43,900.49 for the 64-bed joint run.

However, the analysis required two critical conceptual corrections across human and machine review:
1. Marginal Cost vs. Average Variable Cost: In Section 4, my draft initially conflated marginal cost at the final bed with the shutdown rule. My instructor's Stage 1.3 review flagged that testing price against MC does not answer the shutdown question. Rather than accepting the feedback passively, I independently recomputed the variable cost schedules across the full blocks, verifying that Carrot AVC at 20 beds ($1,918.45) and Mesclun AVC at 30 beds ($2,430.74) both comfortably sit below price.
2. Economic Causation vs. Coincidence: In my redrafted conclusion, I inadvertently suggested that the optimal plan halted because AVC crossed market price. Claude caught this overstatement before commitment, pointing out that stopping points were dictated solely by the tomato P=MC crossing and physical bed caps, while the fact that AVC cleared price simply justified operating rather than shutting down.

This engagement demonstrated that while models excel at rapid computation, reconciling economic mechanisms across external feedback and automated drafting demands rigorous, independent auditing.
*(264 words)*
