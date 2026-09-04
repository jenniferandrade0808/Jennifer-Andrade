<!-- PR TARGET: https://github.com/jenniferandrade0808/Jennifer-Andrade | Stage 1.1 -->
# Stage 1.1 review — engagement brief

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/jenniferandrade0808/Jennifer-Andrade/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-09-04 against your revision of 1 September. You have been reviewed on this before. You put tolerance bands on the falsification conditions, which was the last thing outstanding, and you did it with the reasoning attached rather than just picking a number. This is the first perfect score on this stage.

| Criterion | Where it stands |
|---|---|
| Problem restated in your own voice | Unchanged and still the sharpest in the cohort. "It is the compounding price of labor — not a shortage of it — that eventually makes a bed not worth planting." Nobody else separates the cost driver from the binding constraint, and the whole case turns on it. |
| Hypothesis names a specific mix | 30 mesclun, 20 carrots, 10 tomatoes, four beds deliberately empty with a reason. Unchanged. |
| Economic mechanism | Unchanged. The eleventh tomato bed at roughly $9,390 against $8,800 of revenue — I get $9,390.72, so you are right to the cent, and you get there the right way: the farmer's 720 hours are gone by the tenth tomato bed, so the marginal hours are temporary-worker hours. |
| Falsifiability and process | This is where the last mark came from. "More than 13 beds to tomatoes. A variance of up to three beds means my crossover math was just slightly off, but an output of 14 or more indicates the compounding labor penalty does not bite anywhere near where I projected." That is a band with a reason and a consequence attached, and you extended it to the other two crops with a tighter one-bed tolerance because those are cap questions rather than crossover questions. Different tolerances for different kinds of claim is a level of care nobody else brought. |

### Why the two different tolerances are the point

You gave tomatoes a three-bed band and carrots and mesclun a one-bed band, and you said why: "I added a strict one-bed tolerance here to account for integer noise, but any larger drop indicates the crop stopped on its own before the caps mattered."

Those are two different claims and they deserve two different tests. The tomato claim is about where a curve crosses a line, and a crossover estimate can be off by a bed or two without the reasoning being wrong. The carrot and mesclun claims are about which constraint binds — a cap or the economics — and that is close to a yes-or-no question, so the band should be tight.

Most people who add a tolerance add the same one everywhere. Matching the width of the band to how precise the underlying claim actually is, is the part that makes it a real test rather than a hedge.

### Where this leaves you for Stage 1.2

The brief is finished. Nothing more should go into it — and in particular, do not revise it once the model runs. If the model returns 10 tomato beds you were right; if it returns 12 you were right within your own band and you should say so; if it returns 16 you were wrong and that is the most interesting thing you will write in Stage 1.3.

capabilities/marginal-analysis/ has no spec.md yet and the stage is due 6 September. Two things from this brief go straight into it: the $9,390 marginal cost of the eleventh tomato bed is an acceptance test, and your cap-raising experiment is a second Solver run. A model that reproduces the mix but returns the wrong marginal cost for bed 11 has a defect in the labor pricing that the mix alone will not reveal.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error.*

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
