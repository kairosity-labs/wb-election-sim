# Lessons from AC 198 (Tarakeswar)

## New pattern: GP-conditional caste sampling via plugin

**Symptom:** `caste_given_gp` joint has high chisq (300+) and max cell |z|>10
even after the joint table is properly mapped to caste-axis leaves. The
default DAG samples religion → caste (via `caste_given_religion`), so the
actual GP×caste cross-tab in the population doesn't reproduce the
`caste_given_gp` table — it reproduces the religion-conditional one.

**Cause:** Two joints (`caste_given_religion` and `caste_given_gp`) both
specify caste distributions, but if the sampler uses one, the verifier
sees the other's cells violated. The conditionals are mutually consistent
only if the underlying joint distribution is fully specified — which it
isn't, since each is a 1D conditional.

**Fix:** Write a per-AC `derived/caste_sampling.py` plugin that samples
caste conditional on BOTH `gp_location` and `religion`:
  - Muslim → "Muslim" caste
  - Sarna_Tribal_religion / Christian / Other → "Christian_Sarna_only_Other"
  - Hindu → use `caste_given_gp` row, restricted to Hindu sub-castes

```python
HINDU_CASTES = ("UC_bhadralok", "OBC_Hindu", "Other_Hindu",
                "SC_total", "ST_total")

def sample(rng, ctx, axis, persona, persona_config=None, **kwargs):
    religion = persona.get("religion")
    gp = persona.get("gp_location")
    if religion == "Muslim":
        return _pick_category(axis, ("Muslim",))
    if religion in ("Sarna_Tribal_religion", "Christian", "Other"):
        return _pick_category(axis, ("Christian_Sarna_only_Other",))
    joint = _try_joint(ctx, "caste_given_gp")
    if joint is not None:
        row = joint.table.get(gp, {})
        cats = [c for c in HINDU_CASTES if c in row and row[c] > 0]
        weights = [row[c] for c in cats]
        if sum(weights) > 0:
            return rng.choices(cats, weights=weights, k=1)[0]
    return _pick_category(axis, ("OBC_Hindu",))
```

Wire it in `persona_configs/baseline_rule.yaml`:
```yaml
caste:
  method:   plugin
  module:   derived.caste_sampling
  function: sample
  after:    [gp_location, religion]
```

This drove `caste_given_gp` chisq from 300+ to ~18.

**Suggested skill section:** NEW (or extension to §A: when joints with
overlapping child axes need caste distribution to honor multiple parents).

---

## New pattern: Workforce residual weights tuned for target marginal

**Symptom:** After dropping child cohorts, fixing female-housewife rate,
and adding student/senior gates, Non_worker still observed 5–10pp above
target. The marginal residual sample (from generic plugin) over-samples
Non_worker because the axis marginal includes the 37% Non_worker share
which is meant to be hit *across* gates plus residual, not within residual
alone.

**Cause:** Generic plugin's residual `_sample_from_marginal_excluding`
samples from {Main_worker, Marginal_worker, Non_worker, Unemployed} with
axis-marginal weights. After gates capture ~half the Non_worker target,
the residual still samples Non_worker at marginal weight, double-counting
the Non_worker mass.

**Fix:** Replace residual with explicit weight map tuned to balance after
gate effects:
```python
weights_map = {"Main_worker": 55, "Marginal_worker": 20,
                "Unemployed": 12, "Non_worker": 13}
```
Numbers depend on AC; iterate until workforce_status |z| < 2.

**Suggested skill section:** Extension to §B (workforce/non-worker tuning).

---

## New pattern: Mahishya is GENERAL caste, not OBC

**Symptom:** When the auto-builder produces `caste_given_gp` rows with a
combined "Mahishya_Sadgop" code in OBC-dominant Hooghly/Howrah ACs
(AC 198, similar in others), naive routing of all Mahishya_Sadgop mass to
OBC_Hindu produces OBC observed = 40+% but axis target only 30%, while
Other_Hindu observed ≈ 3% vs target 16%.

**Cause:** Mahishya is a General/UC caste in the WB Mandal classification
(despite being numerically a "Sudra" caste historically). Sadgop IS OBC.
The CSV combined them but the verifier needs them split.

**Fix:** In curate.py, split Mahishya_Sadgop ~70:30 (Mahishya general /
Sadgop OBC) when mapping to caste leaves:
```python
obc_total = ms * 0.30 + kto * 0.50
ohm = ms * 0.70 + kto * 0.50  # ohm = Other_Hindu mass
```
The 70:30 ratio is approximate and AC-specific (tune by checking observed
OBC_Hindu / Other_Hindu against target ratio).

**Suggested skill section:** Extension to §A on caste rollups; could
generalize as a WB-Mandal sub-caste classification reference table for
common sub-codes.
