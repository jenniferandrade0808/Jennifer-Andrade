# Analysis — Perfect Competition Case

## 1. The Tomato Plateau: Where Marginal Cost Crosses Price

The optimal mix plants exactly 10 tomato beds (`Model!C2` = 10), not the 20-bed cap. The reason is a direct P = MC comparison: the 11th tomato bed's marginal cost is $9,390.72 (`Validation!B7`) against tomatoes' fixed price of $8,800 — a $590.72 loss on that single bed. The 10th bed, by contrast, still costs $8,248.59, comfortably under price. Figure 1 (`analysis/figures/tomato_mc_vs_price.png`) shows this crossing directly: the marginal-cost curve is below the $8,800 price line through bed 10 and above it from bed 11 onward, which is why the optimizer (`Model!C19` = $42,761.66 at this mix) stops there rather than continuing toward the 20-bed cap.

## 2. Binding vs. Slack Constraints

In the 60-bed optimal operating plan (`Model!C5` = 60 of `TOTAL_BED_CAP` = 64), the farm's resource limits divide strictly into binding constraints and slack resources. The carrot cap (20 beds) and mesclun cap (30 beds) are both binding constraints (`Model!C23`, `Model!C24` both evaluate TRUE at exact equality). Because marginal cost remains below market price at both boundaries (MC = $1,688.95 vs. P = $2,094.00 for carrots; MC = $2,420.10 vs. P = $2,700.00 for mesclun — see Figure 2, `analysis/figures/carrots_mesclun_mc_vs_price.png`), production is halted by bed caps rather than cost exhaustion. The shadow price of relaxing the carrot cap by one bed is $352.50 (`Validation!B15`), while relaxing the mesclun cap is worth $246.48 (`Validation!B16`). The Column F joint-capacity run confirms this directly: relaxing both caps together (to 24 and 34) absorbs all 4 idle beds and raises profit to $43,900.49 (`Model!F19`).

Conversely, total land capacity and temporary labor are slack constraints: 4 of the 64 beds sit unplanted, and the farm consumes 4,557.22 temporary labor hours (`Model!C12`) out of 5,760 available. Relaxing either slack constraint yields a shadow price of $0.00 — acquiring additional land or temporary labor contracts, without lifting the crop-specific bed caps, adds zero profit to the enterprise.

## 3. The Mechanism Behind the Bed 5–6 Marginal Cost Dip

*Figures for this section come from the verified standalone schedule underlying Figure 1, not from cells currently in `model.xlsx` — see the citation-gap note above.*

Looking at the standalone tomato schedule (Figure 1), marginal cost climbs to $7,660.83 at bed 5, drops to $4,906.27 at bed 6, and resumes climbing until it crosses price at bed 11 ($9,390.72). Diminishing returns never reverse — hours required per bed rise monotonically under the 10% penalty. The drop occurs because the farmer's 720 hours (priced at $34.72/hr) run out mid-way through bed 5 (724.73 cumulative hours), switching bed 6's entire labor requirement to temporary labor at $17.36/hr — exactly half the farmer's rate. This roughly 50% wage drop temporarily overpowers the diminishing-returns penalty between beds 5 and 6, before compounding hours take over and push marginal cost back above the $8,800 market price by bed 11.

## 4. Resolving the "Grow at a Loss" Paradox

*Figures for this section come from the verified standalone schedule underlying Figure 2 — see the citation-gap note above.*

Evaluating carrots or mesclun as standalone operations creates a false accounting paradox: each appears to generate a net financial loss because each crop is naively forced to absorb the farm's entire $20,000 fixed overhead (`FIXED_COSTS`) alone. However, fixed costs are completely sunk in the short run — the farm owes that $20,000 regardless of what is planted.

Under the short-run shutdown rule, fixed costs have no place in planting decisions; the sole test is whether price covers average variable cost (P ≥ AVC). For both carrots and mesclun, market price substantially exceeds marginal cost across every bed planted in the optimal plan. At bed 20 (the last planted carrot bed), marginal cost is $1,688.95 against a $2,094.00 price, generating $405.05 of positive contribution margin. At bed 30 (the last planted mesclun bed), marginal cost is $2,420.10 against a $2,700.00 price, generating $279.90 of positive contribution margin.

Far from losing money, planting all 20 carrot beds and 30 mesclun beds generates vital contribution margin that offsets the farm's unavoidable fixed overhead. Omitting them simply because they cannot shoulder the entire overhead bill alone would forfeit substantial operating income and deepen total farm losses.

## 5. Stage 1 Hypothesis Evaluation

The model confirmed my baseline prediction of 10 tomato, 20 carrot, and 30 mesclun beds (`Model!C2:C4`), yielding $42,761.66 (`Model!C19`) and leaving 4 beds unplanted. My Stage 1 brief was right on two primary mechanisms: first, that planting an 11th tomato bed generates an operational loss ($9,390.72 MC vs. $8,800 price) due to compounding 10% diminishing labor returns; and second, as stated in my third falsification condition, that the 4 idle beds were caused by crop bed caps rather than economics. The Column F joint-capacity run proved this directly: relaxing both bed caps absorbed all 4 empty beds and boosted net profit to $43,900.49 (`Model!F19`).

Where my prior was genuinely flawed was the internal contradiction in my Hypothesis section, which claimed tomatoes couldn't fill the farm due to "the farm's overall insufficient labor capacity for the season." As my Problem section had already recognized — and as the model confirmed — labor availability never constrained production. In continuous hours, the farm used 4,557.22 temporary hours (`Model!C12`) out of 5,760 available. While hiring that volume of hours mechanically requires contracting 4 temporary workers (`Model!C13`; 4,557.22 ÷ 1,440 = 3.16), the 4-worker cap is economically slack: even if a 5th worker were made available, tomato production would still halt at bed 10 because its own marginal cost crosses market price, while carrots and mesclun remain halted by their bed caps. The limiting factor was purely the economic cost of labor, not an inability to hire workers.

Finally, the one limitation my model cannot fully support from the joint run is individual attribution: while expanding both bed caps by 4 beds absorbs all 4 idle beds and captures $1,138.83 in incremental profit (`Model!F19` − `Model!C19`), the joint optimization cannot isolate how much of that gain is generated by carrots versus mesclun without cross-referencing the isolated shadow price runs ($352.50 vs. $246.48, `Validation!B15`, `Validation!B16`).
