"""Per-measurement-set cross-domain accuracy across the notebook iterations.

All numbers are read off the stored outputs of the shipped notebooks:
  baseline, non-overlapping windows (stride 340)
  SupCon frozen encoder + linear probe, same windows
  baseline, sliding window (stride 30)
  same sliding-window model, 4-antenna soft decision fusion
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SETS = ["S2", "S3", "S4", "S5", "S6", "S7", "Overall"]

SERIES = [
    ("baseline, non-overlapping", [45.5, 51.4, 48.5, 47.5, 48.1, 52.3, 48.2], "#0072B2"),
    ("+ SupCon linear probe",     [51.1, 59.7, 51.9, 52.9, 51.3, 58.2, 53.1], "#009E73"),
    ("baseline, sliding window",  [60.8, 61.6, 56.9, 57.4, 57.4, 64.0, 59.3], "#D55E00"),
    ("+ 4-antenna fusion",        [77.9, 75.2, 66.2, 66.0, 72.7, 70.9, 72.1], "#8C6BB1"),
]

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 7,
    "axes.linewidth": 0.6,
})

fig, ax = plt.subplots(figsize=(3.45, 1.62), dpi=400)

x = np.arange(len(SETS), dtype=float)
x[-1] += 0.35                      # small gap before the "Overall" group
w = 0.20

for k, (label, vals, color) in enumerate(SERIES):
    off = (k - 1.5) * w
    ax.bar(x + off, vals, width=w * 0.92, color=color, label=label,
           linewidth=0, zorder=3)

# separate the summary group from the per-set ones
ax.axvline((x[-2] + x[-1]) / 2, color="#CCCCCC", lw=0.6, zorder=1)

ax.axhline(20, color="#999999", lw=0.6, ls=(0, (3, 3)), zorder=2)

ax.set_ylabel("cross-domain accuracy [\\%]" if False else "cross-domain accuracy [%]")
ax.set_ylim(0, 90)
ax.set_yticks([0, 20, 40, 60, 80])
ax.set_xticks(x)
ax.set_xticklabels(SETS)
ax.set_xlim(x[0] - 0.55, x[-1] + 0.55)
ax.grid(axis="y", color="#DDDDDD", lw=0.5, zorder=0)
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_color("#888888")
ax.spines["bottom"].set_color("#888888")
ax.tick_params(length=2, width=0.5, colors="#444444")

ax.legend(ncol=2, fontsize=5.8, frameon=False, loc="upper center",
          bbox_to_anchor=(0.5, 1.30), handlelength=1.1, handleheight=0.8,
          columnspacing=1.2, borderaxespad=0.0)

fig.tight_layout(pad=0.3)
out = "/Users/francescovezzani/Desktop/Neural-Networks-Deep-Learning/Project/report/figures/perset_accuracy.png"
fig.savefig(out, bbox_inches="tight", pad_inches=0.02)
print("wrote", out)
