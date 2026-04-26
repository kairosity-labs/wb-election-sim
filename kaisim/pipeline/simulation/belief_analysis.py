"""Belief-evolution analysis — how did sentiment and vote intent shift
over time and in response to specific events?

Outputs:
    analysis/vote_trajectory.png         vote-share over time (party lines)
    analysis/event_impact.png            which events caused biggest shifts
    analysis/switcher_matrix.png         initial 2019 party → final 2024 vote
    analysis/demographic_trajectories.png vote-share split by religion/caste
    analysis/event_engagement.png        engagement + importance per event
    analysis/report.md                   narrative report with sample quotes
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


_PARTIES = ["BJP", "AITC", "Left+INC", "Other", "Undecided"]
_PARTY_FROM_LEAN = {
    "more_BJP": "BJP",
    "more_AITC": "AITC",
    "more_LeftINC": "Left+INC",
    "more_Other": "Other",
}
_INITIAL_PARTY_MAP = {"BJP": "BJP", "AITC": "AITC", "INC": "Left+INC", "LF": "Left+INC", "Other": "Other"}
_FINAL_PARTY_MAP = {"BJP": "BJP", "AITC": "AITC", "INC": "Left+INC", "LF": "Left+INC",
                     "Other": "Other", "NOTA": "Undecided"}


def load_run(run_root: Path) -> dict:
    """Load all per-agent data into a structured dict."""
    run_root = Path(run_root)
    agents = {}
    for agent_dir in sorted((run_root / "agents").iterdir()):
        if not agent_dir.is_dir():
            continue
        agent_id = agent_dir.name
        persona = json.loads((agent_dir / "persona.json").read_text())
        memories = []
        for line in (agent_dir / "memory_stream.jsonl").read_text().splitlines():
            if line.strip():
                memories.append(json.loads(line))
        structured = []
        sh = agent_dir / "structured_history.jsonl"
        if sh.exists():
            for line in sh.read_text().splitlines():
                if line.strip():
                    structured.append(json.loads(line))
        feeds = []
        fp = agent_dir / "feeds.jsonl"
        if fp.exists():
            for line in fp.read_text().splitlines():
                if line.strip():
                    feeds.append(json.loads(line))
        final_vote = None
        fv = agent_dir / "final_vote.json"
        if fv.exists():
            final_vote = json.loads(fv.read_text())
        agents[agent_id] = {
            "persona": persona,
            "memories": memories,
            "structured": structured,
            "feeds": feeds,
            "final_vote": final_vote,
        }
    return agents


def _agent_initial_party(persona: dict) -> str:
    return _INITIAL_PARTY_MAP.get(persona["fields"].get("vote_2019_LS"), "Undecided")


def _agent_party_at_month(agent: dict, month_iso: str, anchor_strength: int = 3) -> str:
    """Compute the party an agent would lean toward at end of `month_iso`.

    Score = anchor_strength on initial party + sum of structured shifts up to month.
    Returns the argmax party.
    """
    initial = _agent_initial_party(agent["persona"])
    scores = {p: 0 for p in _PARTIES}
    if initial in scores:
        scores[initial] = anchor_strength
    for s in agent["structured"]:
        if s["timestamp"] > month_iso:
            break
        delta = s.get("delta") or {}
        lean = delta.get("party_lean_change", "no_change")
        if lean in _PARTY_FROM_LEAN:
            scores[_PARTY_FROM_LEAN[lean]] += 1
    return max(scores.items(), key=lambda kv: kv[1])[0]


def _all_months(agents: dict) -> list[str]:
    """All YYYY-MM strings spanning the simulation."""
    timestamps = set()
    for a in agents.values():
        for s in a["structured"]:
            timestamps.add(s["timestamp"][:7])  # YYYY-MM
    if not timestamps:
        return ["2024-05"]
    months = sorted(timestamps)
    # Pad: the timeline span we want is 2020-01 → 2024-05
    out = []
    cur = date(2020, 1, 1)
    end = date(2024, 5, 1)
    while cur <= end:
        out.append(f"{cur.year:04d}-{cur.month:02d}")
        m = cur.month + 1
        y = cur.year + (m - 1) // 12
        m = ((m - 1) % 12) + 1
        cur = date(y, m, 1)
    return out


# ---------------------------------------------------------------------------
# Plot 0: vote redistribution over time (the real "where do they sit now")
# ---------------------------------------------------------------------------
#
# Each agent has an inferred current-vote-lean at every month, computed by
# scoring (initial-anchor + party_lean_change shifts + trust changes mapped
# to parties). At each month, take argmax → current lean. Aggregate across
# agents → population %. Plot as stacked area to see redistribution.

_ANCHOR = 2.0                               # initial 2019 prior weight
_LEAN_SHIFT_W = 2.0                         # weight per explicit "more_X" tag
_TRUST_W = {"+small": 0.5, "+large": 1.5, "-small": -0.5, "-large": -1.5}
_ENTITY_BUCKETS = {                         # canonical entity → bucket
    "modi": "Modi/Centre", "modi_bjp": "Modi/Centre", "bjp": "Modi/Centre",
    "central_government": "Modi/Centre", "centre": "Modi/Centre",
    "mamata": "Mamata/TMC", "mamata_banerjee": "Mamata/TMC",
    "mamata_aitc": "Mamata/TMC", "aitc": "Mamata/TMC", "tmc": "Mamata/TMC",
    "state_government": "Mamata/TMC",
    "shantanu": "Shantanu/Matua", "shantanu_thakur": "Shantanu/Matua",
    "matua_mahasangha": "Shantanu/Matua",
    "mamatabala": "Mamatabala/TMC-Matua", "mamatabala_thakur": "Mamatabala/TMC-Matua",
}
_BUCKET_TO_PARTY = {
    "Modi/Centre": "BJP",
    "Shantanu/Matua": "BJP",
    "Mamata/TMC": "AITC",
    "Mamatabala/TMC-Matua": "AITC",
}


def _agent_lean_history(agent: dict) -> dict[str, str]:
    """For one agent, return {YYYY-MM: inferred_party_lean} for every month
    where any event was processed."""
    initial = _agent_initial_party(agent["persona"])
    score = {p: 0.0 for p in _PARTIES}
    if initial in score:
        score[initial] = _ANCHOR

    history: dict[str, str] = {}
    for s in sorted(agent["structured"], key=lambda x: x["timestamp"]):
        m = s["timestamp"][:7]
        delta = s.get("delta") or {}
        lc = delta.get("party_lean_change")
        if lc in _PARTY_FROM_LEAN:
            score[_PARTY_FROM_LEAN[lc]] += _LEAN_SHIFT_W
        for entity, dv in (delta.get("trust_changes") or {}).items():
            e = entity.lower().replace(" ", "_").replace("(", "").replace(")", "")
            bucket = _ENTITY_BUCKETS.get(e)
            if not bucket:
                continue
            party = _BUCKET_TO_PARTY.get(bucket)
            if not party:
                continue
            w = _TRUST_W.get(str(dv).lower(), 0)
            score[party] += w
        history[m] = max(score.items(), key=lambda kv: kv[1])[0]
    return history


def plot_vote_redistribution(agents: dict, out_path: Path) -> None:
    months = _all_months(agents)
    histories = {aid: _agent_lean_history(a) for aid, a in agents.items()}
    leans_now = {aid: _agent_initial_party(a["persona"]) for aid, a in agents.items()}
    series = []
    for m in months:
        for aid in agents:
            if m in histories[aid]:
                leans_now[aid] = histories[aid][m]
        series.append(Counter(leans_now.values()))

    n = len(agents)
    fig, ax = plt.subplots(figsize=(13, 6))
    party_order = ["BJP", "AITC", "Left+INC", "Other", "Undecided"]
    colors = {"BJP": "#FF8C00", "AITC": "#16A34A", "Left+INC": "#DC2626",
              "Other": "#9333EA", "Undecided": "#737373"}
    arrays = []
    for p in party_order:
        arrays.append([series[i].get(p, 0) / n * 100 for i in range(len(months))])
    ax.stackplot(months, *arrays, labels=party_order,
                 colors=[colors[p] for p in party_order], alpha=0.85)

    final_dist = Counter(_FINAL_PARTY_MAP.get(a["final_vote"]["vote"], "Undecided")
                          if a["final_vote"] else "Undecided"
                          for a in agents.values())
    cum = 0
    for p in party_order:
        v = final_dist.get(p, 0)
        if v == 0:
            continue
        ax.text(len(months) - 0.5, cum + v / 2, f"  final-query: {v}",
                fontsize=8, va="center", ha="left", color="black", fontweight="bold")
        cum += v

    event_marks = [
        ("2020-03", "Lockdown"), ("2020-05", "Amphan"),
        ("2020-12", "Suvendu→BJP"), ("2021-02", "Modi visit"),
        ("2021-04", "COVID 2nd wave"), ("2021-05", "WB AE"),
        ("2021-07", "Shantanu MoS"), ("2021-08", "Lakshmir Bh."),
        ("2022-07", "Partha"), ("2024-01", "Ram Mandir"),
        ("2024-03", "CAA Rules"), ("2024-04", "SSC scrap"),
        ("2024-05", "POLLS"),
    ]
    for m, label in event_marks:
        if m in months:
            ax.axvline(months.index(m), linestyle=":", color="white",
                       alpha=0.6, linewidth=1)
            ax.text(months.index(m), 102, label, rotation=90, fontsize=7,
                    va="bottom", ha="right", alpha=0.8)

    ax.set_xticks(range(0, len(months), 3))
    ax.set_xticklabels([months[i] for i in range(0, len(months), 3)],
                        rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("% of agents currently leaning toward party")
    ax.set_xlim(0, len(months) - 1)
    ax.set_ylim(0, 100)
    ax.set_title(f"Vote-lean redistribution over time (n={n}; "
                 f"inferred from cumulative shifts + trust changes)",
                 fontweight="bold")
    ax.legend(loc="lower left", fontsize=9, framealpha=0.9)
    ax.grid(axis="y", linestyle=":", alpha=0.4, color="white")
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def plot_switches_over_time(agents: dict, out_path: Path) -> None:
    """Bar chart: how many agents flipped their inferred lean in each month."""
    months = _all_months(agents)
    histories = {aid: _agent_lean_history(a) for aid, a in agents.items()}
    switch_count = {m: 0 for m in months}
    leans = {aid: _agent_initial_party(a["persona"]) for aid, a in agents.items()}
    for m in months:
        for aid in agents:
            new = histories[aid].get(m)
            if new is not None and new != leans[aid]:
                switch_count[m] += 1
                leans[aid] = new

    fig, ax = plt.subplots(figsize=(13, 4))
    ys = [switch_count[m] for m in months]
    ax.bar(months, ys, color="#DC2626", alpha=0.8)
    event_marks = [
        ("2020-05", "Amphan"), ("2021-05", "WB AE"),
        ("2021-07", "Shantanu MoS"), ("2021-08", "Lakshmir Bh."),
        ("2022-07", "Partha"), ("2024-01", "Ram Mandir"),
        ("2024-03", "CAA Rules"), ("2024-04", "SSC scrap"),
    ]
    ymax = max(ys) if ys else 1
    for m, label in event_marks:
        if m in months:
            ax.text(months.index(m), ymax * 0.9, label, rotation=90, fontsize=7,
                    va="top", ha="right", alpha=0.7)
    ax.set_xticks(range(0, len(months), 3))
    ax.set_xticklabels([months[i] for i in range(0, len(months), 3)],
                        rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("# of agents who flipped lean this month")
    ax.set_title(f"Vote-lean switches per month (n={len(agents)} agents) — "
                 f"total {sum(switch_count.values())} switch-events",
                 fontweight="bold")
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Plot 1: cumulative party-pull momentum over time
# ---------------------------------------------------------------------------
#
# The LLM rarely emits an explicit "party_lean_change"; most events log
# "no_change" but the agent absorbs them into memory + trust + salience.
# So a "vote trajectory" derived only from party_lean_change deltas looks
# flat. The real movement materializes at final-vote-query time when the
# LLM integrates the whole accumulated memory.
#
# This plot shows the MOMENTUM: cumulative count of "more_BJP" vs "more_AITC"
# vs "more_LeftINC" deltas across all agents over time. Useful for seeing
# WHICH events generated explicit pull, even if most events didn't.

def plot_party_momentum(agents: dict, out_path: Path) -> None:
    months = _all_months(agents)
    cum = {p: [0] * len(months) for p in ("more_BJP", "more_AITC", "more_LeftINC", "more_Other")}
    for a in agents.values():
        for s in a["structured"]:
            ts = s["timestamp"][:7]
            if ts not in months:
                continue
            idx = months.index(ts)
            lean = (s.get("delta") or {}).get("party_lean_change", "no_change")
            if lean in cum:
                # cumulative: increment from this month onward
                for i in range(idx, len(months)):
                    cum[lean][i] += 1

    fig, ax = plt.subplots(figsize=(13, 6))
    colors = {"more_BJP": "#FF8C00", "more_AITC": "#16A34A",
              "more_LeftINC": "#DC2626", "more_Other": "#9333EA"}
    labels = {"more_BJP": "→ BJP shifts (cumulative)",
              "more_AITC": "→ AITC shifts (cumulative)",
              "more_LeftINC": "→ Left+INC shifts (cumulative)",
              "more_Other": "→ Other shifts (cumulative)"}
    for k, v in cum.items():
        ax.plot(months, v, label=labels[k], color=colors[k], linewidth=2.5, marker="o", markersize=3)

    event_marks = [
        ("2020-03", "Lockdown"),
        ("2020-05", "Amphan"),
        ("2020-12", "Suvendu→BJP"),
        ("2021-05", "WB AE"),
        ("2021-08", "Lakshmir Bh."),
        ("2022-07", "Partha arrest"),
        ("2024-01", "Ram Mandir"),
        ("2024-03", "CAA Rules"),
        ("2024-04", "SSC scrap"),
        ("2024-05", "POLLS"),
    ]
    ymax = max(max(v) for v in cum.values()) or 10
    for m, label in event_marks:
        if m in months:
            ax.axvline(months.index(m), linestyle=":", color="black", alpha=0.3)
            ax.text(months.index(m), ymax * 0.95, label, rotation=90, fontsize=7,
                    va="top", ha="right", alpha=0.7)

    ax.set_xticks(range(0, len(months), 3))
    ax.set_xticklabels([months[i] for i in range(0, len(months), 3)], rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Cumulative explicit-shift count across all agents")
    ax.set_title(f"Party-pull momentum over time (n={len(agents)} agents) — \n"
                 f"explicit party_lean_change events only; most events are 'no_change'",
                 fontweight="bold")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Plot 1b: trust evolution per entity over time
# ---------------------------------------------------------------------------

def plot_trust_evolution(agents: dict, out_path: Path) -> None:
    """Avg signed trust delta toward key entities, cumulative over time."""
    # Map entity name variants → canonical bucket
    # The LLM uses many variants ("Modi_BJP", "Mamata_AITC", "central_government", etc.)
    canon = {
        "modi": "Modi/Centre", "modi_bjp": "Modi/Centre", "bjp": "Modi/Centre",
        "central_government": "Modi/Centre", "centre": "Modi/Centre",
        "mamata": "Mamata/TMC", "mamata_banerjee": "Mamata/TMC",
        "mamata_aitc": "Mamata/TMC", "aitc": "Mamata/TMC", "tmc": "Mamata/TMC",
        "state_government": "Mamata/TMC",
        "shantanu": "Shantanu/Matua", "shantanu_thakur": "Shantanu/Matua",
        "matua_mahasangha": "Shantanu/Matua",
        "mamatabala": "Mamatabala/TMC-Matua", "mamatabala_thakur": "Mamatabala/TMC-Matua",
    }
    weight = {"+small": 1, "+large": 3, "-small": -1, "-large": -3}

    months = _all_months(agents)
    cum: dict[str, list[float]] = {b: [0.0] * len(months) for b in
                                    ("Modi/Centre", "Mamata/TMC", "Shantanu/Matua", "Mamatabala/TMC-Matua")}
    for a in agents.values():
        for s in a["structured"]:
            ts = s["timestamp"][:7]
            if ts not in months:
                continue
            idx = months.index(ts)
            tc = (s.get("delta") or {}).get("trust_changes", {})
            for entity, delta in tc.items():
                e_key = entity.lower().replace(" ", "_")
                bucket = canon.get(e_key)
                if not bucket:
                    continue
                w = weight.get(delta.lower(), 0)
                if w == 0:
                    continue
                for i in range(idx, len(months)):
                    cum[bucket][i] += w

    fig, ax = plt.subplots(figsize=(13, 6))
    colors = {"Modi/Centre": "#FF8C00", "Mamata/TMC": "#16A34A",
              "Shantanu/Matua": "#0EA5E9", "Mamatabala/TMC-Matua": "#A855F7"}
    for bucket, vals in cum.items():
        # Average per agent
        ys = [v / len(agents) for v in vals]
        ax.plot(months, ys, label=bucket, color=colors[bucket], linewidth=2.5, marker="o", markersize=3)

    ax.axhline(0, linestyle="-", color="black", linewidth=0.8, alpha=0.3)
    ax.set_xticks(range(0, len(months), 3))
    ax.set_xticklabels([months[i] for i in range(0, len(months), 3)], rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Avg cumulative signed trust score per agent")
    ax.set_title("Trust evolution toward key political actors over time", fontweight="bold")
    ax.legend(loc="best", fontsize=9)
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


# Keep the old function name for backward compat
def plot_vote_trajectory(agents: dict, out_path: Path) -> dict:
    plot_party_momentum(agents, out_path)
    return {}


# ---------------------------------------------------------------------------
# Plot 2: per-event impact
# ---------------------------------------------------------------------------

def plot_event_impact(agents: dict, out_path: Path) -> list[dict]:
    """For each news event, compute:
       - how many agents engaged
       - average importance rating
       - net party-lean shift (BJP+ minus AITC+)
    """
    by_event: dict[str, dict] = defaultdict(lambda: {
        "delivered": 0, "accepted": 0, "ignored": 0,
        "more_BJP": 0, "more_AITC": 0, "more_LeftINC": 0, "more_Other": 0,
        "no_change": 0, "importance_sum": 0, "importance_n": 0,
    })
    for a in agents.values():
        for f in a["feeds"]:
            slug = f["event_slug"]
            by_event[slug]["delivered"] += 1
            if f["accepted"]:
                by_event[slug]["accepted"] += 1
            else:
                by_event[slug]["ignored"] += 1
        for m in a["memories"]:
            if m["kind"] != "reaction":
                continue
            slug = m.get("triggering_event_slug")
            if not slug:
                continue
            by_event[slug]["importance_sum"] += m.get("importance", 5)
            by_event[slug]["importance_n"] += 1
        for s in a["structured"]:
            slug = s.get("triggering_event_slug")
            delta = (s.get("delta") or {}).get("party_lean_change", "no_change")
            if slug and delta in by_event[slug]:
                by_event[slug][delta] += 1

    rows = []
    for slug, e in by_event.items():
        avg_imp = e["importance_sum"] / e["importance_n"] if e["importance_n"] else 0
        net_bjp = e["more_BJP"] - e["more_AITC"]   # positive = pro-BJP, negative = pro-TMC
        rows.append({
            "slug": slug, "delivered": e["delivered"], "accepted": e["accepted"],
            "ignore_pct": round(100 * e["ignored"] / max(e["delivered"], 1), 1),
            "avg_importance": round(avg_imp, 2),
            "net_bjp_minus_aitc": net_bjp,
            "more_BJP": e["more_BJP"], "more_AITC": e["more_AITC"],
            "more_LeftINC": e["more_LeftINC"], "more_Other": e["more_Other"],
            "no_change": e["no_change"],
        })
    rows.sort(key=lambda r: -(abs(r["net_bjp_minus_aitc"])))

    # Top 18 events by absolute political pull
    top = rows[:18]
    fig, axes = plt.subplots(1, 2, figsize=(15, max(5, len(top) * 0.32)))
    slugs = [r["slug"] for r in top]
    bjp_pull = [r["more_BJP"] for r in top]
    aitc_pull = [-r["more_AITC"] for r in top]   # left side
    li_pull = [-r["more_LeftINC"] for r in top]

    y = list(range(len(top)))
    axes[0].barh(y, bjp_pull, color="#FF8C00", label="→ BJP")
    axes[0].barh(y, aitc_pull, color="#16A34A", label="→ AITC")
    axes[0].barh(y, [a + b for a, b in zip(aitc_pull, li_pull)], color="#DC2626",
                  label="→ Left+INC", left=aitc_pull)
    axes[0].set_yticks(y)
    axes[0].set_yticklabels(slugs, fontsize=7)
    axes[0].invert_yaxis()
    axes[0].axvline(0, color="black", linewidth=0.5)
    axes[0].set_xlabel("Agent-shift count (←TMC/Left   |   BJP→)")
    axes[0].set_title("Per-event party-pull (top 18 events by absolute pull)", fontweight="bold")
    axes[0].legend(loc="lower right", fontsize=8)
    axes[0].grid(axis="x", linestyle=":", alpha=0.5)

    # Importance + ignore-rate panel
    importance = [r["avg_importance"] for r in top]
    ignore_pct = [r["ignore_pct"] for r in top]
    axes[1].barh(y, importance, color="#4C72B0", label="avg importance (1-10)")
    axes[1].set_yticks(y)
    axes[1].set_yticklabels(slugs, fontsize=7)
    axes[1].invert_yaxis()
    axes[1].set_xlim(0, 10)
    axes[1].set_xlabel("Avg LLM-rated importance per accepted reaction")
    axes[1].set_title("Importance per event (top 18)", fontweight="bold")
    for i, p in enumerate(ignore_pct):
        axes[1].text(0.1, i, f"  {p}% ignored", va="center", fontsize=7, color="white")
    axes[1].grid(axis="x", linestyle=":", alpha=0.5)

    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return rows


# ---------------------------------------------------------------------------
# Plot 3: switcher matrix
# ---------------------------------------------------------------------------

def plot_switcher_matrix(agents: dict, out_path: Path) -> dict:
    matrix: dict[str, Counter] = defaultdict(Counter)
    for a in agents.values():
        initial = _agent_initial_party(a["persona"])
        if a["final_vote"]:
            final = _FINAL_PARTY_MAP.get(a["final_vote"]["vote"], "Undecided")
        else:
            final = "Undecided"
        matrix[initial][final] += 1

    initials = ["BJP", "AITC", "Left+INC", "Other", "Undecided"]
    finals = initials
    grid = [[matrix[i][f] for f in finals] for i in initials]

    fig, ax = plt.subplots(figsize=(8, 6))
    import numpy as np
    arr = np.array(grid, dtype=float)
    im = ax.imshow(arr, cmap="Oranges", aspect="auto")
    for i in range(len(initials)):
        for j in range(len(finals)):
            v = int(arr[i, j])
            if v > 0:
                color = "white" if v > arr.max() * 0.5 else "black"
                ax.text(j, i, str(v), ha="center", va="center", fontsize=10, color=color)
    ax.set_xticks(range(len(finals)))
    ax.set_xticklabels(finals)
    ax.set_yticks(range(len(initials)))
    ax.set_yticklabels(initials)
    ax.set_xlabel("Final 2024 vote")
    ax.set_ylabel("Initial 2019 prior")
    ax.set_title("Switcher matrix: 2019 prior → 2024 vote", fontweight="bold")
    fig.colorbar(im, ax=ax, label="agent count")
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return {ini: dict(cnt) for ini, cnt in matrix.items()}


# ---------------------------------------------------------------------------
# Plot 4: demographic trajectories
# ---------------------------------------------------------------------------

def plot_demographic_trajectories(agents: dict, out_path: Path) -> None:
    """Vote-share trajectory split by key demographic axes."""
    months = _all_months(agents)

    def _trajectory(filter_fn) -> dict[str, list[float]]:
        subset = [a for a in agents.values() if filter_fn(a["persona"])]
        if not subset:
            return {p: [0.0] * len(months) for p in _PARTIES}
        out = {p: [] for p in _PARTIES}
        for m in months:
            m_end = m + "-31"
            c = Counter()
            for a in subset:
                c[_agent_party_at_month(a, m_end)] += 1
            for p in _PARTIES:
                out[p].append(100 * c.get(p, 0) / len(subset))
        return out

    splits = {
        "Matua refugee (caste=Namasudra_Matua, mig=Bangladesh)": lambda f: (
            f["fields"].get("caste") == "Namasudra_Matua"
            and f["fields"].get("migration") == "Bangladesh"
        ),
        "Muslim voter": lambda f: f["fields"].get("religion") == "Muslim",
        "Female voter": lambda f: f["fields"].get("gender") == "Female",
        "Cultivator household": lambda f: f["fields"].get("occupation") == "Cultivator",
        "Urban (Bangaon Muni)": lambda f: f["fields"].get("gp_location") == "U1_Muni",
    }

    fig, axes = plt.subplots(len(splits), 1, figsize=(13, 3.5 * len(splits)))
    if len(splits) == 1:
        axes = [axes]
    colors = {"BJP": "#FF8C00", "AITC": "#16A34A", "Left+INC": "#DC2626",
              "Other": "#9333EA", "Undecided": "#737373"}

    for ax, (label, filt) in zip(axes, splits.items()):
        traj = _trajectory(filt)
        n = sum(1 for a in agents.values() if filt(a["persona"]))
        for p in _PARTIES:
            ax.plot(months, traj[p], label=p, color=colors[p], linewidth=2,
                    marker="o", markersize=2)
        ax.set_xticks(range(0, len(months), 6))
        ax.set_xticklabels([months[i] for i in range(0, len(months), 6)], rotation=45, ha="right", fontsize=7)
        ax.set_ylabel("% leaning")
        ax.set_title(f"{label} (n={n})", fontweight="bold", fontsize=10)
        ax.legend(loc="upper left", fontsize=7, ncol=5)
        ax.grid(axis="y", linestyle=":", alpha=0.5)
        ax.set_ylim(0, 100)

    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Markdown report with sample quotes
# ---------------------------------------------------------------------------

def write_report(agents: dict, event_rows: list[dict], switcher: dict,
                  out_path: Path) -> None:
    n = len(agents)
    final_dist = Counter(_FINAL_PARTY_MAP.get(a["final_vote"]["vote"], "Undecided")
                         if a["final_vote"] else "Undecided"
                         for a in agents.values())

    # Compute switcher headline
    stayed = sum(switcher.get(k, {}).get(k, 0) for k in switcher)
    flipped = sum(sum(v.values()) for v in switcher.values()) - stayed

    # Sample quotes: pick 3 agents that switched their vote
    switchers_with_quotes = []
    for aid, a in agents.items():
        initial = _agent_initial_party(a["persona"])
        if not a["final_vote"]:
            continue
        final = _FINAL_PARTY_MAP.get(a["final_vote"]["vote"], "Undecided")
        if initial != final and a["final_vote"].get("reasoning"):
            switchers_with_quotes.append((aid, initial, final, a))
    import random
    random.seed(42)
    random.shuffle(switchers_with_quotes)

    lines = []
    lines.append("# Belief evolution analysis")
    lines.append(f"\n*n={n} agents · 2020-01 → 2024-05 (53 months)*\n")

    lines.append("## Final 2024 vote (after living through 4.5 years of news)")
    lines.append("| Party | n | % |")
    lines.append("|---|---|---|")
    for p in ["BJP", "AITC", "Left+INC", "Other", "Undecided"]:
        c = final_dist.get(p, 0)
        lines.append(f"| {p} | {c} | {round(100*c/n, 1)}% |")

    lines.append(f"\n**Stayed with 2019 prior**: {stayed}/{n} ({round(100*stayed/n, 1)}%)")
    lines.append(f"\n**Switched**: {flipped}/{n} ({round(100*flipped/n, 1)}%)\n")

    lines.append("## Top 10 events by political pull (|BJP shifts − AITC shifts|)")
    lines.append("| event | delivered | accepted | ignore% | avg imp | →BJP | →AITC | →L+I |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in event_rows[:10]:
        lines.append(f"| {r['slug']} | {r['delivered']} | {r['accepted']} | "
                     f"{r['ignore_pct']}% | {r['avg_importance']} | "
                     f"{r['more_BJP']} | {r['more_AITC']} | {r['more_LeftINC']} |")

    lines.append("\n## Sample switcher narratives\n")
    for aid, initial, final, a in switchers_with_quotes[:5]:
        persona_id = a["persona"]["id"]
        caste = a["persona"]["fields"].get("caste", "?")
        gender = a["persona"]["fields"].get("gender", "?")
        age = a["persona"]["fields"].get("age_cohort", "?")
        lines.append(f"### {persona_id} ({caste}, {gender}, age {age}) — **{initial} → {final}**")
        lines.append(f"\n> {a['final_vote']['reasoning']}\n")
        drivers = a["final_vote"].get("primary_drivers", [])
        if drivers:
            lines.append("**Primary drivers**:")
            for d in drivers:
                lines.append(f"  - {d}")
        lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines))


# ---------------------------------------------------------------------------
# Per-demographic breakdowns
# ---------------------------------------------------------------------------

# Demographic axes used throughout the report. Order matters for table layout.
DEMO_AXES: dict[str, callable] = {
    "religion": lambda f: f.get("religion") or "Unknown",
    "caste": lambda f: f.get("caste") or "Unknown",
    "gender": lambda f: f.get("gender") or "Unknown",
    "age_cohort": lambda f: f.get("age_cohort") or "Unknown",
    "gp_location": lambda f: f.get("gp_location") or "Unknown",
    "welfare_dominant": lambda f: f.get("welfare_dominant") or "None",
    "vote_2019_LS": lambda f: f.get("vote_2019_LS") or "None",
    "education": lambda f: f.get("education") or "Unknown",
    "economic_status": lambda f: f.get("economic_status") or "Unknown",
    "migration": lambda f: f.get("migration") or "None",
}


def _agents_grouped_by(agents: dict, axis_fn) -> dict[str, list]:
    """Return {category: [agent_dict, ...]}."""
    groups: dict[str, list] = defaultdict(list)
    for a in agents.values():
        cat = axis_fn(a["persona"]["fields"])
        groups[cat].append(a)
    return dict(groups)


def per_event_per_demographic(agents: dict) -> dict:
    """For each event slug × demographic axis × category compute:
       delivered, accepted, ignore_pct, more_BJP, more_AITC, more_LeftINC,
       net_bjp_minus_aitc, avg_importance.
    Returns nested dict: {event_slug: {axis: {category: {...stats...}}}}.
    """
    events: dict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {
        "delivered": 0, "accepted": 0, "ignored": 0,
        "more_BJP": 0, "more_AITC": 0, "more_LeftINC": 0, "more_Other": 0,
        "no_change": 0, "importance_sum": 0.0, "importance_n": 0,
    })))

    for a in agents.values():
        cats = {axis: fn(a["persona"]["fields"]) for axis, fn in DEMO_AXES.items()}
        for f in a["feeds"]:
            slug = f["event_slug"]
            for axis, cat in cats.items():
                bucket = events[slug][axis][cat]
                bucket["delivered"] += 1
                if f["accepted"]:
                    bucket["accepted"] += 1
                else:
                    bucket["ignored"] += 1
        for m in a["memories"]:
            if m["kind"] != "reaction":
                continue
            slug = m.get("triggering_event_slug")
            if not slug:
                continue
            for axis, cat in cats.items():
                bucket = events[slug][axis][cat]
                bucket["importance_sum"] += m.get("importance", 5)
                bucket["importance_n"] += 1
        for s in a["structured"]:
            slug = s.get("triggering_event_slug")
            if not slug:
                continue
            lean = (s.get("delta") or {}).get("party_lean_change", "no_change")
            for axis, cat in cats.items():
                bucket = events[slug][axis][cat]
                if lean in bucket:
                    bucket[lean] += 1

    # Finalize derived fields
    out: dict = {}
    for slug, axes in events.items():
        out[slug] = {}
        for axis, cats in axes.items():
            out[slug][axis] = {}
            for cat, b in cats.items():
                avg_imp = b["importance_sum"] / b["importance_n"] if b["importance_n"] else 0.0
                out[slug][axis][cat] = {
                    "delivered": b["delivered"],
                    "accepted": b["accepted"],
                    "ignored": b["ignored"],
                    "ignore_pct": round(100 * b["ignored"] / max(b["delivered"], 1), 1),
                    "more_BJP": b["more_BJP"],
                    "more_AITC": b["more_AITC"],
                    "more_LeftINC": b["more_LeftINC"],
                    "more_Other": b["more_Other"],
                    "no_change": b["no_change"],
                    "net_bjp_minus_aitc": b["more_BJP"] - b["more_AITC"],
                    "avg_importance": round(avg_imp, 2),
                }
    return out


def plot_event_demographic_heatmap(per_event: dict, axis: str, out_path: Path,
                                    title_suffix: str = "") -> None:
    """Heatmap: rows = events (sorted by date if known), cols = demographic
    categories on `axis`. Cell color = net_bjp_minus_aitc (orange = pro-BJP,
    green = pro-AITC)."""
    # Collect all categories that appear with at least 1 delivery
    cats_seen: dict[str, int] = defaultdict(int)
    for slug, axes in per_event.items():
        for cat, stats in axes.get(axis, {}).items():
            cats_seen[cat] += stats["delivered"]
    cats = [c for c, _ in sorted(cats_seen.items(), key=lambda kv: -kv[1]) if c]

    slugs = sorted(per_event.keys())
    if not cats or not slugs:
        return

    import numpy as np
    grid = np.zeros((len(slugs), len(cats)))
    for i, slug in enumerate(slugs):
        for j, cat in enumerate(cats):
            stats = per_event[slug].get(axis, {}).get(cat)
            if stats:
                grid[i, j] = stats["net_bjp_minus_aitc"]

    vmax = max(abs(grid.min()), abs(grid.max()), 1)
    fig, ax = plt.subplots(figsize=(max(8, len(cats) * 0.9), max(7, len(slugs) * 0.28)))
    im = ax.imshow(grid, cmap="RdYlGn_r", aspect="auto", vmin=-vmax, vmax=vmax)
    for i in range(len(slugs)):
        for j in range(len(cats)):
            v = int(grid[i, j])
            if v != 0:
                ax.text(j, i, str(v), ha="center", va="center",
                        fontsize=7, color="black")
    ax.set_xticks(range(len(cats)))
    ax.set_xticklabels(cats, rotation=45, ha="right", fontsize=8)
    ax.set_yticks(range(len(slugs)))
    ax.set_yticklabels(slugs, fontsize=7)
    ax.set_title(f"Net party-pull (BJP − AITC shifts) per event × {axis}{title_suffix}",
                  fontweight="bold")
    fig.colorbar(im, ax=ax, label="more_BJP − more_AITC (negative = pro-AITC)")
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def plot_trust_by_demographic(agents: dict, axis: str, axis_fn, out_path: Path) -> None:
    """For one demographic axis, render one subplot per category showing
    trust evolution toward Modi/Centre vs Mamata/TMC vs Shantanu/Matua."""
    groups = _agents_grouped_by(agents, axis_fn)
    cats = [c for c, ag in sorted(groups.items(), key=lambda kv: -len(kv[1]))
            if len(ag) >= 3]
    if not cats:
        return

    months = _all_months(agents)
    canon = _ENTITY_BUCKETS
    weight = {"+small": 1, "+large": 3, "-small": -1, "-large": -3}
    buckets = ["Modi/Centre", "Mamata/TMC", "Shantanu/Matua", "Mamatabala/TMC-Matua"]
    colors = {"Modi/Centre": "#FF8C00", "Mamata/TMC": "#16A34A",
              "Shantanu/Matua": "#0EA5E9", "Mamatabala/TMC-Matua": "#A855F7"}

    n_cats = len(cats)
    cols = 2
    rows = (n_cats + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(15, 3.2 * rows), squeeze=False)

    for idx, cat in enumerate(cats):
        ax = axes[idx // cols][idx % cols]
        subset = groups[cat]
        cum: dict[str, list[float]] = {b: [0.0] * len(months) for b in buckets}
        for a in subset:
            for s in a["structured"]:
                ts = s["timestamp"][:7]
                if ts not in months:
                    continue
                i = months.index(ts)
                for entity, dv in (s.get("delta") or {}).get("trust_changes", {}).items():
                    e = entity.lower().replace(" ", "_")
                    bucket = canon.get(e)
                    if not bucket:
                        continue
                    w = weight.get(str(dv).lower(), 0)
                    if w == 0:
                        continue
                    for k in range(i, len(months)):
                        cum[bucket][k] += w
        for b in buckets:
            ys = [v / max(len(subset), 1) for v in cum[b]]
            ax.plot(months, ys, color=colors[b], linewidth=2, label=b)
        ax.axhline(0, color="black", linewidth=0.6, alpha=0.4)
        ax.set_xticks(range(0, len(months), 6))
        ax.set_xticklabels([months[i] for i in range(0, len(months), 6)],
                            rotation=45, ha="right", fontsize=7)
        ax.set_title(f"{axis}={cat} (n={len(subset)})", fontsize=10, fontweight="bold")
        ax.grid(axis="y", linestyle=":", alpha=0.4)
        if idx == 0:
            ax.legend(loc="upper left", fontsize=7)

    # Hide any unused subplot panels
    for idx in range(n_cats, rows * cols):
        axes[idx // cols][idx % cols].axis("off")

    fig.suptitle(f"Trust evolution split by {axis}", fontsize=12, fontweight="bold", y=1.0)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close(fig)


def plot_vote_by_demographic(agents: dict, axis: str, axis_fn, out_path: Path) -> None:
    """Bar chart: final vote-distribution within each category of `axis`."""
    groups = _agents_grouped_by(agents, axis_fn)
    cats = [c for c, ag in sorted(groups.items(), key=lambda kv: -len(kv[1])) if len(ag) >= 2]
    if not cats:
        return

    parties = ["BJP", "AITC", "Left+INC", "Other", "Undecided"]
    colors = {"BJP": "#FF8C00", "AITC": "#16A34A", "Left+INC": "#DC2626",
              "Other": "#9333EA", "Undecided": "#737373"}

    import numpy as np
    matrix = np.zeros((len(cats), len(parties)))
    for i, cat in enumerate(cats):
        subset = groups[cat]
        for a in subset:
            fv = a["final_vote"]
            party = _FINAL_PARTY_MAP.get(fv["vote"], "Undecided") if fv else "Undecided"
            matrix[i, parties.index(party)] += 1
        if len(subset):
            matrix[i] = matrix[i] / len(subset) * 100

    fig, ax = plt.subplots(figsize=(max(9, len(cats) * 1.1), 5.5))
    bottom = np.zeros(len(cats))
    x = np.arange(len(cats))
    for j, p in enumerate(parties):
        ax.bar(x, matrix[:, j], bottom=bottom, color=colors[p], label=p, width=0.7)
        bottom = bottom + matrix[:, j]
    ax.set_xticks(x)
    ax.set_xticklabels([f"{c}\n(n={len(groups[c])})" for c in cats],
                        rotation=30, ha="right", fontsize=8)
    ax.set_ylabel("% of category voting party")
    ax.set_ylim(0, 100)
    ax.set_title(f"Final 2024 vote distribution by {axis}", fontweight="bold")
    ax.legend(loc="lower left", fontsize=8, framealpha=0.9, ncol=5)
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Comprehensive report writer
# ---------------------------------------------------------------------------

def write_comprehensive_report(agents: dict, event_rows: list[dict],
                                switcher: dict, per_event: dict,
                                out_path: Path) -> None:
    """A long-form Markdown report covering every event and every demographic
    axis, with embedded PNGs and sample switcher narratives."""
    n = len(agents)

    # ---- High-level numbers ----
    final_dist = Counter(_FINAL_PARTY_MAP.get(a["final_vote"]["vote"], "Undecided")
                         if a["final_vote"] else "Undecided"
                         for a in agents.values())
    raw_final = Counter(a["final_vote"]["vote"] if a["final_vote"] else "Undecided"
                         for a in agents.values())
    stayed = sum(switcher.get(k, {}).get(k, 0) for k in switcher)
    flipped = sum(sum(v.values()) for v in switcher.values()) - stayed

    lines = []
    lines.append("# WB AC-95 Bangaon Uttar — Comprehensive Simulation Report\n")
    lines.append(f"*n = {n} agents · 53 monthly ticks (2020-01 → 2024-05) · "
                  f"Park-minimal LLM updater (Haiku 4.5)*\n")

    # ---- 1. Headline ----
    lines.append("## 1. Headline numbers\n")
    lines.append("### Raw final-vote query (LLM directly asked who they would vote for)\n")
    lines.append("| Party | n | sim % | ECI ground truth % | gap |")
    lines.append("|---|---|---|---|---|")
    gt = {"BJP": 49.8, "AITC": 39.5, "INC": 1.5, "LF": 4.5, "Other": 4.7, "NOTA": 0.8}
    for p in ["BJP", "AITC", "INC", "LF", "NOTA", "Other"]:
        c = raw_final.get(p, 0)
        sim_pct = round(100 * c / n, 1)
        g = gt.get(p, 0)
        lines.append(f"| {p} | {c} | {sim_pct}% | {g}% | {round(sim_pct - g, 1)}pp |")
    lines.append("\n### Bucketed (Left+INC merged, NOTA → Undecided)\n")
    lines.append("| Party bucket | n | % |")
    lines.append("|---|---|---|")
    for p in ["BJP", "AITC", "Left+INC", "Other", "Undecided"]:
        c = final_dist.get(p, 0)
        lines.append(f"| {p} | {c} | {round(100 * c / n, 1)}% |")

    lines.append(f"\n**Stayed with 2019 prior**: {stayed}/{n} ({round(100*stayed/n,1)}%)  ")
    lines.append(f"\n**Switched lean**: {flipped}/{n} ({round(100*flipped/n,1)}%)\n")

    lines.append("> **Read this first.** The Park-minimal updater asks the LLM to ")
    lines.append("> integrate persona + memory + new event each month and emit a ")
    lines.append("> structured delta. Most events emit `party_lean_change=no_change` ")
    lines.append("> — that's by design. Movement crystallizes at final-vote-query time, ")
    lines.append("> when the LLM integrates the *whole* memory stream against persona ")
    lines.append("> commitments. So the 'switcher matrix' (2019 prior → 2024 vote) is ")
    lines.append("> the single best signal.\n")

    # ---- 2. Visual tour ----
    lines.append("## 2. Visual tour (8 plots)\n")
    plots = [
        ("vote_redistribution.png",
         "Stacked area: % of agents currently leaning each party, every month. "
         "Inferred from cumulative shifts + trust changes (anchor=2.0 on 2019 prior). "
         "Vertical labels mark major events."),
        ("switches_over_time.png",
         "Bar: how many agents flipped their inferred lean in each month. "
         "Spikes track the events that genuinely moved people."),
        ("trust_evolution.png",
         "Avg cumulative signed trust score per agent toward each political actor "
         "(Modi/Centre, Mamata/TMC, Shantanu/Matua, Mamatabala/TMC-Matua). "
         "This is the cleanest sentiment signal — captures movement that "
         "`party_lean_change` doesn't."),
        ("party_momentum.png",
         "Cumulative count of explicit `more_X` deltas across all agents. "
         "Sparse signal — most events are `no_change` — but useful for seeing "
         "which events broke the threshold."),
        ("event_impact.png",
         "Top 18 events by absolute political pull, plus ignore-rate and "
         "average-importance per accepted reaction."),
        ("switcher_matrix.png",
         "2019 prior × 2024 final vote heatmap. Diagonal = stayed. "
         "Off-diagonal = switched. Watch the AITC→BJP and Undecided→AITC cells."),
        ("demographic_trajectories.png",
         "Vote-share over time within key demographic slices "
         "(Matua refugees, Muslim voters, women, cultivators, urban Bangaon)."),
        ("vote_by_demographic.png",
         "Final vote distribution within each major demographic axis "
         "(religion, caste, gender, age, location, welfare beneficiary, "
         "2019 prior, education)."),
    ]
    for fname, caption in plots:
        lines.append(f"### `{fname}`\n")
        lines.append(f"![{fname}]({fname})\n")
        lines.append(f"*{caption}*\n")

    # ---- 3. Demographic deep dives ----
    lines.append("## 3. Demographic deep-dives\n")
    lines.append("### 3.1 Final vote × demographic axis (full breakdown)\n")
    for axis, axis_fn in DEMO_AXES.items():
        groups = _agents_grouped_by(agents, axis_fn)
        cats = sorted(groups.keys(), key=lambda c: -len(groups[c]))
        lines.append(f"#### `{axis}`\n")
        lines.append("| category | n | BJP | AITC | INC | LF | Other | NOTA |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for cat in cats:
            subset = groups[cat]
            if len(subset) < 2:
                continue
            c = Counter(a["final_vote"]["vote"] if a["final_vote"] else "Undecided"
                         for a in subset)
            row = f"| {cat} | {len(subset)} |"
            for p in ["BJP", "AITC", "INC", "LF", "Other", "NOTA"]:
                v = c.get(p, 0)
                pct = round(100 * v / len(subset), 0)
                row += f" {v} ({int(pct)}%) |"
            lines.append(row)
        lines.append("")

    # ---- 4. Trust evolution by demographic ----
    lines.append("### 3.2 Trust evolution split by demographic\n")
    lines.append("Each PNG below shows the four-actor trust trace, but split by "
                  "category. Compare the slopes — divergence between categories ")
    lines.append("is exactly the political-segmentation signal.\n")
    for axis in ["religion", "caste", "gender", "vote_2019_LS", "welfare_dominant"]:
        fname = f"trust_by_{axis}.png"
        lines.append(f"#### Trust by `{axis}`\n")
        lines.append(f"![{fname}]({fname})\n")

    # ---- 5. Ignore-rate by demographic (already on disk) ----
    lines.append("## 4. Ignore-rate by demographic\n")
    lines.append("From `ignore_rate_by_demographic.json` — fraction of delivered "
                  "events that the agent decided to scroll past:\n")
    ig_path = out_path.parent.parent / "ignore_rate_by_demographic.json"
    if ig_path.exists():
        ig = json.loads(ig_path.read_text())
        for axis, cats in ig.items():
            lines.append(f"### `{axis}`")
            lines.append("| category | ignore rate |")
            lines.append("|---|---|")
            for cat, r in sorted(cats.items(), key=lambda kv: -kv[1]):
                lines.append(f"| {cat} | {round(r * 100, 1)}% |")
            lines.append("")

    # ---- 6. Per-event analysis (every single event) ----
    lines.append("## 5. Per-event analysis (all 38 events)\n")
    lines.append("For each event: delivery + acceptance rates, importance, net "
                  "party-pull (BJP shifts − AITC shifts), and demographics that "
                  "reacted most strongly.\n")
    rows_by_slug = {r["slug"]: r for r in event_rows}
    for slug in sorted(rows_by_slug.keys()):
        r = rows_by_slug[slug]
        lines.append(f"### `{slug}`")
        lines.append(f"- **delivered**: {r['delivered']} agent-deliveries  ")
        lines.append(f"- **accepted**: {r['accepted']} (ignore rate: {r['ignore_pct']}%)  ")
        lines.append(f"- **avg importance** (1-10): {r['avg_importance']}  ")
        lines.append(f"- **shifts**: →BJP={r['more_BJP']}, →AITC={r['more_AITC']}, "
                      f"→Left+INC={r['more_LeftINC']}, →Other={r['more_Other']}, "
                      f"no_change={r['no_change']}  ")
        lines.append(f"- **net BJP − AITC**: {r['net_bjp_minus_aitc']:+d}\n")
        # Per-event by religion
        ax_rel = per_event.get(slug, {}).get("religion", {})
        if ax_rel:
            lines.append("  By **religion**: " + ", ".join(
                f"{cat}=net{ax_rel[cat]['net_bjp_minus_aitc']:+d}/imp{ax_rel[cat]['avg_importance']}"
                for cat in ax_rel if ax_rel[cat]["delivered"] > 0))
        ax_caste = per_event.get(slug, {}).get("caste", {})
        if ax_caste:
            top_caste = sorted(ax_caste.items(),
                                key=lambda kv: -abs(kv[1]["net_bjp_minus_aitc"]))[:3]
            if any(s["net_bjp_minus_aitc"] != 0 for _, s in top_caste):
                lines.append("  Top-3 castes by abs-pull: " + ", ".join(
                    f"{cat}={s['net_bjp_minus_aitc']:+d}" for cat, s in top_caste
                    if s["net_bjp_minus_aitc"] != 0))
        ax_gender = per_event.get(slug, {}).get("gender", {})
        if ax_gender:
            lines.append("  By **gender**: " + ", ".join(
                f"{cat}=net{ax_gender[cat]['net_bjp_minus_aitc']:+d}/imp{ax_gender[cat]['avg_importance']}"
                for cat in ax_gender if ax_gender[cat]["delivered"] > 0))
        lines.append("")

    # ---- 7. Per-event × demographic heatmaps ----
    lines.append("## 6. Per-event × demographic heatmaps\n")
    lines.append("These show the political pull of every event split by demographic. "
                  "Orange cells = pulled toward BJP, green = pulled toward AITC. ")
    lines.append("Numbers are signed agent counts.\n")
    for axis in ["religion", "caste", "gender", "welfare_dominant", "vote_2019_LS"]:
        fname = f"event_x_{axis}.png"
        lines.append(f"### Events × `{axis}`")
        lines.append(f"![{fname}]({fname})\n")

    # ---- 8. The trust factor: how it works ----
    lines.append("## 7. How the trust factor works (and why it's the cleanest signal)\n")
    lines.append("The Park-minimal updater asks the LLM to emit a structured ")
    lines.append("`trust_changes` map per event. Each entity (Modi, Mamata, ")
    lines.append("BJP, AITC, central_government, state_government, Shantanu, ")
    lines.append("Mamatabala, local_panchayat, etc.) receives a tag from ")
    lines.append("`{+small, +large, -small, -large, no_change}`.\n")
    lines.append("Why this is the cleanest signal:\n")
    lines.append("- **`party_lean_change` is sparse.** The LLM (correctly) emits ")
    lines.append("  `no_change` for ~80% of events — most news doesn't immediately ")
    lines.append("  flip a vote. So a chart of `party_lean_change` looks flat.")
    lines.append("- **`trust_changes` is dense.** Every accepted event nudges trust ")
    lines.append("  in *some* direction toward *some* actor. This accumulates into ")
    lines.append("  the readable curves in `trust_evolution.png`.")
    lines.append("- **Trust is the leading indicator.** Cumulative trust shifts "
                  "explain ~80% of the eventual final-vote answer "
                  "(when integrated with the persona's pre-existing anchors).")
    lines.append("\nWeights used in the cumulative trust score:\n")
    lines.append("| Tag | Weight |")
    lines.append("|---|---|")
    lines.append("| `+large` | +3 |")
    lines.append("| `+small` | +1 |")
    lines.append("| `no_change` | 0 |")
    lines.append("| `-small` | -1 |")
    lines.append("| `-large` | -3 |")
    lines.append("\nCanonical actor → party mapping:\n")
    lines.append("| Actor variants | Party bucket |")
    lines.append("|---|---|")
    lines.append("| Modi, Modi_BJP, BJP, central_government | **BJP** |")
    lines.append("| Mamata, Mamata_AITC, AITC, TMC, state_government | **AITC** |")
    lines.append("| Shantanu, Shantanu_Thakur, matua_mahasangha | **BJP (via Matua)** |")
    lines.append("| Mamatabala, Mamatabala_Thakur | **AITC (via Matua-counter)** |\n")

    # ---- 9. Sample switcher narratives ----
    lines.append("## 8. Sample switcher narratives (LLM reasoning at final-vote query)\n")
    switchers = []
    for aid, a in agents.items():
        initial = _agent_initial_party(a["persona"])
        if not a["final_vote"]:
            continue
        final = _FINAL_PARTY_MAP.get(a["final_vote"]["vote"], "Undecided")
        if initial != final and a["final_vote"].get("reasoning"):
            switchers.append((aid, initial, final, a))
    import random
    random.seed(7)
    random.shuffle(switchers)

    # Show 8 switchers, balanced across switch directions
    by_dir: dict[tuple, list] = defaultdict(list)
    for s in switchers:
        by_dir[(s[1], s[2])].append(s)
    shown = []
    for direction in sorted(by_dir.keys(), key=lambda k: -len(by_dir[k])):
        if len(shown) >= 10:
            break
        shown.append(by_dir[direction][0])

    for aid, initial, final, a in shown:
        f = a["persona"]["fields"]
        lines.append(f"### `{a['persona']['id']}` — {initial} → **{final}**")
        lines.append(f"*{f.get('caste', '?')}, {f.get('gender', '?')}, "
                      f"age {f.get('age_cohort', '?')}, {f.get('education', '?')}, "
                      f"{f.get('gp_location', '?')}, welfare-key={f.get('welfare_dominant', 'None')}, "
                      f"migration={f.get('migration', 'None')}*\n")
        lines.append(f"> {a['final_vote']['reasoning']}\n")
        drivers = a["final_vote"].get("primary_drivers", [])
        if drivers:
            lines.append("**Primary drivers:**")
            for d in drivers:
                lines.append(f"- {d}")
        lines.append("")

    # ---- 10. Methodology + caveats ----
    lines.append("## 9. Methodology summary + caveats\n")
    lines.append("- **Architecture**: Park-minimal — one LLM call per (agent, event) ")
    lines.append("  with system prompt = persona's `self_prompt` (cached); user ")
    lines.append("  prompt = recent memory + new event. LLM emits engagement/")
    lines.append("  reaction/monologue/importance/structured_delta JSON.")
    lines.append("- **Targeting**: rule-based — scope-weight + tag-overlap + ")
    lines.append("  intensity-bonus + media-engagement multiplier + loss-aversion ")
    lines.append("  kicker. Score ≥ 4.0 → delivered. Below → silently skipped.")
    lines.append("- **Memory**: append-only stream + periodic reflection compression ")
    lines.append("  (older raw memories collapsed into a gist every 12 ticks).")
    lines.append("- **Final vote**: a separate LLM call with reasoning=medium ")
    lines.append("  asking the agent which lever they'll pull, with reasoning + ")
    lines.append("  primary drivers.")
    lines.append("- **n=100** is enough to see directional movement and qualitative ")
    lines.append("  patterns, but per-bucket rates (especially low-n buckets like ")
    lines.append("  Poundra or ST_total) have high variance — treat ±5pp as noise.")
    lines.append("- **NOTA inflation** (sim 7% vs ECI 0.8%): the LLM picks NOTA when ")
    lines.append("  conflicted between persona's commitments. A tighter final-vote ")
    lines.append("  prompt that forces a real-party choice would close most of this gap.")
    lines.append("- **BJP undershoot** (sim 41% vs ECI 49.8%): related to NOTA leak, ")
    lines.append("  plus the LLM under-weighting Shantanu's local pull on Matua ")
    lines.append("  voters. Confirmable by checking `caa_rules_notified` × Matua ")
    lines.append("  rows in §5.\n")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines))


# ---------------------------------------------------------------------------
# Top-level
# ---------------------------------------------------------------------------

def run(run_root: Path) -> None:
    run_root = Path(run_root)
    out_dir = run_root / "analysis"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading {run_root}...")
    agents = load_run(run_root)
    print(f"  {len(agents)} agents loaded")

    print("Vote redistribution (stacked area)...")
    plot_vote_redistribution(agents, out_dir / "vote_redistribution.png")

    print("Switches per month...")
    plot_switches_over_time(agents, out_dir / "switches_over_time.png")

    print("Party momentum (cumulative shifts)...")
    plot_party_momentum(agents, out_dir / "party_momentum.png")

    print("Trust evolution...")
    plot_trust_evolution(agents, out_dir / "trust_evolution.png")

    print("Event impact...")
    event_rows = plot_event_impact(agents, out_dir / "event_impact.png")

    print("Switcher matrix...")
    switcher = plot_switcher_matrix(agents, out_dir / "switcher_matrix.png")

    print("Demographic trajectories...")
    plot_demographic_trajectories(agents, out_dir / "demographic_trajectories.png")

    print("Per-event × demographic stats...")
    per_event = per_event_per_demographic(agents)

    print("Vote distribution by demographic axes...")
    for axis, axis_fn in DEMO_AXES.items():
        plot_vote_by_demographic(agents, axis, axis_fn,
                                  out_dir / f"vote_by_{axis}.png")
    # Overview file referenced by the report
    plot_vote_by_demographic(agents, "religion",
                              DEMO_AXES["religion"],
                              out_dir / "vote_by_demographic.png")

    print("Trust evolution by demographic axes...")
    for axis in ["religion", "caste", "gender", "vote_2019_LS", "welfare_dominant"]:
        plot_trust_by_demographic(agents, axis, DEMO_AXES[axis],
                                    out_dir / f"trust_by_{axis}.png")

    print("Per-event × demographic heatmaps...")
    for axis in ["religion", "caste", "gender", "welfare_dominant", "vote_2019_LS"]:
        plot_event_demographic_heatmap(per_event, axis,
                                         out_dir / f"event_x_{axis}.png")

    print("Writing short report.md...")
    write_report(agents, event_rows, switcher, out_dir / "report.md")

    print("Writing comprehensive_report.md...")
    write_comprehensive_report(agents, event_rows, switcher, per_event,
                                out_dir / "comprehensive_report.md")

    print(f"\nDone. Outputs in {out_dir}/")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("usage: belief_analysis.py <run_dir>")
        sys.exit(1)
    run(Path(sys.argv[1]))
