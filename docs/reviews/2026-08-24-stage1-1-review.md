<!-- PR TARGET: https://github.com/jenniferandrade0808/Jennifer-Andrade | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief · **97 / 100** (A+) · 2.43 / 2.5 pts

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/jenniferandrade0808/Jennifer-Andrade/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-08-31 against your revised brief. Your previous score was 90. Both things I asked for are in, and one of them you did better than I described.

| Criterion | Earned | Notes |
|---|---|---|
| Problem restated in your own voice | 29 / 30 | Up from 28, and the gain is one clause: "Labor is the dominant cost driver rather than a binding limit." That distinction is the one this case turns on and almost nobody states it. Labor never runs out — the farm has 6,480 hours available and the optimum uses about 5,277 — so labor does not stop you the way a bed cap stops you. It just gets more expensive, and it is the price of labor that eventually makes a bed not worth planting. Cost driver, not constraint. Getting that separation into the problem statement before modeling is the difference between a brief that frames the analysis and one that describes the scenario. |
| Hypothesis names a specific mix | 25 / 25 | 30 mesclun, 20 carrots, 10 tomatoes, with four beds deliberately empty and a stated reason for leaving them empty. Unchanged and still exactly what this criterion asks for. |
| Economic mechanism | 24 / 25 | Up from 23. The mechanism is correct and now carries the whole argument: low diminishing-return rates let carrots and mesclun run to their caps without marginal cost overtaking price, while tomatoes stop early because "steep compounding labor penalties and flat fertilizer expenses" catch the price first. Naming the fertilizer cost as flat is a detail most people miss — it means fertilizer cannot be what stops a crop, which narrows the mechanism to labor by elimination. The last point is the same one as before: you say the eleventh tomato bed would be a loss and the case gives you everything you need to show it costs about $9,390 against $8,800 of revenue. One line of arithmetic turns the claim into evidence. |
| Falsifiability and process | 19 / 20 | Up from 14, and this is the whole gain. Three conditions, each naming an observable and the claim it kills. The third one is a different species from the other two and worth pointing at: "I would know my explanation for the idle beds was wrong if raising the carrot or mesclun caps causes those 4 empty beds to fill up." That is not a prediction about the model's output — it is a designed experiment. You are proposing to change an input and watch a specific thing happen, which distinguishes two explanations that produce identical output under the original assumptions: either the beds are empty because nothing else is worth planting, or they are empty because the caps are in the way. Nothing else in this cohort's briefs separates two hypotheses that way. The remaining point is that none of the three carries a tolerance — "more than 10 beds to tomatoes" treats 11 and 18 as the same result, and they are not. |
| **Final** | **97 / 100** | earned on merit |

### What changed

Your previous brief had a good problem statement, a committed mix, and a correct mechanism, and no statement of what would show it wrong. That was the whole gap and it cost six points.

Your commit message names the revision precisely — "Stage 1 revision per feedback: separate labor as cost driver from binding constraint, add falsification conditions" — and you logged the session separately. That is the sequence the stage wants: a brief with a before and an after, both in the history, so Stage 3 can point at what you believed and when.

### What to carry into Stage 1.2

Your third falsification condition is a specification for a Solver run, and you should build it as one. The workbook has the carrot and mesclun caps as named inputs; raising them and re-solving is a two-minute experiment that answers a question you have already written down. The difference between the profit at the real caps and the profit at raised caps is the shadow price of the cap — what one more allowed bed of that crop would be worth — and it is exactly the number your condition is asking about.

One thing to decide before you build: put a band on the first condition. If the model returns 11 tomato beds, were you wrong? 13? Deciding now, while you cannot see the answer, is what makes the Stage 3 reflection worth writing.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
