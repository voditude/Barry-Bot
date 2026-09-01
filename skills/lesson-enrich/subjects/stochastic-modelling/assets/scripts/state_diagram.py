"""
Markov-chain transition/state-diagram renderer for lesson-enrich, matching the
document's palette (see diagram_style.py). No networkx dependency (not installed
in this environment) — states are laid out on a circle by hand and edges are drawn
with matplotlib FancyArrowPatch, curved outward for a reciprocal pair of arrows and
as a small self-loop for pjj > 0.

    from state_diagram import draw_state_diagram
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    P = [[0, 0.5, 0.5], [0.25, 0.75, 0], [0.4, 0, 0.6]]
    draw_state_diagram(ax, P, labels=["1", "2", "3"])
    plt.savefig("out.png", dpi=150, facecolor="white", bbox_inches="tight")

Only draws an edge i->j when P[i][j] > 0. Edge labels are the probability values,
formatted as simplified fractions where the value is a "nice" fraction (denominator
<= 24), otherwise as a decimal.
"""

import math
from fractions import Fraction

import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from diagram_style import COLORS, apply

NODE_RADIUS = 0.14


def _fmt(p):
    frac = Fraction(p).limit_denominator(24)
    if abs(float(frac) - p) < 1e-9 and frac.denominator <= 24:
        if frac.denominator == 1:
            return str(frac.numerator)
        return f"{frac.numerator}/{frac.denominator}"
    return f"{p:.2f}"


def _circle_positions(n, radius=1.0):
    return [
        (radius * math.cos(math.pi / 2 - 2 * math.pi * i / n),
         radius * math.sin(math.pi / 2 - 2 * math.pi * i / n))
        for i in range(n)
    ]


def draw_state_diagram(ax, P, labels=None, radius=1.0, node_color=None,
                        edge_color=None, show_probabilities=True, fontsize=11):
    """Draw a directed transition-probability diagram for P (list of lists / 2D
    array, rows summing to 1) onto ax. labels defaults to 1..n."""
    apply()
    n = len(P)
    labels = labels or [str(i + 1) for i in range(n)]
    node_color = node_color or COLORS["source"]
    edge_color = edge_color or COLORS["add"]
    pos = _circle_positions(n, radius)

    # edges first, so nodes sit on top
    for i in range(n):
        for j in range(n):
            p = P[i][j]
            if p <= 0:
                continue
            if i == j:
                _draw_self_loop(ax, pos[i], p, edge_color, show_probabilities, fontsize)
                continue
            reciprocal = P[j][i] > 0
            _draw_edge(ax, pos[i], pos[j], p, edge_color, reciprocal,
                       show_probabilities, fontsize)

    for (x, y), label in zip(pos, labels):
        ax.add_patch(mpatches.Circle((x, y), NODE_RADIUS, facecolor=node_color,
                                      edgecolor=COLORS["ink"], linewidth=1.2, zorder=3))
        ax.text(x, y, label, ha="center", va="center", color="white",
                fontsize=fontsize + 1, fontweight="bold", zorder=4)

    pad = radius + 0.45
    ax.set_xlim(-pad, pad)
    ax.set_ylim(-pad, pad)
    ax.set_aspect("equal")
    ax.axis("off")


def _draw_edge(ax, p0, p1, prob, color, curved, show_prob, fontsize):
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    ux, uy = dx / dist, dy / dist
    start = (x0 + ux * NODE_RADIUS, y0 + uy * NODE_RADIUS)
    end = (x1 - ux * NODE_RADIUS, y1 - uy * NODE_RADIUS)
    rad = 0.18 if curved else 0.0
    arrow = FancyArrowPatch(start, end, connectionstyle=f"arc3,rad={rad}",
                             arrowstyle="-|>", mutation_scale=14,
                             color=color, linewidth=1.6, zorder=2)
    ax.add_patch(arrow)
    if show_prob:
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        nx, ny = -uy, ux
        offset = (0.14 if curved else 0.08)
        ax.text(mx + nx * offset, my + ny * offset, _fmt(prob), ha="center",
                va="center", fontsize=fontsize - 1.5, color=color,
                bbox=dict(boxstyle="round,pad=0.12", facecolor="white",
                          edgecolor="none", alpha=0.85), zorder=5)


def _draw_self_loop(ax, p0, prob, color, show_prob, fontsize):
    x0, y0 = p0
    d = math.hypot(x0, y0)
    ux, uy = (x0 / d, y0 / d) if d > 0 else (0, 1)
    loop_center = (x0 + ux * NODE_RADIUS * 2.4, y0 + uy * NODE_RADIUS * 2.4)
    loop = mpatches.Circle(loop_center, NODE_RADIUS * 0.85, facecolor="none",
                            edgecolor=color, linewidth=1.6, zorder=2)
    ax.add_patch(loop)
    tip = (loop_center[0] + ux * NODE_RADIUS * 0.2,
           loop_center[1] + uy * NODE_RADIUS * 0.2 - 0.03)
    ax.annotate("", xy=tip, xytext=(tip[0] + 0.001, tip[1] + 0.001),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6))
    if show_prob:
        ax.text(loop_center[0] + ux * NODE_RADIUS * 1.6,
                 loop_center[1] + uy * NODE_RADIUS * 1.6, _fmt(prob),
                 ha="center", va="center", fontsize=fontsize - 1.5, color=color,
                 bbox=dict(boxstyle="round,pad=0.12", facecolor="white",
                           edgecolor="none", alpha=0.85), zorder=5)
