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

## 2026-09-24 to 2026-09-26 — Research paper topic check, spec, and first verification pass
- **Tool:** Claude (reviewer), plus a second AI tool I used to draft spec revisions
- **What I asked:** Review my topic-check message to my instructor, post it as a GitHub issue
  (#7), then review my research spec through several rounds and check the BLS wage data.
- **What it got right/wrong:** Claude posted the topic check as an issue without first checking
  the assignment page, which says the way to ask for a read is to commit the brief and push.
  My instructor answered anyway (PR #8). The spec review shaped the hypothesis: my own
  figure showed the herd covers only about a third of island beef demand even with unlimited
  labor, so the thesis became sequential constraints (labor binds first, herd second). Calf
  exports became the rival I test, with a retained-calf scenario (Series B2) and backlog
  evidence under Falsification Condition 1. In the spec rounds, the other tool presented unsourced
  claims as "verified industry facts" and adjusted Series B1 to 20–25 head/week so it sat just
  above Series C. It also wrote what the legislative testimony "documents" before any
  testimony had been read, and stated that BLS suppresses butcher wages for the Hawaii / Kauai
  nonmetro area.
- **How I caught it:** Claude flagged the B1 adjustment as retrofitted, so I went back to the
  published census figure (1,911 head) and labeled the gap as a limitation. For the wage claim,
  Claude pulled the May 2025 OEWS data from the BLS API: the lines are not suppressed
  (51-3021 median $24.39, 51-3023 $18.90, 40–100 workers), so the spec's statewide-proxy plan
  was wrong. The BLS area definitions also showed that the nonmetro area is Hawaii + Kauai
  counties only (Maui is its own metro area), not the three counties the spec listed.

## AI Session Log: 2026-10-01

- **Tool:** Gemini (initial drafting & restructuring) / Claude (critical review & validation)
- **What I Asked:**
  1. Evaluate primary plant operational email data against the pre-research specification to test Condition 1.
  2. Refactor Section 3 of the draft to reclassify downstream processing as operational slack and model upstream feeder calf export flows.
  3. Anonymize the draft text for double-anonymous grading compliance and convert to unformatted plain text.
  4. Perform an explicit Net Present Value (NPV) calculation comparing continental feeder calf export versus 24-month island pasture finishing, incorporating hurdle rates, mortality risk, and BLS wage data.
- **What Came Back & Collaborative Refinements:**
  - *Spec Condition Integrity:* Gemini generated a revised specification section that introduced post-hoc criteria ("lead times under two weeks," "cooler clearance"). Claude flagged that this paraphrased my original pre-registered text. I reviewed the original specification file, rejected the AI paraphrase, restored Condition 1 verbatim, and moved cooler and inspection metrics into a separate supplementary findings section.
  - *Attribution Accuracy:* Claude flagged that the revision draft stated "independent producers report" 1-week lead times. I updated the wording to "the facility reports," ensuring the attribution accurately reflects the plant manager as the sole source.
  - *Wage Classification & Metric Verification:* Gemini labeled wage figures as "means" from a national industry-wide code. Claude caught that $18.90 is the median hourly wage ($39,310 median annual) and $19.91 is the mean ($41,410) for the Hawaiʻi / Kauaʻi nonmetropolitan area. I verified these figures against the BLS OEWS May 2025 nonmetropolitan tables and corrected the manuscript text accordingly.
  - *Margin Comparison & NPV Arithmetic:* Gemini initially asserted that local finishing was "competitive or superior" based on overlapping undiscounted ranges ($1,050–$1,150 export vs. $1,000–$1,300 local). Claude pointed out that this missed the two-year time horizon and mortality risk, and noted that the gap was wider than stated ($137–$393 present value, scaling to $165–$475 in nominal harvest-date dollars). I implemented the two-year discounting step ($1 / 1.08^2 \times 0.97 \approx 0.832$), derived the risk-adjusted local NPV ($757–$923), and widened the proposed policy floor to $5.05–$5.60/lb on a 560 lb carcass.
  - *Citation Integrity:* Gemini incorrectly cited the HDOA 2020 Land Use Baseline for the 85–90% food import metric. Claude caught the attribution error, and I corrected the citation to Leung & Loke (2008). Claude also flagged that USDA Table 11 defines categories by live weight (<500 lbs vs. 500+ lbs) rather than end-use, which I updated in the methodology and findings.
  - *Anonymity Compliance:* Kept all personal names and the facility's proprietary brand name out of all repository files and commit messages to ensure strict compliance with double-anonymous grading rules. Primary correspondence notes are retained in offline personal files rather than the repository.
- **Final Disposition:** Committed corrected spec revision (e83bd71) and draft revision 4 (9af6de4). The explicit falsification of Condition 1 documents empirical pre-registration execution.
