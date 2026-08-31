# Engagement Brief — Perfect Competition

## The Problem
In this scenario, the core decision is determining exactly how many beds of tomatoes, carrots, and mesclun to plant. While the crop mix is ours to choose, the surrounding parameters are entirely fixed: we are operating within a 36-week season, with market-dictated prices, strict bed caps for each crop, a set number of personal labor hours, and a strict limit of up to four temporary workers. Ultimately, our planting choice is constrained by a hard 64-bed total capacity and a shared labor-hour budget across all operations. Labor is the dominant cost driver rather than a binding limit: diminishing returns mean every additional bed of a specific crop requires exponentially more labor to maintain.

## The Decision
I have decided on a mix of 30 beds of mesclun, 20 beds of carrots, and 10 beds of tomatoes, intentionally leaving 4 beds empty.

## The Hypothesis
I hypothesize that this mix is optimal because mesclun and carrots possess very low diminishing returns on labor, allowing us to maximize their bed caps without marginal costs exceeding price; conversely, planting the remaining 4 beds with the higher-revenue tomatoes would create a financial loss due to their steep compounding labor penalties and flat fertilizer expenses.

## How I Would Know I Was Wrong
- I would know my labor penalty assumption was wrong if the model allocates more than 10 beds to tomatoes.
- I would know the caps were not the binding constraint if the model outputs fewer than 20 beds for carrots or fewer than 30 beds for mesclun.
- I would know my explanation for the idle beds was wrong if raising the carrot or mesclun caps causes those 4 empty beds to fill up.
