"""Generate `prompts/system_anchors.md` for the 9 non-095 ACs from each AC's
constituency-data MD. Distributional analysis showed AC 095 (the only one
with a hand-written system_anchors.md) had ~30× more news engagement per
agent than the others; populating this file for every AC closes the gap.

Output content (one file per AC):
  - From MD §A (Identity): AC number, name, district, LS, sub-units
  - From MD §F (Pre-2019 history): vote history snapshot
  - Short prose "what defines this AC" pulled from MD §A note + §C.16
    migration note where helpful.

We do NOT pull §H (post-2019 anchors) — the system_anchors block is
2019-frozen pre-period context, mirroring AC 095's hand-written file.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]                # kaisim/
SIMS_DIR = ROOT / "simulations"
GT_PATH = SIMS_DIR / "_phase2_2021/ground_truth_2021.yaml"
CONST_DIR = ROOT.parent / "constituency_data/constituencies"


def section(md: str, heading_re: str) -> str:
    """Extract content between a heading (matched by regex on its line) and the
    next top-level `## ` heading. Returns "" if not found."""
    m = re.search(rf"^{heading_re}\s*\n", md, flags=re.MULTILINE)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^## ", md[start:], flags=re.MULTILINE)
    end = start + nxt.start() if nxt else len(md)
    return md[start:end].strip()


def render_anchors(ac_dir_name: str, gt_for_ac: dict) -> str:
    ac_num, *rest = ac_dir_name.split("_", 1)
    name_pretty = gt_for_ac["name"]
    md_path = CONST_DIR / ac_dir_name / "2019" / f"{ac_num}_{rest[0] if rest else ''}_2019.md"
    md = md_path.read_text() if md_path.exists() else ""

    identity = section(md, r"## A\. Identity.*")
    history  = section(md, r"## F\. Pre-2019 vote history.*")

    # Headline 2019 LS facts from the ground-truth — useful for the LLM
    # without leaking 2021 results.

    parts = [
        f"## What this simulation is",
        "",
        f"You are populating **AC {int(ac_num)} — {name_pretty}** with synthetic voter "
        f"personas calibrated to **end-2019** demographic conditions. The downstream "
        f"simulation feeds news from 2019 → 2021 to each persona, then asks them how "
        f"they vote in the 2021 West Bengal Legislative Assembly Election.",
        "",
        f"## Identity (from canonical MD §A)",
        "",
        identity if identity else f"_(no §A in {md_path.name})_",
        "",
        f"## Pre-2019 vote history (from canonical MD §F)",
        "",
        history if history else f"_(no §F in {md_path.name})_",
        "",
        f"## What's at stake in 2019",
        "",
        f"The dominant political axis in West Bengal at end-2019 is the BJP-vs-TMC "
        f"contest, with the Congress + Left bloc collapsing toward irrelevance in "
        f"most ACs but holding pockets. The CAB/CAA passage in December 2019 is the "
        f"single largest force on the citizenship axis — strongly polarizing among "
        f"Hindu refugees from Bangladesh and the Muslim community.",
        "",
        f"State-wide TMC welfare stack active by end-2019: Khadya Sathi (PDS), "
        f"Swasthya Sathi (insurance), Kanyashree (girl-student stipend), Sabuj Sathi "
        f"(school-bicycle), Krishak Bandhu (cultivator transfer, just launched Jan 2019). "
        f"**Lakshmir Bhandar (women's monthly cash transfer) does NOT exist yet at "
        f"end-2019** — it was announced Feb 2021 and launched Aug 2021. Do not reference it.",
    ]
    return "\n".join(parts)


def main():
    gt = yaml.safe_load(GT_PATH.read_text())["constituencies"]
    written = 0
    for ac_dir_name, gt_for_ac in gt.items():
        ac_num = ac_dir_name.split("_", 1)[0]
        sim_dir = SIMS_DIR / f"wb_2021_ac{ac_num}"
        prompts_dir = sim_dir / "prompts"
        prompts_dir.mkdir(parents=True, exist_ok=True)
        out = prompts_dir / "system_anchors.md"

        # Don't overwrite AC 095's hand-written one.
        if ac_num == "095" and out.exists():
            continue

        out.write_text(render_anchors(ac_dir_name, gt_for_ac))
        written += 1
        print(f"wrote {out}  ({out.stat().st_size} bytes)")
    print(f"\nWrote {written} system_anchors.md files (AC 095's hand-written copy preserved).")


if __name__ == "__main__":
    main()
