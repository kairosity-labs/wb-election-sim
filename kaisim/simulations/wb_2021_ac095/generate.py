"""Generate a persona set from a persona_config.

Usage:
    python kaisim/simulations/wb_2021_ac095/generate.py baseline_rule
    python kaisim/simulations/wb_2021_ac095/generate.py default      # LLM

Reads persona_configs/<name>.yaml, runs the configured sampler, verifies the
population, and writes everything to personas/<set_name>/.
LLM samplers archive raw responses + per-batch reports under batches/ and reports/.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Make pipeline + simulations importable.
KAISIM = Path(__file__).resolve().parents[2]
if str(KAISIM) not in sys.path:
    sys.path.insert(0, str(KAISIM))

# Load .env (kaisim/.env) before any provider is constructed.
from dotenv import load_dotenv
load_dotenv(KAISIM / ".env")

from pipeline.core.config import PersonaConfig, SimulationContext
from pipeline.core.persona_set import PersonaSet
from pipeline.persona_generation.samplers import make_sampler
from pipeline.verifiers import render_md, verify_population


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
    print(f"  axes={len(ctx.axes)}  joints={len(ctx.joints)}  sampler={cfg.sampler}  "
          f"target_n={cfg.target_n}")

    SamplerCls = make_sampler(cfg.sampler)
    seed = cfg.raw.get("generation", {}).get("seed")
    sampler = SamplerCls(ctx, cfg, seed=seed)

    # Pre-create the persona-set output directory so LLM sampler can stream
    # batches/reports there during generation.
    out = sim_dir / "personas" / cfg.set_name
    out.mkdir(parents=True, exist_ok=True)
    if hasattr(sampler, "attach_artifact_dir"):
        sampler.attach_artifact_dir(out)

    # Print DAG order if the sampler exposes one (rule-based does).
    if hasattr(sampler, "dag"):
        print("\nDAG order:")
        for name in sampler.dag.topo_order:
            ps = sampler.dag.parents_of(name)
            print(f"  {name:25s}  parents={ps}")
    print()

    personas = sampler.sample_many(cfg.target_n)
    print(f"\n  generated {len(personas)} personas")

    tol = cfg.get("verifier.tolerance") or None
    weights = cfg.get("verifier.tier_weights") or None
    report = verify_population(ctx, personas, tolerance=tol, tier_weights=weights)
    print(f"\n{report.headline()}")

    pset = PersonaSet(name=cfg.set_name, personas=personas, config_snapshot=cfg.raw)
    pset.update_meta(sampler=cfg.sampler, verifier_summary=report.headline(),
                     extra={"provider": getattr(sampler, "provider_name", None),
                            "model": getattr(getattr(sampler, "provider", None), "model", None)}
                            if cfg.sampler == "llm_batch" else None)
    pset.save(out)
    (out / "reports" / "FINAL.md").write_text(render_md(report))
    print(f"\nwrote: {out}")


if __name__ == "__main__":
    main()
