# Methodology — 2019-Calibrated Bangaon Uttar (AC 95)

This document accompanies [`095_bangaon_uttar_2019.md`](095_bangaon_uttar_2019.md) and the CSVs in [`csv/`](csv/). It records the projection assumptions, calibration choices, source list, and known gaps in v0.

## 1. Reading the calibrated file

The `_2019.md` artifact is **frozen at 2019-state-of-knowledge** — written as if the year were end-2019 and we did not yet know:

- The 2019 NRC controversy escalation, 2020 protests, COVID-19 (2020+)
- 2021 WB Assembly Election results
- Lakshmir Bhandar (launched 2021)
- CAA rules notification (March 2024)
- Thakurbari Shantanu vs Mamatabala split crystallization (2020+)
- SSC scam exposure (2022+)
- RG Kar protest (2024)
- SIR voter-roll revision (2025)
- Subsequent General Election results (post-2019)

The downstream simulator can use post-2019 events as out-of-sample validation gates without information leakage from this file.

## 2. Confidence tiers

Same A–E taxonomy as the main dataset. Recap:

- **A** — direct AC/block-level hard data
- **B** — state govt or central MIS dashboard, sub-AC granularity, aggregated to AC
- **C** — academic study or CSDS regional subsample
- **D** — journalistic estimate
- **E** — modeled imputation

## 3. Composition of AC 95 (Delimitation 2008)

AC 95 = Bangaon Municipality (full) + 7 of the ~16 Gram Panchayats of CDB Bangaon (rural):

- Akaipur, Chhaigheria, Dharma Pukuria, Ganganandapur, Ghatbore, Gopalnagar-I, Gopalnagar-II

The remaining GPs of CDB Bangaon (Bagda-side, Gaighata-side) fall under AC 94 Bagda, AC 96 Bangaon Dakshin, and AC 97 Gaighata.

For v0, GP-level data isn't accessible (DCHB N24P Part-A connection-blocked from this environment). We treat the AC as **two sub-units** for spatial heterogeneity:

- **U1: Bangaon Municipality** — urban, ~108,864 pop in 2011
- **U2: Bangaon-CDB-rural-AC-share** — 7 of ~16 GPs of CDB Bangaon, estimated 7/16 × 207,835 ≈ 90,928 pop in 2011

Total AC 95 base 2011 population estimate: **~199,792**. Proportionally adjusted +8.5% to 2019 ≈ **~216,725 population**.

## 4. Projection from Census 2011 → 2019

Eight-year compound projection. Documented assumptions (the simulator can override):

| Variable | Assumption | Source |
|---|---|---|
| Hindu population growth | +1.0%/yr → +8.29% over 8 years | Pew India 2021 projections; 2001-2011 Census growth rate |
| Muslim population growth | +1.3%/yr → +10.92% over 8 years | Same |
| Christian / other growth | +0.5%/yr → +4.07% over 8 years | Same |
| Net out-migration (working-age males) | -0.5%/yr from working-age cohort | PMC-Springer WB→Kerala study (2020) |
| Voter cohort additions | +5%/yr of 18-yr cohort enters electorate annually | Census 2011 C-13 age pyramid |
| Asset/media diffusion (TV) | +3-5%/yr in WB rural; saturating ~85% by 2019 | NFHS-4 (2015-16) → NFHS-5 (2019-21) |
| Smartphone diffusion | +10-15%/yr in WB rural; ~50% by 2019 | NFHS-4/5 |
| Literacy growth | +0.5pp/yr in rural; saturating | Census 2001-2011 trend |

**Net effect on religion shares 2011 → 2019:** Muslim share rises ~0.3-0.5pp, Hindu falls correspondingly. The shift is small over 8 years and well within the model's noise bounds.

## 5. Calibration target

The simulator's job is to reproduce the **2019 Lok Sabha Bangaon (LS PC 14) result** at the AC-95 segment level:

- 2019 LS Bangaon result (whole LS, A): **Shantanu Thakur (BJP) 48.85% / Mamata Thakur (AITC) 40.92% / margin 111,594** ([ECI/Wikipedia](https://en.wikipedia.org/wiki/Bangaon_Lok_Sabha_constituency))
- AC-95 segment within Bangaon LS (D): not published per polling-station; v0 uses the whole-LS proportional decomposition. Form-20 GE2019 should refine this when fetched.

Pre-2019 anchors for cross-validation (these are NOT calibration targets — they're historical context the simulator can use to initialize beliefs):

| Year | Election | AC 95 result | Source tier |
|---|---|---|---|
| 2011 AE | AC 95 | Biswajit Das (AITC) 54.55% / Dr. Biswajit Biswas (CPI(M)) 40.12% — margin 23,620 | A |
| 2014 LS | Bangaon | Kapil Krishna Thakur (AITC) 36.81% / Subrata Thakur (BJP) 19.65% / Indrani Halder (CPI(M)) 18.81% — TMC won | A |
| 2014 LS by-election | Bangaon | Mamatabala Thakur (AITC) won (Kapil Krishna Thakur's death) | A |
| 2016 AE | AC 95 | Biswajit Das (AITC) 50.59% / Sushanta Baowali (AIFB) 33.07% — margin 33,192 | A |
| 2019 LS | Bangaon | Shantanu Thakur (BJP) 48.85% / Mamata Thakur (AITC) 40.92% — margin 111,594 | A |

## 6. Source list

| # | Source | Used for | Status |
|---|---|---|---|
| 1 | Census 2011 — Bangaon CD Block (Wikipedia rollup of A) | Religion, SC%, ST%, literacy, mother tongue, occupation | ✓ have |
| 2 | Census 2011 — Bangaon sub-division | Religion at sub-division, augments municipality estimate | ✓ have |
| 3 | Census 2011 — N24P district | Cross-checks for joint tables | ✓ have |
| 4 | Pew India 2021 — religious growth projection | 2011→2019 religion projection | ✓ public estimates |
| 5 | NFHS-4 (2015-16) WB | Asset/media + amenity baseline mid-decade | partial — published summary |
| 6 | ECI archives 2019 LS Bangaon | Calibration target (whole-LS) | ✓ have via Wikipedia |
| 7 | ECI archives 2011/2014/2016 — AC 95 / Bangaon LS | Pre-2019 anchors | ✓ have via Wikipedia |
| 8 | DCHB N24P Part-A (Census 2011 GP-level) | GP-level demographics for 7 Bangaon GPs | ✗ deferred — host blocked from current environment |
| 9 | Census HH-13 (asset / media ownership) | Media-access columns at block/GP level | ✗ deferred — accessible PDF not located in v0 |
| 10 | Census D-series migration | Birthplace / refugee / internal migrant | ✗ deferred — accessible PDF not located in v0 |
| 11 | ECI 2019 final electoral roll AC 95 | Population baseline cross-check | ✗ deferred — not on CEO WB current site |
| 12 | ECI 2019 LS Form-20 Bangaon | AC-95 segment vote share refinement | ✗ deferred — not on CEO WB current site |
| 13 | CSDS-Lokniti 2019 NES post-poll | Vote × demographic conditionals | ✓ partial — national rollup; WB regional ~from secondary sources |
| 14 | Swarajya / CSDS press summaries (2019) | WB regional voting breakdowns | ✓ have via DemographicParameters.md citations |

## 7. v0 known gaps (to be closed in v1)

1. **GP-level demographics** — collapsed to 2 sub-units (Municipality + Rural-CDB-share). When DCHB Part-A becomes accessible, refine to 8 sub-units.
2. **Form-20 GE2019 segment vote** — using whole-LS proportional decomposition. Refine with Form-20 when accessible.
3. **HH-13 asset / media** — using NFHS-4 WB rural/urban averages as proxy (tier C). Refine with Census HH-13 block-level when accessible.
4. **D-series migration** — using qualitative narrative anchors only ("Matua refugee population is dominant in CDB-rural-share"). Refine with Census D-01 when accessible.
5. **CSDS WB regional cross-tabs** — using state-summary numbers from Swarajya/CSDS 2019 press summaries (tier C/D). Could refine with full Lokniti WB report if obtainable.

## 8. Validation gates (run via `scripts/validate_calibrated_2019.py 095`)

1. **Marginal sum** — every marginal in §C of MD sums to 100 ± 0.5
2. **Joint marginal recovery** — joint tables, summing along one axis, recover the corresponding marginal within ±0.5
3. **Population calibration** — projected adult population × eligibility-rate ≈ ECI 2019 final roll for AC 95 within ±2% (note: ECI roll not available, so this gate currently checks against the projection-derived estimate)
4. **Vote calibration** — Σ(joint Vote × demographic) recovers the 2019 LS Bangaon AC-95 segment within ±1pp on each major party (currently using whole-LS as the segment estimate; replace with Form-20 when available)
5. **No-future-leakage** — automated grep over MD + CSVs for any reference to: `2020|2021|2022|2023|2024|2025|2026|CAA rules|SIR|Thakurbari|RG Kar|SSC scam|Lakshmir Bhandar|Cyclone Amphan|COVID-19|coronavirus`

## 9. Reproducing v0

```bash
# (No fetch step — v0 uses already-collected data)
python3 scripts/derive_calibrated_2019_csvs.py    # parses MD tables → csv/*.csv
python3 scripts/validate_calibrated_2019.py 095   # runs the 5 gates
```
