# Methodology — 2024-Calibrated WB Assembly Constituencies

This document accompanies the per-AC `<NNN>_<slug>_2024.md` files and their derived CSVs. It records what shifts when re-calibrating to end-2024 from the 2019/2021 baselines. Read [`methodology_2019.md`](methodology_2019.md) for the unchanged parts (tier taxonomy, schema rules, 16 marginal axes, 18 joint tables, validation gates).

## 1. Reading the calibrated file

The `_2024.md` artifact is **frozen at end-2024-state-of-knowledge** — written as if the year were end-2024 (after the June 2024 LS results were known) and we did not yet know:

- 2025 SIR (Special Intensive Revision) voter-roll deletions
- 2025-26 pre-poll surveys, defection chains, candidate lists
- 2026 WB Assembly Election polling and results

**Forbidden keywords (auto-checked by gate 5):** `2025, 2026, SIR, Special Intensive Revision, AE-2026, 2026 election`

The file MAY freely reference: 2019 LS, all of 2020-2024 events (COVID, Amphan, 2021 AE, Lakshmir Bhandar, SSC scam, Partha Chatterjee arrest, BSF 50km, Bangladesh attacks, CAA notification Mar 2024, 2024 LS campaign and result, RG Kar protests Aug 2024, Bangladesh interim regime Aug 2024+).

## 2. What changes from the 2019/2021 files

| Section | Shift |
|---|---|
| Title preamble | "Calibrated 2024" |
| § B (population) | 13-year projection from Census 2011 |
| § C marginals | Same 16 axes; updated for 13 yrs of trend |
| § C.14 asset/media | Smartphone effectively saturated (~85-90%); banking PMJDY+ peak penetration; UPI/digital payments universal |
| § C.16 migration | Bangladesh interim regime trade disruption (Aug 2024+) for border ACs; sustained out-migration to Kerala/Tamil Nadu |
| § D joint tables | Same 18; vote × demographics now anchor on 2024 LS AC-segment result |
| § E calibration target | **2024 LS AC-segment result for the AC** — direct from `data/2024_AssemblySegmentLevelVotingData.csv` (tier A) |
| § F vote history | Includes 2019 LS, 2021 AE, 2024 LS as anchors (in chronological order) |
| § H validation anchors | Forward-looking only — 2026 AE polling/forecasts (out-of-sample) — leave thin or blank in v0 |

## 3. Calibration target

For each AC, the **2024 LS AC-segment result** is the new ECI-tier-A calibration target. Direct extraction:

```python
import csv
with open('data/2024_AssemblySegmentLevelVotingData.csv') as f:
    next(f)  # skip header preamble row
    rows = list(csv.DictReader(f))
ac = [r for r in rows if 'West Bengal' in r['State/UT Name'] and r['AC NO'].strip() == '<NNN_INT>']
```

Columns: `AC NO`, `AC NAME`, `TOTAL ELECTORS IN AC`, `NOTA VOTES EVM IN AC`, `CANDIDATE NAME`, `PARTY`, `VOTES SECURED EVM`. Aggregate by `PARTY`, divide by total valid votes for vote shares.

## 4. New events to incorporate (post-2021, pre-end-2024)

- **2022 Jul**: Partha Chatterjee SSC scam arrest; ED money seizure at Arpita Mukherjee
- **2023 Apr-Jun**: Sandeshkhali ED raid build-up (Sheikh Shahjahan absconding)
- **2023 Jul**: WB Panchayat election (TMC dominance, BJP/CPI(M) split rural opposition)
- **2024 Feb 8**: Sandeshkhali women's protests; widespread coverage
- **2024 Feb 29**: Sheikh Shahjahan arrested
- **2024 Mar 11**: CAA rules notified (3 years after Act); Matua belt jubilation tempered by paperwork
- **2024 Apr-May**: 2024 LS campaign — Modi rallies, Mamata rallies
- **2024 Jun 4**: 2024 LS results — TMC 29 / BJP 12 / INC 1 in WB
- **2024 Jun**: CAA citizenship grants begin tokenistic (~14 certificates from ~1.12L apps by polling)
- **2024 Aug**: RG Kar Hospital rape-murder; mass medical-fraternity protests; CBI investigation
- **2024 Aug 5**: Bangladesh student protests / Hasina ouster; Yunus interim government
- **2024 Aug+**: Petrapole/Hili India-Bangladesh trade depressed; AC-level livelihood hit for border seats

## 5. Source list (additions)

- `data/2024_AssemblySegmentLevelVotingData.csv` (ECI 2024 LS AC-segment, tier A)
- Wikipedia 2024 WB LS election article (per LS PC)
- WB Lakshmir Bhandar penetration figures (where available)
- The Hindu, Indian Express, ThePrint coverage of CAA notification and grants delivery
- Bangladesh trade volume data (Petrapole) where AC is on border

## 6. Validation gates

Same 5 gates. Forbidden-keyword gate uses §1 list above. Run:

```bash
python3 kaisim/scripts/derive_calibrated_2024_csvs.py NNN
python3 kaisim/scripts/derive_calibrated_2024_csvs.py --all
```

## 7. Section H — special handling

Since 2024 is now the most recent calibrated year, § H ("Post-{YEAR} validation anchors") becomes thin. Acceptable contents:
- 2026 pre-poll surveys (if any are publicly summarized) — tier D
- "TBD: 2026 AE results" placeholder
- Or: leave the section header with a single note "No post-2024 validation anchors fetched in v0"
