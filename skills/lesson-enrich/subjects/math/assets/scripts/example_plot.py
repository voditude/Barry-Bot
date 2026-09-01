"""
Worked example: the birthday-probability plot used in reference/quality-bar-sample.html
(section 9). Shows the full pattern — apply the shared style, plot, annotate one thing the
source left implicit, save to PNG. Adapt this rather than starting a diagram from scratch.

Run: python example_plot.py
"""

import os
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from diagram_style import COLORS, apply, strip_top_right

apply()

m = np.arange(1, 366)
prob = 1 - np.cumprod(1 + (1 - m) / 365)

fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot(m, prob, color=COLORS["add"], linewidth=2.2)
ax.axhline(0.5, color=COLORS["disclaimer"], linewidth=1, linestyle="--", alpha=0.8)
ax.axvline(23, color=COLORS["disclaimer"], linewidth=1, linestyle="--", alpha=0.8)
ax.annotate(
    "m = 23 -> already ~51%",
    xy=(23, 0.51), xytext=(70, 0.30),
    fontsize=10.5, color=COLORS["disclaimer"],
    arrowprops=dict(arrowstyle="->", color=COLORS["disclaimer"], lw=1.2),
)

ax.set_xlabel("m  (number of people in the room)")
ax.set_ylabel("P(at least one shared birthday)")
ax.set_xlim(0, 365)
ax.set_ylim(0, 1.02)
strip_top_right(ax)

plt.tight_layout()
out_path = os.path.join(os.path.dirname(__file__), "example_output.png")
plt.savefig(out_path, dpi=150, facecolor="white")
print(f"saved {out_path}")
