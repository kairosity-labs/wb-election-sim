# Bangaon Uttar (AC 095) — WB 2021 simulation

Pilot Kaisim simulation: simulate the 2021 West Bengal Assembly Election
result for AC 95 (Bangaon Uttar) by generating ~100–1000 voter personas
calibrated to 2019 demographics, then querying them.

**Status:** Phase 1.1 complete (rule-based persona generation + verifier).
Phase 1.2 (LLM-generated personas with narrative) and Phase 2 (downstream
simulation) pending.

---

## Quick start

```bash
# Build axes.json + joints.json from the calibrated 2019 CSVs.
# Re-run only when the underlying CSVs change.
python kaisim/simulations/wb_2021_ac095/build_structures.py

# Generate the rule-based reference persona set (n=1000, no LLM).
python kaisim/simulations/wb_2021_ac095/generate.py baseline_rule

# Inspect the verifier report.
cat kaisim/simulations/wb_2021_ac095/personas/baseline_rule_n1000/reports/FINAL.md
```

---

## What this simulation does

  - **Calibrates against** the 2019 LS Bangaon AC-95 segment vote share
    (`095_calibration_target_2019.csv`): BJP 48 / AITC 44 / Left+INC 6 /
    Other 2.
  - **Generates** ~1000 personas via the framework's rule-based sampler,
    each with 17 demographic fields + vote_2019_LS prior.
  - **Verifies** the population against 17 marginals + 18 joint tables +
    the aggregate vote target.
  - **(Phase 1.2)** Replaces rule-based with LLM-batched persona generation
    that adds a `narrative` field per persona.
  - **(Phase 2)** Feeds news headlines from 2019 → 2021 to each persona one
    at a time and re-asks vote intent for the 2021 AE.

---

## Files of interest

  - [`STRUCTURE.md`](STRUCTURE.md) — design choices: 4 overlap resolutions,
    welfare derivation rules, vote blending defaults, verifier tolerance.
  - [`build_structures.py`](build_structures.py) — translates CSVs into
    framework-consumable `structures/{axes,joints}.json`.
  - [`derived/`](derived/) — region-specific Python plugins for axes that
    can't be sampled from a simple marginal/joint (welfare exposure,
    workforce rules, marital residual fill, asset blending, amenity
    cooking-fuel partition, occupation guarding).
  - [`persona_configs/baseline_rule.yaml`](persona_configs/baseline_rule.yaml)
    — sampling spec + vote blending + verifier tolerance for the rule-based
    reference run.
  - [`personas/baseline_rule_n1000/`](personas/baseline_rule_n1000/) —
    generated artifact (1000 personas + verifier report).

---

## Sources

The CSVs under `kaisim/data/calibrated_2019/csv/` were derived from
[`095_bangaon_uttar_2019.md`](../../data/calibrated_2019/095_bangaon_uttar_2019.md).
That document is the canonical 2019-frozen description of AC 95: caste
composition, religion, education, vote history, narrative anchors. It is
the source for prompts in Phase 1.2 (and never directly read by the
framework).
