# West Bengal Electoral Politics — Constituency-Level Demographic Dataset

A structural-causal-model ready dataset for the 2026 WB Legislative Assembly election (Phase 1 polled 23 April 2026; Phase 2 polls 29 April; counting 4 May).

**Scope:** 294 Assembly Constituencies (210 GEN + 68 SC + 16 ST) across 23 districts.
**Consumers:** SCM simulation of voter behaviour — the India analog of Aaru/Simile.

---

## Artifacts

| File | Purpose |
|---|---|
| [DemographicParameters.md](DemographicParameters.md) | State-level SCM reference with top-15 nodes ranked by elasticity |
| [data/constituencies.csv](data/constituencies.csv) | Machine-readable master — 294 rows × 125 columns, each data cell with a `*_conf` tier tag (A–E) |
| [data/methodology.md](data/methodology.md) | Tier definitions, schema, imputation logic, verification gates |
| [data/sources.md](data/sources.md) | Source catalog with probe-status + ingest-status |
| [data/raw/](data/raw/) | Canonical scraper/parser outputs |
| [scripts/](scripts/) | Python ingestion pipeline (pdfplumber, requests, bs4) |
| [constituencies/](constituencies/) | One MD profile per AC — 10 fully populated, 284 stubs |

---

## Current tier coverage

After Step-2 ingestion + Step-3 pilot profiles:

| Column family | 294 ACs populated | Tier mix |
|---|---|---|
| Electorate (total / M / F) | 294 / 294 | **A** (CEO WB SIR 2026 AC-wise PDF) |
| Religion (Hindu/Muslim/Christian/Other) | 294 / 294 | **E** (Wikipedia Census 2011 district rollup) + 10 pilots refined via CDB |
| SC/ST totals | 274 / 294 | **E** (district rollup; 20 Kolkata ACs blank pending Census Kolkata-urban rollup) |
| SC/ST sub-groups (Namasudra/Rajbanshi/Santhal/Oraon etc.) | 10 pilots only | E (CDB-research-based where applicable) |
| Language (Bengali/Hindi/Urdu/Santhali/Nepali) | 200+ / 294 | E (district rollup, partial) + 10 pilots refined |
| Literacy (overall / M / F) | 294 / 294 | **E** (district rollup) + 10 pilots refined |
| BPL% / MGNREGA worker share | Blank | Pending: SECC dashboard down, MGNREGA 401-auth, Swasthya Sathi 403. Fallback: Census 2001 CDB baselines for pilots only |
| Welfare scheme beneficiaries | 10 pilots only | E (district pop-scaling) |
| AC ↔ CDB mapping | 294 ACs, 625 components | **A** (Delimitation Commission 2008 order, pages 517-539) |

---

## Pilot profiles (10/294 fully written)

Chosen across every major SCM axis; each profile exercises a different causal node from DemographicParameters.md §SUMMARY top-15.

| # | AC | District | Axis tested |
|---|---|---|---|
| 1 | [095 Bangaon Uttar (SC)](constituencies/095_bangaon_uttar.md) | North 24 Parganas | **Matua × SIR × CAA** — Thakurbari seat, ~40% Namasudra/Matua |
| 2 | [210 Nandigram (GEN)](constituencies/210_nandigram.md) | Purba Medinipur | **Mahishya-Muslim coalition + 2007 land movement + Mamata-Suvendu 2021** |
| 3 | [159 Bhabanipur (GEN)](constituencies/159_bhabanipur.md) | Kolkata | **Urban bhadralok + Hindi-speaker + Muslim "mini-India" — Mamata's own seat** |
| 4 | [007 Dinhata (GEN)](constituencies/007_dinhata.md) | Cooch Behar | **Rajbanshi identity + Kamtapur autonomy + 57-vote 2021 → 164k by-poll swing** |
| 5 | [069 Bharatpur (GEN)](constituencies/069_bharatpur.md) | Murshidabad | **Muslim-majority border + SIR deletions + Humayun Kabir AJUP spoiler** |
| 6 | [023 Darjeeling (GEN)](constituencies/023_darjeeling.md) | Darjeeling | **Nepali Gorkha + hill factional politics (BGPM/GNLF/Hamro) + GTA** |
| 7 | [237 Binpur (ST)](constituencies/237_binpur.md) | Jhargram | **Santhal + Sarna Dharma + Kurmi-Santhal ST-reservation tension** |
| 8 | [216 Kanthi Dakshin (GEN)](constituencies/216_kanthi_dakshin.md) | Purba Medinipur | **Mahishya OBC + Adhikari family stronghold** |
| 9 | [281 Asansol Uttar (GEN)](constituencies/281_asansol_uttar.md) | Paschim Bardhaman | **Industrial Hindi-speaker + Bengali bhadralok + urban BJP-competitive** |
| 10 | [014 Madarihat (ST)](constituencies/014_madarihat.md) | Alipurduar | **Dooars tea-garden + Oraon/Munda + ₹300/day wage politics** |

The remaining 284 ACs carry their tier-A electorate + tier-E district-rollup values but have stub profiles; Step 4 (scale to 294) is the automated breadth pass.

---

## Sources successfully ingested

| Source | Tier | Coverage | Script |
|---|---|---|---|
| CEO WB AC-wise Draft Elector SIR 2026 PDF | **A** | 294 ACs × electorate (total/M/F/TG/PS) | `scripts/parse_ceo_wb_sir_pdf.py` |
| Delimitation Commission of India 2008, Schedule XXX (pp 517-539) | **A** | 294 ACs × CDB/Municipality/Notified-Area components (625 rows) | `scripts/parse_delimitation_wb.py` |
| Wikipedia district pages (Census 2011 demographics) | **E** (district rollup) | 23 districts × religion / SC-ST / literacy / language | `scripts/aggregate_census_district_to_ac.py` |
| Form 20 Part II 2024 LS (18 MB PDF) | Downloaded only | AC-segment LS vote shares | Parser deferred |

## Sources blocked / deferred

| Source | Blocker | Fallback |
|---|---|---|
| SECC 2011 (`secc.gov.in`) | DNS dead | Census 2001 CDB BPL baselines (tier C), where available |
| MGNREGA MIS (`nrega.dord.gov.in`) state drilldown | HTTP 401 auth | Data.gov.in district CSV (deferred) |
| Swasthya Sathi (`swasthyasathi.gov.in`) | HTTP 403 | State-level ≥95% coverage narrative (tier C) |
| `voters.eci.gov.in` (AC-level electoral roll) | React SPA, captcha | CEO WB SIR PDF covers key needs |
| Census 2011 village/town PCA on data.gov.in | Janparichay auth required | District Wikipedia rollup (tier E) |

---

## Reproducing the pipeline

```bash
python3 scripts/bootstrap.py                     # 294 CSV skeleton + stub MDs
python3 scripts/parse_ceo_wb_sir_pdf.py          # tier-A electorate
python3 scripts/parse_delimitation_wb.py         # AC↔CDB mapping
python3 scripts/aggregate_census_district_to_ac.py  # tier-E district rollup
python3 scripts/build_constituencies_csv.py      # merge all raw/ → master CSV
python3 scripts/_fill_ac.py                      # apply 10 pilot overrides
python3 scripts/validate_csv.py                  # internal-consistency check
```

All scripts are idempotent; pilot MD profiles are manually authored and not overwritten by `bootstrap.py`.

---

## Known limitations (what the SCM should distrust)

Full catalog in [data/methodology.md §6](data/methodology.md). Headline items:

1. **Caste sub-group shares are tier C-E for all 294 ACs.** No post-1931 caste census for non-SC/ST. Mahishya, Sadgop, Kurmi, Namasudra/Matua sub-shares are journalistic/academic estimates.
2. **Religion/language/literacy at AC level is tier E (district rollup)** for 284 of 294 ACs. Within-district variation collapses. Pilot ACs have tier-E CDB rollups — more specific but still imputation.
3. **Welfare-scheme beneficiary counts at AC level are tier E (district pop-scaling)** for all 294. No public AC-level dashboard for Lakshmir Bhandar / Krishak Bandhu / Kanyashree.
4. **SIR deletion counts at AC level** are tier D/E; only district totals (Murshidabad 7.48L, Nadia 4.85L, Malda 4.59L, UD 3.63L, Cooch Behar 2.42L) are ECI-published.
5. **2024 LS AC-segment vote shares** are tier D until ECI Form-20 is parsed (downloaded; parser pending).

---

## Next steps

- **Step 4 — Scale to 294** via `build_constituencies_csv.py` plus targeted per-district research sweeps (one per district, not per AC). Budget: 23 district sweeps.
- **Deferred parsers** in priority order:
  1. Delimitation order → block-to-AC aggregation formula enabled for future tier-A Census village data
  2. Form 20 Part II → 2024 LS AC-segment vote shares (tier A)
  3. Data.gov.in Census 2011 village PCA (requires Janparichay auth)
  4. Playwright retry for Swasthya Sathi + MGNREGA MIS (only if SCM sensitivity requires)
- **Validation sweeps** on per-AC profiles: district roll-up checks (±5% tier A / ±10% tier B / ±15% tier C+), Trivedi Centre cross-reference on literacy/SC% for pilots.
