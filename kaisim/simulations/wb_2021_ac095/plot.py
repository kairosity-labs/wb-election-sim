"""Plot distributions for a generated persona set vs targets.

Usage:
    python kaisim/simulations/wb_2021_ac095/plot.py <persona_set_name>
"""
from __future__ import annotations

import sys
from pathlib import Path

KAISIM = Path(__file__).resolve().parents[2]
if str(KAISIM) not in sys.path:
    sys.path.insert(0, str(KAISIM))

from pipeline.core.config import SimulationContext
from pipeline.core.persona_set import PersonaSet
from pipeline.verifiers.plots import save_all_plots


def main():
    if len(sys.argv) < 2:
        print("usage: plot.py <persona_set_name>")
        sys.exit(2)
    set_name = sys.argv[1]
    sim_dir = Path(__file__).parent
    ctx = SimulationContext.load(sim_dir)
    pset = PersonaSet.load(sim_dir / "personas" / set_name)
    out_dir = (sim_dir / "personas" / set_name / "reports" / "plots")
    paths = save_all_plots(ctx, pset.personas, out_dir)
    print(f"Wrote {len(paths)} plots:")
    for p in paths:
        print(f"  {p}")


if __name__ == "__main__":
    main()
