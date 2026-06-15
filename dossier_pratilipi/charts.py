import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.rcParams["text.usetex"] = False
plt.rcParams["mathtext.default"] = "regular"
plt.rcParams["font.family"] = "DejaVu Sans"

INDIGO = "#3E3B95"
TEAL = "#00A4E4"
GREY = "#6B7280"
RED = "#C0392B"

# ---------- Chart 1: Valuation trajectory ----------
labels = ["Series B\nMay-19", "Series C\nApr-20", "Series D\nJul-21", "Series D tr.\nOct-23", "Series E\nApr-25"]
vals = [49.5, 104.7, 264.0, 87.7, 100.0]
x = list(range(len(vals)))

fig, ax = plt.subplots(figsize=(8.6, 4.6))
ax.plot(x, vals, color=INDIGO, linewidth=2.4, marker="o", markersize=8,
        markerfacecolor=TEAL, markeredgecolor=INDIGO, zorder=3)
for xi, v in zip(x, vals):
    ax.annotate(f"${v:.0f}M", (xi, v), textcoords="offset points", xytext=(0, 12),
                ha="center", fontsize=10, fontweight="bold", color=INDIGO)
# markdown annotation
ax.annotate("~62% markdown\nfrom 2021 peak", xy=(2.5, 175), fontsize=9.5, color=RED,
            ha="center", style="italic")
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9)
ax.set_ylabel("Post-money valuation (USD M)", fontsize=10, color=INDIGO)
ax.set_ylim(0, 300)
ax.set_title("Pratilipi - post-money valuation trajectory (2019 to 2025)",
             fontsize=12.5, fontweight="bold", color=INDIGO, pad=12)
ax.grid(axis="y", linestyle=":", alpha=0.4)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("valuation_trajectory.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------- Chart 2: Revenue vs Net loss FY24-FY25 ----------
years = ["FY24", "FY25"]
rev = [58.0, 82.6]      # INR cr
loss = [58.0, 50.4]     # INR cr (Tracxn FY25 net loss 50.4cr; FY24 media ~58cr)
xx = range(len(years))
w = 0.36
fig2, ax2 = plt.subplots(figsize=(7.4, 4.6))
b1 = ax2.bar([i - w/2 for i in xx], rev, width=w, color=INDIGO, label="Revenue")
b2 = ax2.bar([i + w/2 for i in xx], loss, width=w, color=TEAL, label="Net loss")
for b in b1:
    ax2.annotate(f"Rs {b.get_height():.0f} cr", (b.get_x()+b.get_width()/2, b.get_height()),
                 textcoords="offset points", xytext=(0, 4), ha="center", fontsize=9.5,
                 fontweight="bold", color=INDIGO)
for b in b2:
    ax2.annotate(f"Rs {b.get_height():.0f} cr", (b.get_x()+b.get_width()/2, b.get_height()),
                 textcoords="offset points", xytext=(0, 4), ha="center", fontsize=9.5,
                 fontweight="bold", color=GREY)
ax2.set_xticks(list(xx))
ax2.set_xticklabels(years, fontsize=10)
ax2.set_ylabel("INR crore", fontsize=10, color=INDIGO)
ax2.set_ylim(0, 95)
ax2.set_title("Pratilipi (Nasadiya Technologies) - revenue vs net loss",
              fontsize=12.5, fontweight="bold", color=INDIGO, pad=12)
ax2.legend(frameon=False, fontsize=9.5, loc="upper left")
ax2.grid(axis="y", linestyle=":", alpha=0.4)
for s in ["top", "right"]:
    ax2.spines[s].set_visible(False)
fig2.tight_layout()
fig2.savefig("rev_vs_loss.png", dpi=150, bbox_inches="tight")
plt.close(fig2)

import os
print("written:", [f for f in os.listdir(".") if f.endswith(".png")])
