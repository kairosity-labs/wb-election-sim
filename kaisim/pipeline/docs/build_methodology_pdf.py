"""Build kaisim/pipeline/docs/METHODOLOGY.pdf.

Strict layout rules enforced:
  1. Every Box belongs to a Container (the figure root is the implicit one).
  2. A child Box is rendered ENTIRELY INSIDE its parent's content area
     (parent provides padding; render-time check raises if a child
     exceeds parent bounds).
  3. Sibling Boxes never overlap (bbox-intersection check raises on conflict).
  4. Arrows always anchor at the EDGE of source/dest rectangles
     (`top|bottom|left|right`-`center|left|right|top|bottom`). Computed,
     never hand-placed, so they always land on an actual edge.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


# ---------------------------------------------------------------------------
# Layout primitives
# ---------------------------------------------------------------------------

@dataclass
class Box:
    """A rectangle. Coordinates are absolute (figure-units, 0..100 each axis).
    Children are placed in absolute coords too — caller is responsible for
    keeping them inside parent."""
    x: float
    y: float
    w: float
    h: float
    label: str
    sublabel: str = ""
    style: str = "default"            # default | header | accent | leaf | callout
    children: list["Box"] = field(default_factory=list)
    parent: "Box | None" = field(default=None, repr=False)

    def add(self, child: "Box") -> "Box":
        # Containment check — child must lie fully inside parent's content area.
        pad = 0.6
        if not (self.x + pad <= child.x
                and child.x + child.w <= self.x + self.w - pad
                and self.y + pad <= child.y
                and child.y + child.h <= self.y + self.h - pad):
            raise ValueError(
                f"Box {child.label!r} ({child.x},{child.y},{child.w},{child.h}) "
                f"escapes parent {self.label!r} "
                f"({self.x},{self.y},{self.w},{self.h})")
        # No-overlap check among siblings.
        for sib in self.children:
            if not (child.x + child.w <= sib.x
                    or sib.x + sib.w <= child.x
                    or child.y + child.h <= sib.y
                    or sib.y + sib.h <= child.y):
                raise ValueError(
                    f"Box {child.label!r} overlaps sibling {sib.label!r} "
                    f"inside parent {self.label!r}")
        child.parent = self
        self.children.append(child)
        return child

    # Edge anchors — for arrows
    def top(self):    return (self.x + self.w / 2, self.y + self.h)
    def bottom(self): return (self.x + self.w / 2, self.y)
    def left(self):   return (self.x,              self.y + self.h / 2)
    def right(self):  return (self.x + self.w,     self.y + self.h / 2)

    def edge(self, side: str, frac: float = 0.5):
        """`side` ∈ top|bottom|left|right; `frac` ∈ [0, 1] along that edge."""
        if side == "top":    return (self.x + self.w * frac, self.y + self.h)
        if side == "bottom": return (self.x + self.w * frac, self.y)
        if side == "left":   return (self.x,                 self.y + self.h * frac)
        if side == "right":  return (self.x + self.w,        self.y + self.h * frac)
        raise ValueError(side)


STYLES = {
    "default": dict(facecolor="#F8FAFC", edgecolor="#1E293B", linewidth=1.4),
    "header":  dict(facecolor="#1E293B", edgecolor="#0F172A", linewidth=1.6),
    "accent":  dict(facecolor="#FFEDD5", edgecolor="#C2410C", linewidth=1.6),
    "leaf":    dict(facecolor="#DBEAFE", edgecolor="#1E40AF", linewidth=1.2),
    "callout": dict(facecolor="#FEF3C7", edgecolor="#A16207", linewidth=1.2),
    "phase":   dict(facecolor="#ECFDF5", edgecolor="#047857", linewidth=2.0),
}
TEXT_COLOR = {"header": "white"}


def render_box(ax, box: Box) -> None:
    s = STYLES[box.style]
    rect = FancyBboxPatch(
        (box.x, box.y), box.w, box.h,
        boxstyle="round,pad=0.0,rounding_size=0.6",
        **s,
        zorder=2,
    )
    ax.add_patch(rect)

    txt_color = TEXT_COLOR.get(box.style, "#0F172A")
    if box.style in ("header", "phase", "accent"):
        # Header/phase title at top of box
        ax.text(box.x + box.w / 2, box.y + box.h - 1.2, box.label,
                ha="center", va="top", fontsize=11, fontweight="bold",
                color=txt_color, zorder=3)
        if box.sublabel:
            ax.text(box.x + box.w / 2, box.y + box.h - 3.2, box.sublabel,
                    ha="center", va="top", fontsize=8.5, color=txt_color,
                    style="italic", zorder=3)
    else:
        ax.text(box.x + box.w / 2, box.y + box.h / 2 + (1.0 if box.sublabel else 0),
                box.label, ha="center", va="center",
                fontsize=10, fontweight="bold", color=txt_color, zorder=3)
        if box.sublabel:
            ax.text(box.x + box.w / 2, box.y + box.h / 2 - 1.4,
                    box.sublabel, ha="center", va="center",
                    fontsize=8, color="#475569", zorder=3)
    for c in box.children:
        render_box(ax, c)


def arrow(ax, src_anchor, dst_anchor, label: str = "",
          color: str = "#0F172A", style: str = "->", curved: float = 0.0,
          label_offset: tuple = (0, 0)) -> None:
    arrow = FancyArrowPatch(
        src_anchor, dst_anchor,
        arrowstyle=style,
        mutation_scale=14,
        linewidth=1.4,
        color=color,
        connectionstyle=f"arc3,rad={curved}",
        zorder=4,
    )
    ax.add_patch(arrow)
    if label:
        mid = ((src_anchor[0] + dst_anchor[0]) / 2 + label_offset[0],
                (src_anchor[1] + dst_anchor[1]) / 2 + label_offset[1])
        ax.text(*mid, label, ha="center", va="center",
                fontsize=8, color=color, style="italic",
                bbox=dict(boxstyle="round,pad=0.2",
                          facecolor="white", edgecolor="none", alpha=0.85),
                zorder=5)


def new_canvas(title: str, subtitle: str = ""):
    fig, ax = plt.subplots(figsize=(11.69, 8.27))   # A4 landscape
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 75)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(50, 72.5, title, ha="center", va="center",
            fontsize=16, fontweight="bold", color="#0F172A")
    if subtitle:
        ax.text(50, 69.5, subtitle, ha="center", va="center",
                fontsize=10, color="#475569", style="italic")
    return fig, ax


# ---------------------------------------------------------------------------
# Diagram 1 — System architecture (Phase 1 → Phase 2)
# ---------------------------------------------------------------------------

def diagram_architecture():
    fig, ax = new_canvas(
        "Kaisim — System Architecture",
        "Two-phase pipeline: persona synthesis (Phase 1) → belief evolution (Phase 2)")

    # Root frame
    root = Box(2, 2, 96, 65, "", style="default")

    # Phase 1 container
    p1 = Box(4, 8, 42, 56, "PHASE 1 — Persona Generation",
              sublabel="static synthesis from joint distributions",
              style="phase")
    root.add(p1)

    # Phase 2 container
    p2 = Box(54, 8, 42, 56, "PHASE 2 — Belief Evolution",
              sublabel="dynamic LLM-driven simulation over time",
              style="phase")
    root.add(p2)

    # Phase 1 children
    p1_data = p1.add(Box(7, 51, 36, 6, "Source data",
                          sublabel="Census 2011 · NFHS-5 · SHRUG · ECI",
                          style="leaf"))
    p1_axes = p1.add(Box(7, 41, 36, 6, "Axes & joints",
                          sublabel="dimensions × constraints",
                          style="default"))
    p1_samp = p1.add(Box(7, 31, 36, 6, "Samplers",
                          sublabel="sample personas honoring joints",
                          style="default"))
    p1_ver = p1.add(Box(7, 21, 36, 6, "Verifiers",
                         sublabel="chi-square vs marginals (z ≤ 2)",
                         style="default"))
    p1_pers = p1.add(Box(7, 10, 36, 8, "PersonaSet (output)",
                          sublabel="N personas — fields + self_prompt",
                          style="accent"))

    arrow(ax, p1_data.bottom(),  p1_axes.top())
    arrow(ax, p1_axes.bottom(),  p1_samp.top())
    arrow(ax, p1_samp.bottom(),  p1_ver.top())
    arrow(ax, p1_ver.bottom(),   p1_pers.top())

    # Phase 2 children
    p2_news = p2.add(Box(57, 51, 36, 6, "NewsPool",
                          sublabel="events_<period>.yaml — audited",
                          style="leaf"))
    p2_targ = p2.add(Box(57, 41, 36, 6, "Targeting Strategy",
                          sublabel="rule_based · show_all · embedding",
                          style="default"))
    p2_orch = p2.add(Box(57, 31, 36, 6, "Orchestrator",
                          sublabel="async tick loop · semaphore concurrency",
                          style="default"))
    p2_upd = p2.add(Box(57, 21, 36, 6, "Updaters (LLM)",
                         sublabel="park_minimal · reflection · final_query",
                         style="default"))
    p2_out = p2.add(Box(57, 10, 36, 8, "Run artifacts",
                         sublabel="memory + feeds + structured + final_vote",
                         style="accent"))

    arrow(ax, p2_news.bottom(),  p2_targ.top())
    arrow(ax, p2_targ.bottom(),  p2_orch.top())
    arrow(ax, p2_orch.bottom(),  p2_upd.top())
    arrow(ax, p2_upd.bottom(),   p2_out.top())

    # Cross-phase arrow: PersonaSet → Orchestrator
    arrow(ax, p1_pers.right(), p2_orch.left(),
          label="agents",
          color="#C2410C", curved=-0.2, label_offset=(0, -1))

    render_box(ax, root)
    return fig


# ---------------------------------------------------------------------------
# Diagram 2 — Data flow per tick
# ---------------------------------------------------------------------------

def diagram_data_flow():
    fig, ax = new_canvas(
        "Kaisim — Data flow per simulation tick",
        "What happens in one period (e.g. 2024-03) for one agent")

    root = Box(2, 2, 96, 65, "", style="default")

    # Inputs row
    inp = Box(4, 50, 92, 14, "Inputs (per tick)", style="phase")
    root.add(inp)
    in_news = inp.add(Box(7, 53, 22, 7, "NewsPool",
                           sublabel="events active in this period",
                           style="leaf"))
    in_agent = inp.add(Box(33, 53, 22, 7, "Agent state",
                            sublabel="persona + tags + memory_stream",
                            style="leaf"))
    in_clock = inp.add(Box(59, 53, 16, 7, "Ticker",
                            sublabel="period · is-reflection-tick?",
                            style="leaf"))
    in_cfg = inp.add(Box(77, 53, 16, 7, "Config",
                          sublabel="thresholds · concurrency",
                          style="leaf"))

    # Targeting → Updater → Memory
    targ = Box(7, 32, 35, 12, "Targeting",
                sublabel="score(agent, event) ≥ 4.0?",
                style="accent")
    root.add(targ)

    upd = Box(50, 32, 35, 12, "Updater (LLM call)",
               sublabel="park_minimal — engagement, reaction, delta",
               style="accent")
    root.add(upd)

    # Output row
    mem = Box(4, 8, 42, 18, "Memory write (per accepted event)",
               style="phase")
    root.add(mem)
    mem_a = mem.add(Box(7, 10, 36, 5, "memory_stream.jsonl",
                         sublabel="MemoryItem(timestamp, kind, content, importance)",
                         style="default"))
    mem_b = mem.add(Box(7, 16, 36, 5, "structured_history.jsonl",
                         sublabel="party_lean_change · trust_changes · salience",
                         style="default"))

    fee = Box(50, 8, 46, 18, "Audit + lookups", style="phase")
    root.add(fee)
    fee_a = fee.add(Box(53, 10, 40, 5, "feeds.jsonl",
                         sublabel="every delivery decision (accepted=true/false)",
                         style="default"))
    fee_b = fee.add(Box(53, 16, 40, 5, "(periodic) reflection compresses old memory",
                         sublabel="every 12 ticks → gist replaces raw",
                         style="callout"))

    # Arrows
    arrow(ax, in_news.bottom(),   targ.top())
    arrow(ax, in_agent.bottom(),  targ.edge("top", 0.6),
          label="tags + media", color="#475569")
    arrow(ax, in_agent.bottom(),  upd.edge("top", 0.2),
          label="self_prompt + memory", color="#475569",
          curved=-0.15)
    arrow(ax, targ.right(),       upd.left(),
          label="selected events", color="#C2410C")
    arrow(ax, upd.bottom(),       mem.top(),
          label="MemoryItem", color="#0F172A",
          curved=0.15, label_offset=(-3, 0))
    arrow(ax, targ.bottom(),      fee.edge("top", 0.05),
          label="every delivery decision", color="#475569",
          curved=-0.2, label_offset=(2, 0))

    render_box(ax, root)
    return fig


# ---------------------------------------------------------------------------
# Diagram 3 — Agent lifecycle (one update call internals)
# ---------------------------------------------------------------------------

def diagram_agent_lifecycle():
    fig, ax = new_canvas(
        "Kaisim — Agent lifecycle (one Park-minimal LLM call)",
        "Persona + memory + event → LLM → structured delta → memory append")

    root = Box(2, 2, 96, 65, "", style="default")

    # Pre-call container
    pre = Box(4, 38, 42, 26, "Prompt assembly (Python)",
               style="phase")
    root.add(pre)
    pre_p = pre.add(Box(7, 55, 36, 6, "System prompt",
                         sublabel="persona.narrative.self_prompt (cached)",
                         style="leaf"))
    pre_m = pre.add(Box(7, 47, 36, 6, "Memory window",
                         sublabel="last K reactions + reflections",
                         style="leaf"))
    pre_e = pre.add(Box(7, 39, 36, 6, "New event",
                         sublabel="headline + summary + scope + intensity",
                         style="leaf"))

    # LLM box (centered, no children)
    llm = Box(48, 42, 14, 18, "LLM",
               sublabel="Haiku 4.5\n(no thinking)",
               style="accent")
    root.add(llm)

    # Post-call container
    post = Box(64, 38, 32, 26, "Response (JSON)",
                style="phase")
    root.add(post)
    post_e = post.add(Box(67, 55, 26, 6, "engagement",
                           sublabel="scrolled_past | skimmed | engaged",
                           style="leaf"))
    post_r = post.add(Box(67, 47, 26, 6, "reaction + monologue",
                           sublabel="inner thought (free-text)",
                           style="leaf"))
    post_d = post.add(Box(67, 39, 26, 6, "structured_delta",
                           sublabel="party_lean + trust + salience",
                           style="leaf"))

    # Arrows pre → LLM → post
    arrow(ax, pre.right(), llm.left(),
          label="prompt", color="#C2410C")
    arrow(ax, llm.right(), post.left(),
          label="JSON", color="#C2410C")

    # Below: write decisions
    write = Box(4, 6, 92, 26, "Per-output write to disk", style="phase")
    root.add(write)

    write_a = write.add(Box(7, 18, 27, 10, "MemoryItem",
                             sublabel="if engagement ≠ scrolled_past:\nappend monologue",
                             style="default"))
    write_b = write.add(Box(36, 18, 27, 10, "Structured delta",
                             sublabel="append to\nstructured_history.jsonl",
                             style="default"))
    write_c = write.add(Box(65, 18, 28, 10, "Reflection trigger",
                             sublabel="if tick % 12 == 0:\nschedule reflection updater",
                             style="callout"))

    write_d = write.add(Box(7, 8, 86, 7,
                             "Final-tick: final_query updater asks "
                             "vote/reasoning/drivers → final_vote.json",
                             style="accent"))

    # Connect post → writes
    arrow(ax, post_r.bottom(), write_a.top(),
          color="#475569", curved=0.2, label_offset=(-1, 0))
    arrow(ax, post_d.bottom(), write_b.top(),
          color="#475569", curved=0.0)
    arrow(ax, post_d.bottom(), write_c.top(),
          color="#475569", curved=-0.2)

    render_box(ax, root)
    return fig


# ---------------------------------------------------------------------------
# Diagram 4 — Targeting score breakdown
# ---------------------------------------------------------------------------

def diagram_targeting_score():
    fig, ax = new_canvas(
        "Kaisim — Targeting score (rule_based)",
        "How a single (agent, event) pair gets a delivery score")

    root = Box(2, 2, 96, 65, "", style="default")

    # Top row — inputs
    inputs = Box(4, 50, 92, 13, "Inputs", style="phase")
    root.add(inputs)
    i_event = inputs.add(Box(7, 52.5, 28, 8, "Event",
                              sublabel="scope · tags · intensity · valence",
                              style="leaf"))
    i_agent = inputs.add(Box(38, 52.5, 28, 8, "Agent",
                              sublabel="tags · media_engagement",
                              style="leaf"))
    i_cfg = inputs.add(Box(69, 52.5, 24, 8, "Config",
                            sublabel="weights · threshold",
                            style="leaf"))

    # Middle — score formula container
    sc = Box(4, 18, 92, 28, "Score computation", style="phase")
    root.add(sc)
    s1 = sc.add(Box(7, 36, 18, 7, "scope_weight",
                     sublabel="nat:1 / state:2 / dist:3 / AC:4",
                     style="default"))
    s2 = sc.add(Box(28, 36, 18, 7, "tag_overlap × 1",
                     sublabel="|agent.tags ∩ event.tags|",
                     style="default"))
    s3 = sc.add(Box(49, 36, 18, 7, "intensity − 2",
                     sublabel="if intensity ≥ 3",
                     style="default"))
    s4 = sc.add(Box(70, 36, 22, 7, "× media_engagement",
                     sublabel="0.3 .. 1.5 multiplier",
                     style="default"))
    s5 = sc.add(Box(7, 25, 38, 7, "+ loss_aversion (+1)",
                     sublabel="if any tag.valence == 'negative'",
                     style="default"))
    s6 = sc.add(Box(48, 25, 44, 7, "= total_score",
                     sublabel="single float",
                     style="accent"))

    # Bottom — decision
    dec = Box(4, 4, 92, 12, "Decision", style="phase")
    root.add(dec)
    d_pass = dec.add(Box(7, 6.5, 38, 7, "score ≥ 4.0 → DELIVERED",
                          sublabel="written to feeds.jsonl, sent to LLM updater",
                          style="accent"))
    d_drop = dec.add(Box(50, 6.5, 43, 7, "score < 4.0 → silently dropped",
                          sublabel="not delivered; not counted in ignore rate",
                          style="callout"))

    # Arrows
    arrow(ax, inputs.bottom(), sc.top(), color="#475569")
    arrow(ax, sc.bottom(), dec.top(), color="#C2410C", label="threshold check")
    arrow(ax, s6.bottom(), d_pass.edge("top", 0.5), color="#047857",
          curved=-0.2)

    render_box(ax, root)
    return fig


# ---------------------------------------------------------------------------
# Diagram 5 — Belief update cycle (the loop view)
# ---------------------------------------------------------------------------

def diagram_belief_loop():
    fig, ax = new_canvas(
        "Kaisim — Belief evolution loop",
        "How trust + memory accumulate over the simulation period")

    root = Box(2, 2, 96, 65, "", style="default")

    loop = Box(4, 6, 92, 58, "Per-tick loop (53 ticks for WB AC-95)",
                style="phase")
    root.add(loop)

    # Five stations laid out clockwise from top-left
    s_news = loop.add(Box(7, 48, 22, 11, "1. NewsPool active in period",
                           sublabel="episodic · chronic events",
                           style="default"))
    s_targ = loop.add(Box(38, 48, 22, 11, "2. Targeting filter",
                           sublabel="score per (agent, event) ≥ 4.0",
                           style="default"))
    s_upd = loop.add(Box(69, 48, 24, 11, "3. LLM updater (park_minimal)",
                          sublabel="reaction + structured delta",
                          style="accent"))

    s_mem = loop.add(Box(69, 25, 24, 11, "4. Append memory",
                          sublabel="incremental disk flush",
                          style="default"))
    s_ref = loop.add(Box(38, 25, 22, 11, "5. Reflection",
                          sublabel="every 12 ticks (periodic)",
                          style="callout"))
    s_fin = loop.add(Box(7, 25, 22, 11, "6. final_query",
                          sublabel="vote + reasoning (final tick)",
                          style="accent"))

    # Bottom — analysis
    s_an = loop.add(Box(7, 9, 86, 12, "Post-run analysis (belief_analysis.py)",
                         sublabel="trust_evolution · vote_redistribution · "
                                  "switcher_matrix · per-event × demographic heatmaps",
                         style="default"))

    # Arrows: clockwise loop
    arrow(ax, s_news.right(), s_targ.left(), label="active events",
          color="#C2410C")
    arrow(ax, s_targ.right(), s_upd.left(), label="selected", color="#C2410C")
    arrow(ax, s_upd.bottom(), s_mem.top(), label="JSON delta",
          color="#0F172A")
    arrow(ax, s_mem.left(),   s_ref.right(), color="#475569",
          label="trigger?")
    arrow(ax, s_ref.left(),   s_fin.right(), color="#475569",
          label="(or skip)")
    arrow(ax, s_fin.bottom(), s_an.edge("top", 0.15),
          label="last tick", color="#047857", curved=-0.1)
    arrow(ax, s_mem.bottom(), s_an.edge("top", 0.85),
          label="all ticks", color="#047857", curved=0.2)

    # Loop-back arrow indicating recurrence
    arrow(ax, s_fin.top(), s_news.bottom(), color="#94A3B8",
          curved=0.4, label="next tick", label_offset=(-5, -3),
          style="->")

    render_box(ax, root)
    return fig


# ---------------------------------------------------------------------------
# Build the PDF
# ---------------------------------------------------------------------------

def build(out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    builders = [
        ("Architecture", diagram_architecture),
        ("Data flow per tick", diagram_data_flow),
        ("Agent lifecycle", diagram_agent_lifecycle),
        ("Targeting score", diagram_targeting_score),
        ("Belief evolution loop", diagram_belief_loop),
    ]
    with PdfPages(out_path) as pdf:
        # Title page
        fig, ax = new_canvas("Kaisim — Methodology",
                              "Visual reference · 5 diagrams")
        ax.text(50, 45,
                "1. System architecture\n"
                "2. Data flow per tick\n"
                "3. Agent lifecycle\n"
                "4. Targeting score (rule_based)\n"
                "5. Belief evolution loop",
                ha="center", va="center", fontsize=12, color="#1E293B")
        ax.text(50, 18,
                "All rectangles satisfy strict child-parent containment "
                "and zero-overlap constraints. Arrows always anchor at "
                "rectangle edges. Built by `build_methodology_pdf.py` — "
                "rerun after any architectural change.",
                ha="center", va="center", fontsize=9, color="#64748B",
                style="italic", wrap=True)
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)

        for name, fn in builders:
            print(f"  rendering {name}...")
            fig = fn()
            pdf.savefig(fig, bbox_inches="tight")
            plt.close(fig)

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    out = Path(__file__).parent / "METHODOLOGY.pdf"
    build(out)
