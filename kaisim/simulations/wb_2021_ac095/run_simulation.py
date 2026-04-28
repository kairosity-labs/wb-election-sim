"""Run the simulation pipeline on a persona set with a chosen config.

Usage:
    python kaisim/simulations/wb_2021_ac095/run_simulation.py <config_name>

Example:
    python kaisim/simulations/wb_2021_ac095/run_simulation.py rule_based

Loads:
  - simulation_configs/<config>.yaml
  - personas/<persona_set>/personas.jsonl
  - news/events_2019_2024.yaml
Writes:
  - runs/<timestamp>_<config>/agents/<id>/{persona,memory_stream,belief_narrative,...}
  - runs/<timestamp>_<config>/{summary,vote_distribution,...}.json
  - runs/<timestamp>_<config>/plots/vote_distribution.png
"""
from __future__ import annotations

import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

KAISIM = Path(__file__).resolve().parents[2]
if str(KAISIM) not in sys.path:
    sys.path.insert(0, str(KAISIM))

from dotenv import load_dotenv
load_dotenv(KAISIM / ".env")

from pipeline.core.persona_set import PersonaSet
from pipeline.simulation import analytics
from pipeline.simulation.core.config import SimulationConfig
from pipeline.simulation.core.event import NewsPool
from pipeline.simulation.orchestrator import Orchestrator


async def main_async(config_name: str):
    sim_dir = Path(__file__).parent
    config_path = sim_dir / "simulation_configs" / f"{config_name}.yaml"
    if not config_path.exists():
        print(f"ERROR: no simulation config at {config_path}")
        sys.exit(2)

    cfg = SimulationConfig.load(sim_dir, config_path)
    print(f"sim={sim_dir.name}  config={config_name}  set={cfg.persona_set_name}")

    # Load persona set
    persona_set_dir = sim_dir / "personas" / cfg.persona_set_name
    pset = PersonaSet.load(persona_set_dir)
    print(f"Loaded {len(pset)} personas from {persona_set_dir.name}")

    # Load news pool — union per-AC events.yaml + state_events.yaml
    yaml_paths = cfg.events_files
    pool = NewsPool.from_yamls(yaml_paths)
    print(f"Loaded {len(pool)} events from {len(yaml_paths)} file(s); "
           f"cutoff {pool.cutoff_date}")
    for p in yaml_paths:
        print(f"  · {p}")

    # Region-specific tagging
    sys.path.insert(0, str(sim_dir))
    from derived.persona_tags import derive_tags, derive_media_engagement

    # Output directory
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    out_root = sim_dir / "runs" / f"{ts}_{config_name}"
    out_root.mkdir(parents=True, exist_ok=True)
    print(f"Writing to {out_root}\n")

    # Save snapshot of config for reproducibility
    (out_root / "config.snapshot.yaml").write_text(config_path.read_text())

    # Run the simulation
    orch = Orchestrator(
        config=cfg,
        derive_tags_fn=derive_tags,
        derive_media_engagement_fn=derive_media_engagement,
        verbose=True,
    )
    summary = await orch.run(pset, pool, out_root)

    # Run analytics
    print("\n=== Analytics ===")
    gt = cfg.get("ground_truth")
    analytics.run_all(out_root, ground_truth=gt)
    print(f"Final vote distribution: {summary['vote_distribution']}")
    print(f"Ignore rate: {summary['ignore_rate']}")
    print(f"\nDone. Run dir: {out_root}")


def main():
    if len(sys.argv) < 2:
        print("usage: run_simulation.py <config_name>")
        sys.exit(2)
    config_name = sys.argv[1]
    asyncio.run(main_async(config_name))


if __name__ == "__main__":
    main()
