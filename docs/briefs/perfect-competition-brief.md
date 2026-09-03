# Engagement Brief — Perfect Competition

## The Problem
In this scenario, the core decision is determining exactly how many beds of tomatoes, carrots, and mesclun to plant. While the crop mix is ours to choose, the surrounding parameters are entirely fixed: we are operating within a 36-week season, with market-dictated prices, strict bed caps for each crop, a set number of personal labor hours, and a strict limit of up to four temporary workers. Ultimately, our planting choice is constrained by a hard 64-bed total capacity. While labor gets increasingly expensive due to diminishing returns, it never actually runs out; it is the compounding price of labor—not a shortage of it—that eventually makes a bed not worth planting.

## The Decision
I have decided on a mix of 30 beds of mesclun, 20 beds of carrots, and 10 beds of tomatoes, intentionally leaving 4 beds empty.

## The Hypothesis
I hypothesize that this mix is optimal because mesclun and carrots possess very low diminishing returns on labor, allowing us to maximize their bed caps without marginal costs exceeding price; conversely, planting the remaining 4 beds with the higher-revenue tomatoes would create a financial loss. While fertilizer is a flat per-bed expense, the steep compounding labor penalties mean the 11th tomato bed would cost approximately $9,390 (the marginal extra labor hours priced at the temporary worker rate, plus the flat $880 fertilizer cost) to maintain against only $8,800 in revenue.

## How I Would Know I Was Wrong
- I would know my labor penalty assumption was wrong if the model allocates more than 13 beds to tomatoes. A variance of up to three beds means my crossover math was just slightly off, but an output of 14 or more indicates the compounding labor penalty does not bite anywhere near where I projected; with the crop capped at 20, reaching 14 means "stopping early" is no longer a fair description.
- I would know the crop caps were not the binding constraint if the model outputs fewer than 19 beds for carrots or fewer than 29 beds for mesclun. I added a strict one-bed tolerance here to account for integer noise, but any larger drop indicates the crop stopped on its own before the caps mattered.
- I would know my explanation for the idle beds was wrong if raising the carrot or mesclun caps in the model causes those 4 empty beds to fill up, showing the caps themselves forced the capacity to remain idle.
