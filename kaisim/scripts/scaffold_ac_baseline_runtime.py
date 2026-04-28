#!/usr/bin/env python3
"""
scaffold_ac_baseline_runtime.py
For each non-095 AC, create the runtime scaffolding the rule_based sampler
needs to actually generate a baseline population:

  simulations/wb_2021_ac<NN>/
    derived/__init__.py
    derived/marital_sampling.py            (re-exports generic_plugins.marital_sample)
    derived/workforce_sampling.py
    derived/occupation_sampling.py
    derived/asset_sampling.py
    derived/amenity_sampling.py
    persona_configs/baseline_rule.yaml     (DAG + sampling spec, no welfare/blending)
    generate.py                            (sim entry point — same as 095's)

These thin wrappers keep the sampler's plugin loader happy while delegating
all actual logic to pipeline/persona_generation/generic_plugins.py.

For ACs that already hand-curated `derived/` and/or `persona_configs/` (just
AC 095 today), the scaffolder skips them — use --force to overwrite.

Run:
    python3 scripts/scaffold_ac_baseline_runtime.py --all
    python3 scripts/scaffold_ac_baseline_runtime.py 003
"""
from __future__ import annotations

import argparse
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIMS_DIR = ROOT / "simulations"

# Non-095 ACs only; 095 has its own hand-curated derived + configs.
PROTECTED_ACS = {"095"}


PLUGIN_TEMPLATES = {
    "marital_sampling.py": (
        "marital_sample as sample",
        "Marital status sampler (generic delegate).",
    ),
    "workforce_sampling.py": (
        "workforce_sample as sample",
        "Workforce-status sampler (generic delegate).",
    ),
    "occupation_sampling.py": (
        "occupation_sample as sample, class_of_worker_sample as class_of_worker",
        "Occupation + class-of-worker samplers (generic delegate).",
    ),
    "asset_sampling.py": (
        "asset_sample as sample",
        "Asset-flag sampler (generic delegate).",
    ),
    "amenity_sampling.py": (
        "amenity_sample as sample",
        "Amenities-flag sampler (generic delegate).",
    ),
}


BASELINE_RULE_YAML = """\
# Auto-scaffolded baseline persona config for AC {ac}.
# Uses generic plugins from pipeline.persona_generation.generic_plugins —
# AC-agnostic, joint-driven, no per-scheme welfare logic.
# Hand-edit per AC for production runs (e.g. AC 095's baseline_rule.yaml).

persona_set:
  name: "baseline_rule_n{n}"
  description: "Rule-based baseline persona set for AC {ac}, n={n}."

generation:
  sampler: "rule_based"
  target_n: {n}
  batch_size: {n}
  seed: 42

sampling_spec:
  gp_location:           {{method: marginal}}
  age_cohort:            {{method: marginal}}
  gender:                {{method: marginal}}
  household_composition: {{method: marginal}}
  economic_status:       {{method: marginal}}

  religion:
    method: conditional_categorical
    joint:  religion_given_gp

  caste:
    method: conditional_categorical
    joint:  caste_given_religion

  mother_tongue:
    method: conditional_categorical
    joint:  lang_given_religion

  migration:
    method: conditional_categorical
    joint:  migration_given_religion

  education:
    method: conditional_categorical
    joint:  education_given_caste

  marital_status:
    method:   plugin
    module:   derived.marital_sampling
    function: sample
    after:    [age_cohort, gender]

  workforce_status:
    method:   plugin
    module:   derived.workforce_sampling
    function: sample
    after:    [age_cohort, gender, education]

  occupation:
    method:   plugin
    module:   derived.occupation_sampling
    function: sample
    after:    [workforce_status]

  class_of_worker:
    method:   plugin
    module:   derived.occupation_sampling
    function: class_of_worker
    after:    [workforce_status]

  asset_media:
    method:   plugin
    module:   derived.asset_sampling
    function: sample
    after:    [gp_location, religion, occupation]

  amenities:
    method:   plugin
    module:   derived.amenity_sampling
    function: sample
    after:    [gp_location]

# Vote: simple religion-only conditional (no welfare blending in baseline).
# Per-AC overrides can layer in caste/gender/welfare blending.
vote:
  enabled: true
  field_name: "vote_2019_LS"
  parties: {parties}
  blending:
    method: "log_odds_mean"
    inputs:
      - {{table: "vote_given_religion", parent: "religion", weight: 1.5}}
      - {{table: "vote_given_caste",    parent: "caste",    weight: 1.0}}
      - {{table: "vote_given_gender",   parent: "gender",   weight: 0.5}}

verifier:
  tolerance:
    cell_z_max:            2.5
    composite_chisq_max:   800.0
  tier_weights:
    A: 4.0
    B: 3.0
    C: 2.0
    D: 1.5
    E: 1.0
"""


GENERATE_PY = """\
\"\"\"Generate a persona set for AC {ac} from a persona_config.

Usage:
    python kaisim/simulations/wb_2021_ac{ac}/generate.py baseline_rule
\"\"\"
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
    config_path = sim_dir / "persona_configs" / f"{{config_name}}.yaml"
    if not config_path.exists():
        print(f"ERROR: no persona config at {{config_path}}")
        sys.exit(2)

    ctx = SimulationContext.load(sim_dir)
    cfg = PersonaConfig.load(sim_dir, config_path)
    print(f"sim={{sim_dir.name}}  config={{config_name}}  set={{cfg.set_name}}")
    print(f"  axes={{len(ctx.axes)}}  joints={{len(ctx.joints)}}  "
          f"target_n={{cfg.target_n}}")

    SamplerCls = make_sampler(cfg.sampler)
    seed = cfg.raw.get("generation", {{}}).get("seed")
    sampler = SamplerCls(ctx, cfg, seed=seed)

    out = sim_dir / "personas" / cfg.set_name
    out.mkdir(parents=True, exist_ok=True)

    if hasattr(sampler, "dag"):
        print("\\nDAG order:")
        for name in sampler.dag.topo_order:
            print(f"  {{name}}")
    print()

    personas = sampler.sample_many(cfg.target_n)
    print(f"\\n  generated {{len(personas)}} personas")

    tol = cfg.get("verifier.tolerance") or None
    weights = cfg.get("verifier.tier_weights") or None
    report = verify_partial_population(ctx, personas, tolerance=tol,
                                          tier_weights=weights)
    h = report.headline()
    print(f"\\n{{h}}")

    pset = PersonaSet(name=cfg.set_name, personas=personas, config_snapshot=cfg.raw)
    pset.update_meta(sampler=cfg.sampler, verifier_summary=h)
    pset.save(out)
    (out / "reports").mkdir(exist_ok=True)
    (out / "reports" / "FINAL.md").write_text(render_partial_md(report))
    print(f"\\nwrote: {{out}}")


if __name__ == "__main__":
    main()
"""


def _read_party_set(ac: str) -> list[str]:
    """Read parties present in this AC's vote_given_religion CSV header."""
    import csv as _csv
    _matches = sorted((ROOT.parent / "constituency_data" / "constituencies").glob(f"{ac}_*"))
    p = _matches[0] / "2019" / "csv" / f"{ac}_vote_religion_2019.csv" if _matches else Path("__missing__")
    if not p.exists():
        return ["BJP", "AITC", "INC", "LF", "Other"]
    with p.open() as f:
        header = next(_csv.reader(f), [])
    keep = []
    skip = {"Religion", "Caste", "Gender", "Tier", "Source"}
    for c in header[1:]:
        if c and c not in skip:
            # Snake-case via the same pattern as the builder uses.
            code = re.sub(r"\([^)]*\)", "", c)
            code = re.sub(r"[^A-Za-z0-9]+", "_", code).strip("_")
            keep.append(code or "Unknown")
    return keep or ["BJP", "AITC", "INC", "LF", "Other"]


def write_plugin(path: Path, import_spec: str, doc: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    body = (
        f'"""{doc}"""\n'
        f"from pipeline.persona_generation.generic_plugins import {import_spec}\n"
    )
    path.write_text(body)
    return True


DERIVED_STUB = '''"""Derived-axis stub for `{name}` (AC {ac}).

Auto-generated by scripts/scaffold_ac_baseline_runtime.py. Returns the first
category of the axis as a placeholder. Replace with real logic when the AC's
narrative model needs this axis populated meaningfully (the partial verifier
ignores it for population validation either way — derived axes are not part
of the calibrated_2019 marginal/joint set).
"""
from __future__ import annotations


def {fn}(rng, ctx, axis, persona, persona_config=None, **kwargs):
    cats = axis.categories or []
    if not cats:
        return None
    return cats[0]
'''


def write_derived_stubs_for_ac(ac: str, sim_dir: Path, force: bool) -> list[str]:
    """Read the AC's axes.json; for any `kind=derived` axis whose module path
    points into this AC's derived/ AND no module file exists there, write a
    stub. Module-path resolution: 'simulations.wb_2021_ac<NN>.derived.<X>'
    → file at 'simulations/wb_2021_ac<NN>/derived/<X>.py'."""
    import json as _json
    axes_path = sim_dir / "structures" / "axes.json"
    if not axes_path.exists():
        return []
    axes = _json.loads(axes_path.read_text()).get("axes", [])
    written = []
    for a in axes:
        if a.get("kind") != "derived":
            continue
        module = a.get("module") or ""
        fn = a.get("function") or "compute"
        # Resolve to file path inside this sim's derived/
        prefix = f"simulations.wb_2021_ac{ac}."
        if not module.startswith(prefix):
            continue
        rel = module[len(prefix):]                  # e.g. "derived.rajbanshi_status"
        rel_path = sim_dir / Path(*rel.split(".")).with_suffix(".py")
        rel_path.parent.mkdir(parents=True, exist_ok=True)
        if rel_path.exists() and not force:
            continue
        rel_path.write_text(DERIVED_STUB.format(
            name=a["name"], ac=ac, fn=fn))
        written.append(str(rel_path.relative_to(sim_dir)))
    return written


def scaffold_one(ac: str, n: int = 500, force: bool = False) -> dict:
    sim_dir = SIMS_DIR / f"wb_2021_ac{ac}"
    if not sim_dir.exists():
        return {"ac": ac, "error": "sim dir missing"}
    derived = sim_dir / "derived"
    pc_dir = sim_dir / "persona_configs"
    derived.mkdir(exist_ok=True)
    pc_dir.mkdir(exist_ok=True)

    written = []

    init = derived / "__init__.py"
    if not init.exists():
        init.write_text("")
        written.append(init.name)

    for fname, (spec, doc) in PLUGIN_TEMPLATES.items():
        if write_plugin(derived / fname, spec, doc, force=force):
            written.append(f"derived/{fname}")

    cfg = pc_dir / "baseline_rule.yaml"
    if not cfg.exists() or force:
        parties = _read_party_set(ac)
        cfg.write_text(BASELINE_RULE_YAML.format(
            ac=ac, n=n, parties=parties))
        written.append(cfg.name)

    gen = sim_dir / "generate.py"
    if not gen.exists() or force:
        gen.write_text(GENERATE_PY.format(ac=ac))
        written.append(gen.name)

    # Stubs for any derived-axis modules declared by extensions.
    stubs = write_derived_stubs_for_ac(ac, sim_dir, force=force)
    written.extend(stubs)

    return {"ac": ac, "written": written}


def discover_acs() -> list[str]:
    out = []
    for d in sorted(SIMS_DIR.iterdir()):
        if d.is_dir() and d.name.startswith("wb_2021_ac"):
            out.append(d.name.replace("wb_2021_ac", ""))
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ac", nargs="?", default=None)
    p.add_argument("--all", action="store_true")
    p.add_argument("--n", type=int, default=500)
    p.add_argument("--force", action="store_true",
                    help="Overwrite existing derived/, configs, generate.py")
    p.add_argument("--include-095", action="store_true",
                    help="Also scaffold AC 095 (default: skipped, hand-curated)")
    args = p.parse_args()

    targets = (discover_acs() if args.all
               else [args.ac.zfill(3)] if args.ac else [])
    if not targets:
        p.error("provide AC number or --all")
        return 2

    if not args.include_095:
        targets = [t for t in targets if t not in PROTECTED_ACS]

    print(f"Scaffolding baseline runtime for {len(targets)} AC(s) "
           f"(force={args.force}): {targets}\n")
    for ac in targets:
        s = scaffold_one(ac, n=args.n, force=args.force)
        if "error" in s:
            print(f"  AC {ac}: ✗ {s['error']}")
            continue
        if s["written"]:
            print(f"  AC {ac}: wrote {len(s['written'])} files")
            for f in s["written"]:
                print(f"      {f}")
        else:
            print(f"  AC {ac}: ◌ all files already exist (use --force)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
