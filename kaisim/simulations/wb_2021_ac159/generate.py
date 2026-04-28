"""Generate a persona set for AC 159 from a persona_config.

Usage:
    python kaisim/simulations/wb_2021_ac159/generate.py baseline_rule
"""
from __future__ import annotations

import sys
from pathlib import Path

KAISIM = Path(__file__).resolve().parents[2]
if str(KAISIM) not in sys.path:
    sys.path.insert(0, str(KAISIM))

try:
    from dotenv import load_dotenv
    load_dotenv(KAISIM / ".env")
except ImportError:
    pass

from pipeline.core.config import PersonaConfig, SimulationContext
from pipeline.core.persona_set import PersonaSet
from pipeline.persona_generation.samplers import make_sampler
from pipeline.verifiers.partial import (verify_partial_population,
                                          render_partial_md)


def main():
    if len(sys.argv) < 2:
        print("usage: generate.py <persona_config_name>")
        sys.exit(2)
    config_name = sys.argv[1]

    sim_dir = Path(__file__).parent
    config_path = sim_dir / "persona_configs" / f"{config_name}.yaml"
    if not config_path.exists():
        print(f"ERROR: no persona config at {config_path}")
        sys.exit(2)

    ctx = SimulationContext.load(sim_dir)
    cfg = PersonaConfig.load(sim_dir, config_path)
    print(f"sim={sim_dir.name}  config={config_name}  set={cfg.set_name}")
    print(f"  axes={len(ctx.axes)}  joints={len(ctx.joints)}  "
          f"target_n={cfg.target_n}")

    SamplerCls = make_sampler(cfg.sampler)
    seed = cfg.raw.get("generation", {}).get("seed")
    sampler = SamplerCls(ctx, cfg, seed=seed)

    out = sim_dir / "personas" / cfg.set_name
    out.mkdir(parents=True, exist_ok=True)

    if hasattr(sampler, "dag"):
        print("\nDAG order:")
        for name in sampler.dag.topo_order:
            print(f"  {name}")
    print()

    personas = sampler.sample_many(cfg.target_n)
    print(f"\n  generated {len(personas)} personas")

    tol = cfg.get("verifier.tolerance") or None
    weights = cfg.get("verifier.tier_weights") or None
    report = verify_partial_population(ctx, personas, tolerance=tol,
                                          tier_weights=weights)
    h = report.headline()
    print(f"\n{h}")

    pset = PersonaSet(name=cfg.set_name, personas=personas, config_snapshot=cfg.raw)
    pset.update_meta(sampler=cfg.sampler, verifier_summary=h)
    pset.save(out)
    (out / "reports").mkdir(exist_ok=True)
    (out / "reports" / "FINAL.md").write_text(render_partial_md(report))
    print(f"\nwrote: {out}")


if __name__ == "__main__":
    main()
