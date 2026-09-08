# Specification — Marginal Analysis (Perfect Competition Case)

## Purpose
This model determines the profit-maximizing bed allocation across tomatoes, carrots, and mesclun within a strict 64-bed capacity limit. The optimization accounts for fixed market prices, hard per-crop caps, and a shared labor-hour budget subject to compounding diminishing returns. A secondary run tests the shadow price of the carrot and mesclun caps by raising them and re-solving.

## Inputs — The Named Contract

| Name | Value | Unit | Source |
|---|---|---|---|
| `TOMATO_PRICE` | 8,800 | $/bed | Case File |
| `TOMATO_BED_CAP` | 20 | beds | Case File |
| `TOMATO_BASE_LABOR` | 2.50 | hrs/week/bed | Case File |
| `TOMATO_FERTILIZER` | 880 | $/bed | Case File |
| `TOMATO_DIM_PCT` | 10 | % | Case File |
| `CARROT_PRICE` | 2,094 | $/bed | Case File |
| `CARROT_BED_CAP` | 20 | beds | Case File |
| `CARROT_BASE_LABOR` | 5/6 (0.8333...) | hrs/week/bed | Case File prints 0.833 (rounded); exact 5/6 used so profit hits the check figure to the dollar |
| `CARROT_FERTILIZER` | 440 | $/bed | Case File |
| `CARROT_DIM_PCT` | 2.5 | % | Case File |
| `MESCLUN_PRICE` | 2,700 | $/bed | Case File |
| `MESCLUN_BED_CAP` | 30 | beds | Case File |
| `MESCLUN_BASE_LABOR` | 1.25 | hrs/week/bed | Case File |
| `MESCLUN_FERTILIZER` | 880 | $/bed | Case File |
| `MESCLUN_DIM_PCT` | 1.25 | % | Case File |
| `WEEKS` | 36 | weeks | Case File |
| `TOTAL_BED_CAP` | 64 | beds | Case File |
| `FARMER_SALARY` | 50,000 | $/season | Case File |
| `FARMER_FIELD_SHARE` | 0.5 | share of time in field | Case File |
| `FARMER_HOURS` | 720 | hours | Case File |
| `FARMER_HOURLY_RATE` | `=FARMER_SALARY * FARMER_FIELD_SHARE / FARMER_HOURS` (≈34.72) | $/hour | Derived; Case File prints rounded $34.72 |
| `TEMP_WORKER_MAX_COUNT` | 4 | workers | Case File |
| `TEMP_WAGE` | 25,000 | $/worker | Case File |
| `TEMP_WORKER_HOURS` | 1,440 | hours/worker | Case File |
| `TEMP_WORKER_HOURLY_RATE` | `=TEMP_WAGE / TEMP_WORKER_HOURS` (≈17.36) | $/hour | Derived; Case File prints rounded $17.36 |
| `FIXED_COSTS` | 20,000 | $ | Case File |
| `CARROT_BED_CAP_ISOLATED` | 21 | beds | Shadow Price Run (Carrot +1) |
| `MESCLUN_BED_CAP_ISOLATED` | 31 | beds | Shadow Price Run (Mesclun +1) |
| `CARROT_BED_CAP_JOINT` | 24 | beds | Shadow Price Run (+4 cap) |
| `MESCLUN_BED_CAP_JOINT` | 34 | beds | Shadow Price Run (+4 cap) |

## Structure

The workbook is organized into distinct regions:

- **Inputs Region:** Houses the named contract table above, ensuring every baseline and scenario parameter is cleanly referenced by name rather than cell coordinates.
- **Cost & Labor Schedule:** Calculates compounding labor hours per bed for each crop using each crop's own base-labor and diminishing-returns rate.
- **Primary Optimization Region:** The baseline Solver setup, maximizing total profit subject to baseline bed caps (20/20/30), the 64-bed total capacity, and labor constraints.
- **Isolated Carrot Shadow Price Run:** A secondary model region incorporating the carrot-only cap increase (`CARROT_BED_CAP_ISOLATED` = 21, mesclun held at 30), re-solving to isolate the marginal profit delta for carrots alone.
- **Isolated Mesclun Shadow Price Run:** A tertiary model region incorporating the mesclun-only cap increase (`MESCLUN_BED_CAP_ISOLATED` = 31, carrot held at 20), re-solving to isolate the marginal profit delta for mesclun alone.
- **Joint Capacity Absorption Run:** A quaternary model region incorporating the joint raised caps (`CARROT_BED_CAP_JOINT` = 24, `MESCLUN_BED_CAP_JOINT` = 34) to test whether the 4 idle beds get absorbed when both caps are relaxed together; attribution across crops (if the result is a split) is addressed in Audit Findings, not assumed here.
- **Validation Rules Region:** Contains the acceptance tests below.

## Calculation Logic

**1. Labor Hours per Crop**
- $\text{TOMATO\_LABOR}(q_t) = q_t \times \text{TOMATO\_BASE\_LABOR} \times \text{WEEKS} \times (1 + \text{TOMATO\_DIM\_PCT})^{q_t}$
- $\text{CARROT\_LABOR}(q_c) = q_c \times \text{CARROT\_BASE\_LABOR} \times \text{WEEKS} \times (1 + \text{CARROT\_DIM\_PCT})^{q_c}$
- $\text{MESCLUN\_LABOR}(q_m) = q_m \times \text{MESCLUN\_BASE\_LABOR} \times \text{WEEKS} \times (1 + \text{MESCLUN\_DIM\_PCT})^{q_m}$

**2. Labor Aggregation & Cost Allocation**
- $\text{TOTAL\_LABOR\_HOURS} = \text{TOMATO\_LABOR}(q_t) + \text{CARROT\_LABOR}(q_c) + \text{MESCLUN\_LABOR}(q_m)$
- $\text{FARMER\_HOURS\_USED} = \min(\text{TOTAL\_LABOR\_HOURS}, \text{FARMER\_HOURS})$
- $\text{TEMP\_HOURS\_USED} = \max(0, \text{TOTAL\_LABOR\_HOURS} - \text{FARMER\_HOURS})$
- $\text{TOTAL\_LABOR\_COST} = (\text{FARMER\_HOURS\_USED} \times \text{FARMER\_HOURLY\_RATE}) + (\text{TEMP\_HOURS\_USED} \times \text{TEMP\_WORKER\_HOURLY\_RATE})$
- $\text{BLENDED\_LABOR\_RATE} = \dfrac{\text{TOTAL\_LABOR\_COST}}{\text{TOTAL\_LABOR\_HOURS}}$

**3. Total Fertilizer Cost**
- $\text{FERTILIZER\_COST} = (q_t \times \text{TOMATO\_FERTILIZER}) + (q_c \times \text{CARROT\_FERTILIZER}) + (q_m \times \text{MESCLUN\_FERTILIZER})$

**4. Total Revenue**
- $\text{REVENUE} = (q_t \times \text{TOMATO\_PRICE}) + (q_c \times \text{CARROT\_PRICE}) + (q_m \times \text{MESCLUN\_PRICE})$

**5. Profit (Objective Function)**
- $\text{PROFIT} = \text{REVENUE} - \text{FERTILIZER\_COST} - \text{TOTAL\_LABOR\_COST} - \text{FIXED\_COSTS}$

**Solver Model Constraints**
- $q_t + q_c + q_m \le \text{TOTAL\_BED\_CAP}\ (64)$
- $q_t \le \text{TOMATO\_BED\_CAP}\ (20)$
- $q_c \le$ the applicable carrot cap for the run in progress (20 baseline / 21 isolated / 24 joint)
- $q_m \le$ the applicable mesclun cap for the run in progress (30 baseline / 31 isolated / 34 joint)
- $\text{TEMP\_HOURS\_USED} \le \text{TEMP\_WORKER\_MAX\_COUNT} \times \text{TEMP\_WORKER\_HOURS}\ (5{,}760)$
- $q_t, q_c, q_m \ge 0$ and integer

## Conventions

- **Labor Consumption Order:** Field hours must draw from the farmer's personal allocation first (`FARMER_HOURS`, up to 720 hours) priced at `FARMER_HOURLY_RATE` (derived, ≈$34.72/hr). Only once personal hours reach capacity does the farm hire temporary labor (`TEMP_HOURS_USED`, up to 5,760 hours total across a maximum of 4 workers) at `TEMP_WORKER_HOURLY_RATE` (derived, ≈$17.36/hr).
- **Exact vs. Printed Rates:** `CARROT_BASE_LABOR`, `FARMER_HOURLY_RATE`, and `TEMP_WORKER_HOURLY_RATE` use exact values derived from the case's underlying facts (5/6 hrs/week/bed; salary × field share ÷ hours; wage ÷ hours) rather than the case table's rounded printed values (0.833; $34.72; $17.36). Using the rounded versions shifts season profit by a few dollars and fails the $42,762 acceptance test at ±$1 tolerance.
- **Cost Allocation Basis:** The income statement evaluates labor using a single, blended farm-wide rate (`BLENDED_LABOR_RATE = TOTAL_LABOR_COST / TOTAL_LABOR_HOURS`). Labor expense is treated as a unified farm-level resource rather than an individual crop-by-crop contract.

## Validation Rules & Acceptance Criteria

1. **q=1 Hand-Check:** One bed of tomatoes must require exactly $1 \times 2.50 \times 36 \times (1+0.10)^1 = 99.00$ hours of labor.
2. **Optimal Allocation Mix Check:** Baseline Solver run must return 10 tomato beds, 20 carrot beds, and 30 mesclun beds (60 beds planted, 4 idle).
3. **Season Profit Acceptance Test:** Total baseline profit must evaluate to $42,762 (±$1 tolerance).
4. **Marginal Cost Acceptance Test:** The marginal cost of the 11th tomato bed must equal $9,390.72 (±$1 tolerance), computed as $\Delta\text{Labor Hours} \times \text{TEMP\_WORKER\_HOURLY\_RATE} + \text{TOMATO\_FERTILIZER}$.
5. **Isolated Carrot Shadow Price Acceptance Test:** Profit delta from raising the carrot cap to 21 beds must equal approximately $352.
6. **Isolated Mesclun Shadow Price Acceptance Test:** Profit delta from raising the mesclun cap to 31 beds must equal approximately $246.
7. **Solver Robustness & Path Independence:** GRG Nonlinear executed from (0,0,0) and (20,0,0) must converge to the identical global optimum (10,20,30).
8. **Formula Integrity:** Every calculated cell must contain a live formula referencing named ranges — no hardcoded values.
9. **Error-Free Verification:** Zero error cells across the workbook (no `#REF!`, `#DIV/0!`, `#VALUE!`, or `#NAME?`).
10. **Constraint Checks:** All constraint audit cells evaluate TRUE and display green — total beds ≤ 64, per-crop allocations ≤ respective caps, temp labor hours ≤ 5,760.

## Outputs

| Output Name | Unit | Description |
|---|---|---|
| Baseline Optimal Mix ($q_t, q_c, q_m$) | beds | Profit-maximizing allocation under baseline caps |
| Baseline Total Beds Used | beds | Total beds planted vs. idle capacity |
| Baseline Total Labor Hours | hours | Farm-wide labor requirement |
| Baseline Blended Labor Rate | $/hr | Farm-wide total labor cost ÷ total labor hours |
| Baseline Net Profit | $ | Optimized season profit |
| Tomato 11th Bed Marginal Cost | $ | Incremental cost of the 11th tomato bed |
| Isolated Carrot Shadow Price | $ | Profit delta from raising carrot cap to 21 beds |
| Isolated Mesclun Shadow Price | $ | Profit delta from raising mesclun cap to 31 beds |
| Joint Capacity Absorption Profit | $ | Profit and bed-absorption delta under joint caps (24/34) |

## Audit Findings

**1. q=1 Hand-Check — Pass.** Tomato labor hours at q=1 compute to exactly 99.00 hours (`1 × 2.50 × 36 × (1+0.10)^1`), verified live in the Validation sheet against the workbook's own formula, not a pasted value.

**2. Farm Profit Lab Cross-Check — Pass, after correcting a real error.** The first pass at this check priced every marginal labor hour at the temp-worker rate ($17.36/hr) regardless of whether the farmer's 720-hour allocation was still available, giving $2,598.75 for tomato bed 1 and $4,311.48 for bed 5. Both were wrong: in a *standalone* schedule (tomatoes alone, no other crop competing for the farmer's time), those hours fall inside her untouched allocation and must be priced at `FARMER_HOURLY_RATE`, not the temp rate.

Corrected:
- Bed 1 (99.00 hrs, fully within the 720-hour farmer allocation): 99.00 × $34.7222 + $880 fertilizer = **$4,317.50**.
- Bed 5 (cumulative hours run from 527.08 to 724.73, crossing the 720-hour line mid-bed): 192.92 hrs at the farmer rate + 4.73 hrs at the temp rate + $880 fertilizer = **$7,660.83**.

This is the same mechanism that makes the bed-11 acceptance figure ($9,390.72) correct in the *full* 10/20/30 mix: there, the farmer's 720 hours are already exhausted by the rest of that production before tomato bed 11 is reached, so its entire marginal cost is priced at the temp rate. A standalone single-crop schedule and a mixed-portfolio marginal cost are different calculations that happen to share a rate table — conflating them is the error this check exists to catch.

**3. Solver Path Independence — Pass.** Baseline Primary run from (0,0,0) converges to (10, 20, 30), profit $42,761.66. Run again from (20,0,0) — an infeasible starting point on its own (20 tomato beds alone would need over 12,000 labor hours, far beyond the 6,480-hour total capacity) — re-optimizes back to the identical (10, 20, 30) global optimum. No alternate local optimum was found.

**4. Published Check Figures — Pass.**

| Check | Target | Actual |
|---|---|---|
| Optimal mix | 10 / 20 / 30 (60 beds, 4 idle) | 10 / 20 / 30 (60 beds, 4 idle) |
| Season profit | $42,762 (±$1) | $42,761.66 |
| Marginal cost, tomato bed 11 | $9,390.72 (±$1) | $9,390.72 |
| Isolated carrot shadow price | ≈$352 | $352.50 (cap raised to 21; profit $43,114.16) |
| Isolated mesclun shadow price | ≈$246 | $246.48 (cap raised to 31; profit $43,008.14) |

**5. Formula Integrity — Pass.** Every calculated cell in the Inputs, Model, Validation, and Outputs sheets contains a live formula referencing named ranges. The only plain (non-formula) values are the twelve Solver changing cells (`q_t, q_c, q_m` × four scenarios), which is correct — they are decisions, not calculations. No error cells (`#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`) are present.

**Additional finding — Joint Capacity Run.** With both caps raised together (carrot to 24, mesclun to 34), the optimizer uses **all 64 beds** — the 4 beds idle in the baseline mix fill completely, for a profit of $43,900.49 (+$1,138.83 over baseline). This empirically confirms the Stage 1 hypothesis: the carrot and mesclun bed caps, not their underlying economics, were what left those 4 beds idle. Because both caps were raised simultaneously, this run cannot say how the gain splits between the two crops individually — that attribution is exactly what checks 2 and the isolated shadow-price runs above answer instead.
