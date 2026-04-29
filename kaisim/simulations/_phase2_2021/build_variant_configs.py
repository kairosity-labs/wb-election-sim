"""Build 3 simulation_config variants × 10 ACs = 30 YAML files for Phase 2.

Reads ground_truth_2021.yaml (per-AC poll dates + candidates) and writes:

    simulations/wb_2021_ac<NN>/simulation_configs/
        2021_targeted.yaml         — rule_based targeting (default 2019→2021 setup)
        2021_show_all.yaml         — every agent sees every event (capped 10/period)
        2021_blind_to_prior.yaml   — rule_based but bjp_supporter/tmc_supporter masked,
                                     loss-aversion disabled

All three variants share:
    - persona_set: local_qwen_n100              (the K=2 set we just built)
    - clock: 2020-01-01 → AC's poll_date
    - LLM: openai-compat sglang Qwen3.5-9B at localhost:30000
    - high concurrency (max_concurrent_personas=80) so every agent's HTTP
      call rides the same multiplexed sglang queue
"""
from __future__ import annotations

import calendar
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]            # kaisim/
SIMS_DIR = ROOT / "simulations"
GT_PATH  = ROOT / "simulations/_phase2_2021/ground_truth_2021.yaml"


# ---------- helpers ----------------------------------------------------

def humanize(iso_date: str) -> str:
    """ '2021-04-17' -> '17 April 2021' """
    d = date.fromisoformat(iso_date)
    return f"{d.day} {calendar.month_name[d.month]} {d.year}"


def build_election_context(ac_dir_name: str, ac_data: dict) -> dict:
    """Shape the per-AC candidate list for the final_vote.md.j2 template."""
    candidates = {}
    for party, info in ac_data["candidates"].items():
        c = {"name": info.get("name", "—")}
        if info.get("won"):
            c["note"] = "winner"
        candidates[party] = c
    return {
        "ac_name": ac_data["name"],
        "poll_date_human": humanize(ac_data["poll_date"]),
        "election_label": "2021 West Bengal Legislative Assembly Election",
        "candidates": candidates,
    }


def build_ground_truth_pcts(ac_data: dict) -> dict[str, float]:
    """For analytics.run_all — flat party→pct dict."""
    out = {}
    for party, info in ac_data["candidates"].items():
        if isinstance(info.get("pct"), (int, float)):
            out[party] = float(info["pct"])
    return out


# ---------- per-variant config bodies ----------------------------------

COMMON_LLM = {
    "provider": "openai",
    "model": "Qwen/Qwen3.5-9B",
    "base_url": "http://localhost:30000/v1",
    "api_key": "EMPTY",
    "reasoning": None,
    "temperature": 0.7,
    "max_tokens": 4000,
    "cache_system_prompt": True,
}

COMMON_EXECUTION = {
    "async": True,
    "max_concurrent_personas": 80,    # 30 sims × 80 = 2400 in-flight ceiling;
                                       # sglang max_running_req=405/replica × 8 = 3240
}


def variant_targeted(ac_dir_name: str, ac_data: dict) -> dict:
    return {
        "simulation": {
            "name": f"{ac_dir_name}_2021_targeted",
            "description": "tag_match: pure agent_tags ∩ event_tags delivery. No cap.",
        },
        "ac_id": ac_dir_name,
        "input": {"persona_set": "local_qwen_n100"},
        "clock": {
            "start_date": "2020-01-01",
            "end_date":   ac_data["poll_date"],
            "tick_unit":  "month",
            "tick_size":  1,
            "reflection_every_n_ticks": 6,    # twice in the 16-month window
        },
        "targeting": {
            "strategy": "tag_match",
            "config": {},                     # no cap, no threshold, no weights
        },
        "update":     {"style": "park_minimal"},
        "reflection": {"enabled": True, "every_n_ticks": 6, "compression_target_tokens": 200},
        "llm":        COMMON_LLM,
        "execution":  COMMON_EXECUTION,
        "output":     {"runs_dir": "runs", "save_raw_responses": True, "save_feeds_audit": True},
        "election_context": build_election_context(ac_dir_name, ac_data),
        "ground_truth":     build_ground_truth_pcts(ac_data),
    }


def variant_show_all(ac_dir_name: str, ac_data: dict) -> dict:
    cfg = variant_targeted(ac_dir_name, ac_data)
    cfg["simulation"] = {
        "name": f"{ac_dir_name}_2021_show_all",
        "description": "show_all targeting — every agent receives every event. No cap.",
    }
    cfg["targeting"] = {
        "strategy": "show_all",
        "config": {},                       # no cap
    }
    return cfg


def variant_blind_to_prior(ac_dir_name: str, ac_data: dict) -> dict:
    cfg = variant_targeted(ac_dir_name, ac_data)
    cfg["simulation"] = {
        "name": f"{ac_dir_name}_2021_blind_to_prior",
        "description": "tag_match, but bjp/tmc/left_inc supporter tags masked from agent.",
    }
    cfg["targeting"] = {
        "strategy": "tag_match",
        "config": {"mask_tags": ["bjp_supporter", "tmc_supporter", "left_inc_supporter"]},
    }
    return cfg


VARIANTS = {
    "2021_targeted":        variant_targeted,
    "2021_show_all":        variant_show_all,
    "2021_blind_to_prior":  variant_blind_to_prior,
}


def main():
    gt = yaml.safe_load(GT_PATH.read_text())
    constituencies = gt["constituencies"]

    written = 0
    for ac_dir_name, ac_data in constituencies.items():
        ac_num = ac_dir_name.split("_", 1)[0]
        sim_dir = SIMS_DIR / f"wb_2021_ac{ac_num}/simulation_configs"
        sim_dir.mkdir(parents=True, exist_ok=True)
        for variant_name, builder in VARIANTS.items():
            body = builder(ac_dir_name, ac_data)
            out = sim_dir / f"{variant_name}.yaml"
            with out.open("w") as f:
                yaml.dump(body, f, sort_keys=False, default_flow_style=False, width=88)
            written += 1
    print(f"Wrote {written} variant configs across {len(constituencies)} ACs.")


if __name__ == "__main__":
    main()
