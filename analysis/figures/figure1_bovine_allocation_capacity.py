"""Figure 1: Kaua'i weekly bovine allocation vs. inspected processing capacity.

Built from the figure specification of 2026-10-01. Census values are fixed;
the two plant values are parameters from the primary plant operational audit.
"""
import matplotlib.pyplot as plt

# Parameters (head per week)
calf_exports = 3707 / 52          # USDA 2022 Census, Table 11, calves <500 lb
cattle_500_plus = 1911 / 52       # USDA 2022 Census, Table 11, cattle incl. calves 500+ lb
observed_slaughter = 16.0         # plant audit: ~8 head Wednesday + ~8 head Saturday
plant_max_capacity = 25.0         # plant audit: realistic ceiling under existing infrastructure

OUT = "analysis/figures/figure1_bovine_allocation_capacity.png"

INK = "#1f1f1f"
INK_MUTED = "#5c5c5c"
GRID = "#e3e3e3"
CEILING = "#b3261e"

labels = [
    "Upstream Outflow:\nWeaned Calf Exports",
    "Cattle & Calves\n500+ lb Sold",
    "Current Plant\nThroughput:\nInspected Slaughter",
    "Theoretical Plant\nCapacity Ceiling",
]
values = [calf_exports, cattle_500_plus, observed_slaughter, plant_max_capacity]
colors = ["#d9775c", "#6b7785", "#2e6b3f", "white"]

plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"]})
fig, ax = plt.subplots(figsize=(8, 5.4), dpi=300)

x = range(len(values))
bars = ax.bar(x, values, width=0.62, color=colors, zorder=3)
cap_bar = bars[3]
cap_bar.set_edgecolor(CEILING)
cap_bar.set_linewidth(1.2)
cap_bar.set_hatch("///")

for bar, v in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 1.2, f"{v:.1f}",
            ha="center", va="bottom", fontsize=10, color=INK, fontweight="bold")

# Ceiling line across the throughput bars
left = bars[2].get_x() - 0.12
right = bars[3].get_x() + bars[3].get_width() + 0.12
ax.hlines(plant_max_capacity, left, right, colors=CEILING, linestyles="--", linewidth=1.6, zorder=4)
ax.text(right, plant_max_capacity + 4.5,
        f"Practical Processing Ceiling (~{plant_max_capacity:.0f} head/wk)",
        ha="right", va="bottom", fontsize=9, color=CEILING)

# Slack bracket on the current-throughput bar
slack = plant_max_capacity - observed_slaughter
bx = bars[2].get_x() + bars[2].get_width() + 0.06
ax.annotate("", xy=(bx, observed_slaughter), xytext=(bx, plant_max_capacity),
            arrowprops=dict(arrowstyle="|-|", color=INK_MUTED, lw=1.1, mutation_scale=4), zorder=5)
ax.text(bars[2].get_x() + bars[2].get_width() / 2, plant_max_capacity + 16,
        f"Midstream Slack Capacity\n= Plant Ceiling − Current Slaughter\n(~{slack:.0f} head/week unutilized)",
        ha="center", va="center", fontsize=8.2, color=INK,
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GRID, lw=0.8), zorder=6)

ax.set_title("Figure 1: Kauaʻi Weekly Bovine Allocation vs. Inspected Processing Capacity",
             fontsize=12, color=INK, pad=14)
ax.set_ylabel("Head of Cattle / Calves per Week", fontsize=10, color=INK)
ax.set_xticks(list(x))
ax.set_xticklabels(labels, fontsize=8.8, color=INK)
ax.set_ylim(0, max(values) * 1.22)
ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(INK_MUTED)
ax.tick_params(colors=INK_MUTED, length=3)

fig.text(0.01, 0.005,
         "Sources: USDA NASS 2022 Census of Agriculture, Table 11 (annual sales ÷ 52); "
         "plant values from primary operational audit (personal communications, Oct. 1–2, 2026).",
         fontsize=7, color=INK_MUTED, ha="left", va="bottom")

fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(OUT, dpi=300, bbox_inches="tight", facecolor="white")
print("saved", OUT)
