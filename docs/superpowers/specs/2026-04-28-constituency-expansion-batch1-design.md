# Design — Constituency Expansion Batch 1 (20 ACs)

**Date:** 2026-04-28  
**Scope:** Expand `constituency_data/constituencies/` from 10 to 30 ACs by running 20 parallel agents, one per new constituency, each producing a fully calibrated 2019 MD + derived CSVs.

---

## Context

- 294 West Bengal Assembly Constituencies for the 2026 election
- 10 already populated: ACs 3, 11, 64, 95, 123, 143, 159, 198, 210, 222
- This batch adds the first 20 new ACs (sequential from AC 1, skipping existing ones)
- Approach: **Option A — full depth**, same quality as the existing 10 (web research, sourced tiers, sub-AC Census decomposition where available)

---

## Target constituencies — Batch 1

| AC | Name |
|---|---|
| 001 | Mekliganj |
| 002 | Mathabhanga |
| 004 | Cooch Behar Dakshin |
| 005 | Sitalkuchi |
| 006 | Sitai |
| 007 | Dinhata |
| 008 | Natabari |
| 009 | Tufanganj |
| 010 | Kumargram |
| 012 | Alipurduars |
| 013 | Falakata |
| 014 | Madarihat |
| 015 | Dhupguri |
| 016 | Maynaguri |
| 017 | Jalpaiguri |
| 018 | Rajganj |
| 019 | Dabgram-Fulbari |
| 020 | Mal |
| 021 | Nagrakata |
| 022 | Kalimpong |

---

## Directory structure per new AC

```
constituency_data/constituencies/NNN_slug/
├── 2019/
│   ├── NNN_slug_2019.md        ← primary artifact (agent-produced)
│   ├── raw/                    ← source scrapes / PDFs (agent may populate)
│   ├── csv/                    ← derived CSVs (agent runs derivation script)
│   └── audit/                  ← gate report (future step, not this batch)
├── 2021/                       ← scaffold only, empty
├── 2024/                       ← scaffold only, empty
└── events.yaml                 ← stub with AC identity header
```

### Slug rule

`NNN_<ac_name_lowercased_hyphens_and_spaces_to_underscores>`

Examples:
- AC 1 Mekliganj → `001_mekliganj`
- AC 19 Dabgram-Fulbari → `019_dabgram_fulbari`
- AC 22 Kalimpong → `022_kalimpong`

---

## Per-agent task sequence

Each agent receives: AC number, AC name, slug. Reservation status (GEN/SC/ST) must be sourced from Delimitation Commission 2008 via Wikipedia or ECI — it is not in the 2019 votes CSV.

1. Read `constituency_data/TEMPLATE_AC_NNN_2019.md`
2. Read `constituency_data/NORMALIZED_SCHEMA.md`
3. Read `kaisim/pipeline/skills/structured-data-layer/SKILL.md`
4. Read reference example: `constituency_data/constituencies/095_bangaon_uttar/2019/095_bangaon_uttar_2019.md`
5. Extract this AC's 2019 vote data from `data/2019_AssemblySegmentLevelVotingData.csv`
6. Web-search for: Census 2011 CDB/GP breakdown, Wikipedia AC page, district demographics, ECI 2019 result confirmation
7. Fill in all sections A–H following `NORMALIZED_SCHEMA.md`, applying the freeze rule (no post-2019 references), tiering every cell honestly (A–E)
8. Create directory scaffold (mkdir all subdirs, stub `events.yaml`)
9. Write MD to `constituency_data/constituencies/NNN_slug/2019/NNN_slug_2019.md`
10. Run `python3 kaisim/scripts/derive_calibrated_2019_csvs.py NNN` from project root
11. Report: success/failure, derivation errors, any cells that fell back to Tier-E due to data gaps

---

## Parallelism

All 20 agents fire simultaneously via `superpowers:dispatching-parallel-agents`. Main agent waits for all 20 to complete, then collects a summary report (per-AC status, derivation pass/fail, elapsed time, token usage if visible).

---

## What this batch does NOT cover

- 2021 / 2024 MD population (future sprint)
- Validation gate runs (`validate_calibrated_2019.py`) — deferred to post-batch cleanup
- The remaining 264 constituencies — pending batch 1 cost/time measurement
- CSV audit gate reports

---

## Success criteria for batch 1

- All 20 `NNN_slug_2019.md` files written and non-empty
- All 20 derivation script runs exit 0 (or errors logged per AC)
- Directory scaffold present for all 20 ACs
- Wall time and approximate token cost recorded for planning subsequent batches
