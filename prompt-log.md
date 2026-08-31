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
