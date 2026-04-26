---
name: run-calibration
description: Run pre-election calibration — generate a rule-based reference persona set, audit its distributions against target marginals + joints + aggregate vote, and report the verifier composite chi-square. Use when the user wants to "calibrate", "verify the persona set matches targets", "validate the structures", or "run baseline before LLM generation".
---

# Kaisim — Pre-Election Calibration

You are running the rule-based calibration step. This validates that the
demographic structures (`axes.json` + `joints.json`) are internally consistent
and produce a population matching the target distributions.

## When to run

Always before any expensive LLM persona-generation. Catches:
  - Wrong canonical codes (sampler returns "None" because lookup fails)
  - Inconsistent target marginals (e.g., workforce_status target doesn't
    match PLFS data)
  - Vote calibration target inconsistent with religion×caste×welfare blend

## Steps

```bash
SIM=<sim_name>
PCFG=baseline_rule    # or another rule-based config

# 1. Rebuild structures (parses CSVs)
python kaisim/simulations/$SIM/build_structures.py

# 2. Generate persona set with the rule-based sampler
python kaisim/simulations/$SIM/generate.py $PCFG
```

## What "good" looks like

After the run, look at `personas/<set_name>/reports/FINAL.md`:

  - **composite chi-square**: should be **< 800** for n=1000
    (n=100 would be ~150-300)
  - **max axis |z|**: ideally **< 3** for all axes; up to 5 acceptable for
    tier-E targets that are themselves imputed
  - **aggregate vote max |z|**: ideally **< 2** — if BJP/AITC are off by
    >5pp, suspect either the religion mix or the +AITC adjustment in
    aggregate target

## What to fix when calibration fails

Check `reports/FINAL.md` "## Axes" section, sorted by max_abs_z descending:

| Symptom | Likely cause | Fix |
|---|---|---|
| `workforce_status` Non_worker over by >10pp | Heuristic plugin inflates housewife share | Lower female housewife rule rate in `derived/workforce_sampling.py` |
| `religion` off by >5pp | "+1.0%/yr Hindu projection" assumption | Override in `build_structures.py` MARGINAL_OVERRIDES with Census 2011 anchor |
| `welfare_dominant.None` near-zero | Plugin overstates welfare reach | Check `derived/welfare_exposure.py` — base rates probably too high |
| Aggregate vote BJP undershoots | +AITC adjustment in target unsourced | Override in AGGREGATE_OVERRIDES |
| Joint cell |z| > 5 on small-n cells (Other religion, OBC) | Sampling noise — expected | Accept; verifier should auto-discount via z-score |

## Iteration loop

```
1. python build_structures.py
2. python generate.py baseline_rule
3. cat personas/baseline_rule_n1000/reports/FINAL.md   # inspect
4. Apply fix to build_structures.py OR derived/ plugin
5. Goto 1
```

Each iteration is ~10s (rule-based sampling is fast). Tighten until
composite chi-sq < 800 OR until you've documented the gaps as Tier-D/E
acceptable.

## Plot the verifier output

```bash
python kaisim/simulations/$SIM/plot.py baseline_rule_n1000
```

Generates `personas/baseline_rule_n1000/reports/plots/`:
  - `gap_summary.png` — fix-priority view
  - `marginals_partitions.png` — per-axis target vs observed
  - `marginals_flags.png` — flag-axis target vs observed
  - `aggregate_vote.png` — vote share vs ground truth

## Reference

  - Verifier internals: `kaisim/pipeline/verifiers/composite.py` (Pearson chi-square)
  - Tolerance defaults + literature: `kaisim/pipeline/docs/TOLERANCES.md`
  - WB worked example: `kaisim/simulations/wb_2021_ac095/STRUCTURE.md`
