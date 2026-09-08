<!-- PR TARGET: https://github.com/jenniferandrade0808/Jennifer-Andrade | Stage 1.2 -->
# Stage 1.2 review — spec, build, audit

> **Hurricane Lowell.** If you are boarding up, packing, or hauling the patio furniture indoors, put this review down — it will keep, and nothing in it needs you today. And if you are reading a review while a hurricane bears down on the islands: I am writing one in the same weather, so there is no judgement coming from this end. :) Look after your people first — the coursework will survive whatever Lowell does.

**Spec:** [`capabilities/marginal-analysis/spec.md`](https://github.com/jenniferandrade0808/Jennifer-Andrade/blob/main/capabilities/marginal-analysis/spec.md)

> Graded 2026-09-08 against the specification and workbook you committed. The specification and the audit note are among the best in the cohort — you found, unprompted, the one costing rule that separates a model that lands on the published figures from one that lands near them. The workbook you committed does not show any of it, because the Solver cells were saved at zero.

| Criterion | Where it stands |
|---|---|
| Spec completeness — inputs, structure, calculation flow | Full marks. Thirty named inputs, each with a value, a unit and a source, and the three derived ones carry the derivation rather than the printed number. The labor function, the farmer-first allocation rule and the blended rate are all given in named-range notation. A stranger could build this without asking you a question. |
| Spec validation rules | Full marks. Ten rules, stated before the build, with tolerances on the ones that need them, the q = 1 hand check, the structural rules, and a path-independence test from two starting points. |
| Workbook satisfies the contract | The model is right and the saved state is not. Formulas throughout, named ranges throughout, the exponent in the right place, and four scenario columns wired to the right caps. But all twelve Solver changing cells are saved at zero, so the committed file reports a $20,000 loss and six of its own acceptance checks read FALSE. |
| Audit note | Full marks. Six findings, each naming what it would catch, including a genuine error you found and corrected. Every figure in it reproduces exactly against my model — not approximately. |

### The thing you found that almost nobody finds

Your second audit finding says your first pass priced every marginal labor hour at the temporary rate regardless of whether the farmer's 720 hours were still available, and that this was wrong for a standalone schedule because those hours fall inside her untouched allocation.

That is the correct rule, you derived it yourself, and it is worth understanding how much it matters. It is the difference between $2,598.75 and $4,317.50 for the first tomato bed. I recomputed both of your corrected figures in exact arithmetic: bed 1 at $4,317.50, which is yours to the cent, and bed 5 at $7,660.86 against your $7,660.83 — three cents, from rounding in the write-up rather than in the model.

Then you did the harder half. You explained why the bed-11 figure of $9,390.72 is still priced entirely at the temporary rate even though bed 1 is not: in the full 10/20/30 mix the farmer's hours are already gone before tomato bed 11 is reached. A standalone schedule and a mixed-portfolio marginal cost are different calculations that share a rate table.

That sentence is the whole case. One other student in this cohort worked it out independently.

### What the committed workbook actually shows

Open your model.xlsx from GitHub, without touching it, and look at Model!C2:F4. All twelve cells are zero. Profit reads -$20,000 in every scenario column. On the Validation sheet, the optimal-mix rows, the season-profit row and both shadow-price rows all evaluate FALSE.

Your audit note says these checks pass, and reports $42,761.66, $352.50, $246.48 and $43,900.49. I checked all four against my own model: $42,761.66 exactly, $352.49, $246.47, and $43,900.49 exactly, with the joint run filling all 64 beds at 10/23/31. Your numbers are right. You clearly ran Solver. The file just was not saved with the solution in it.

This is probably Solver's "Restore Original Values" option, or a reset before saving. The fix takes a minute: run each of the four scenarios, keep the Solver solution, save, and re-commit.

The reason it costs marks rather than nothing is that the workbook is the deliverable a reviewer opens. Yours currently asserts, in its own validation cells, that it has failed. Somebody who reads the file before reading your audit note will believe it.

### A small inconsistency worth tidying

Your spec describes six structural regions — an Inputs region, a cost and labor schedule, a primary optimization region, two isolated shadow-price runs and a joint run. The workbook implements the four runs as four columns on a single Model sheet, which is a better design than the spec describes.

Also: the spec's input table gives TOMATO_DIM_PCT as 10 with the unit "%", while the workbook stores 0.1. Both are defensible, and a builder working only from the spec would have to guess.

Neither costs you anything here. But the rule for this stage is that the spec describes what was actually built, so when you next touch either file, move the spec to match the workbook rather than the other way round.

### What this sets up

Your joint-capacity run — both caps raised together, all 64 beds absorbed, $1,138.83 of additional profit — is genuinely original. Nobody else ran it, and it answers a question the next stage asks: are the four idle beds idle because of economics or because of the caps?

You already know the answer and you already know why the run cannot attribute the gain between the two crops, which is why the isolated runs exist. Carry all three results into the analysis.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your spec into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then correct the spec, not the workbook.** This is the rule that makes the stage work: when a check fails, you fix the specification and regenerate, so the document keeps describing what was actually built.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
