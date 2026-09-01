"""
Shared matplotlib style for lesson-enrich diagrams, matching the document's palette
(see the CSS custom properties in reference/quality-bar-sample.html). Import and call
apply() before plotting.

    from diagram_style import apply, COLORS
    apply()
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    ax.plot(x, y, color=COLORS["add"], linewidth=2.2)
    ...
    plt.savefig("out.png", dpi=150, facecolor="white")
"""

import matplotlib

# Matches the light-theme tokens in reference/quality-bar-sample.html. If the document's
# palette changes, update these to match — diagrams should look like part of the same
# document, not a generic matplotlib default.
COLORS = {
    "source": "#8A3A34",   # original-lecture-content accent (burgundy)
    "add": "#2F6659",      # enrichment/added-content accent (teal) — most plot lines use this
    "accent": "#2F6659",
    "disclaimer": "#8A5E17",
    "ink": "#3A403C",
    "ink_soft": "#5A5F5C",
    "grid": "#8A8F8C",
}


def apply():
    matplotlib.rcParams["font.size"] = 12
    matplotlib.rcParams["font.family"] = "sans-serif"
    matplotlib.rcParams["axes.edgecolor"] = COLORS["grid"]
    matplotlib.rcParams["axes.labelcolor"] = COLORS["ink"]
    matplotlib.rcParams["xtick.color"] = COLORS["ink_soft"]
    matplotlib.rcParams["ytick.color"] = COLORS["ink_soft"]
    matplotlib.rcParams["text.color"] = COLORS["ink"]


def strip_top_right(ax):
    """Common cleanup: drop the top/right spines, light grid — call after plotting."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.25)
