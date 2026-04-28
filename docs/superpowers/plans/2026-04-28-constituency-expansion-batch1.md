# Constituency Expansion — Batch 1 (20 ACs) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Populate 20 new WB constituency directories (ACs 1, 2, 4–10, 12–22) each with a fully calibrated 2019 MD following NORMALIZED_SCHEMA.md, then derive companion CSVs via the existing derivation script.

**Architecture:** Main agent runs a pre-flight check, then dispatches 20 parallel subagents simultaneously (one per AC). Each subagent researches its AC, writes the MD, scaffolds directories, and runs the CSV derivation script. Main agent collects results.

**Tech Stack:** Python 3, existing `kaisim/scripts/derive_calibrated_2019_csvs.py`, web search, on-disk 2019 voting CSV, NORMALIZED_SCHEMA.md template.

---

## File map

**Created per AC (×20):**
- `constituency_data/constituencies/NNN_slug/2019/NNN_slug_2019.md` — primary artifact
- `constituency_data/constituencies/NNN_slug/2019/raw/` — empty dir, agent may drop scrapes here
- `constituency_data/constituencies/NNN_slug/2019/csv/NNN_*.csv` — derived by script
- `constituency_data/constituencies/NNN_slug/2019/audit/` — empty dir (gate reports deferred)
- `constituency_data/constituencies/NNN_slug/2021/` — empty scaffold
- `constituency_data/constituencies/NNN_slug/2024/` — empty scaffold
- `constituency_data/constituencies/NNN_slug/events.yaml` — minimal stub

**Not created in this batch:**
- 2021/2024 MDs
- Audit gate reports (`validate_calibrated_2019.py` runs)

---

## Task 1: Pre-flight verification

**Files:** read-only checks, no writes

- [ ] **Step 1: Verify all prerequisites exist**

Run from project root `/home/ubuntu/wb-election-sim`:

```bash
python3 -c "
from pathlib import Path
checks = [
    'constituency_data/TEMPLATE_AC_NNN_2019.md',
    'constituency_data/NORMALIZED_SCHEMA.md',
    'kaisim/pipeline/skills/structured-data-layer/SKILL.md',
    'kaisim/scripts/derive_calibrated_2019_csvs.py',
    'data/2019_AssemblySegmentLevelVotingData.csv',
    'constituency_data/constituencies/095_bangaon_uttar/2019/095_bangaon_uttar_2019.md',
]
for c in checks:
    p = Path(c)
    status = '✓' if p.exists() else '✗ MISSING'
    print(f'{status}  {c}')
"
```

Expected: all 6 lines start with `✓`. If any show `✗ MISSING`, stop and fix before proceeding.

- [ ] **Step 2: Confirm the 20 target ACs are not already populated**

```bash
python3 -c "
from pathlib import Path
base = Path('constituency_data/constituencies')
batch1 = [
    ('001','mekliganj'), ('002','mathabhanga'), ('004','cooch_behar_dakshin'),
    ('005','sitalkuchi'), ('006','sitai'), ('007','dinhata'), ('008','natabari'),
    ('009','tufanganj'), ('010','kumargram'), ('012','alipurduars'),
    ('013','falakata'), ('014','madarihat'), ('015','dhupguri'), ('016','maynaguri'),
    ('017','jalpaiguri'), ('018','rajganj'), ('019','dabgram_fulbari'), ('020','mal'),
    ('021','nagrakata'), ('022','kalimpong'),
]
for ac, slug in batch1:
    d = base / f'{ac}_{slug}'
    print('EXISTS' if d.exists() else 'absent', d)
"
```

Expected: all 20 lines print `absent`. If any print `EXISTS`, skip that AC in Task 2.

- [ ] **Step 3: Commit pre-flight baseline**

```bash
git add -A
git status
```

No commit needed if working tree is clean. Proceed to Task 2.

---

## Task 2: Dispatch 20 parallel subagents

**Files:** creates all 20 constituency directories and MDs

- [ ] **Step 1: Dispatch all 20 agents simultaneously**

Fire all 20 agents in a **single parallel batch** using the Agent tool with `subagent_type: general-purpose`. Each agent receives the prompt template below, with its specific AC metadata substituted in.

**Agent prompt template** (fill in `{{AC_NO}}`, `{{AC_NAME}}`, `{{SLUG}}`, `{{ELECTORS}}`, `{{TOTAL_VOTES}}`, `{{TOP3_VOTE_PCT}}`):

---

```
You are populating one West Bengal constituency for the kaisim election simulation project.

Working directory: /home/ubuntu/wb-election-sim

## Your assignment
AC number: {{AC_NO}}
AC name: {{AC_NAME}}
Directory slug: {{SLUG}}
2019 LS electorate: {{ELECTORS}}
2019 LS total valid votes: {{TOTAL_VOTES}}
2019 LS top-3 party vote shares: {{TOP3_VOTE_PCT}}

## What you must produce
1. A fully filled 2019 calibrated MD at:
   constituency_data/constituencies/{{AC_NO}}_{{SLUG}}/2019/{{AC_NO}}_{{SLUG}}_2019.md
2. Directory scaffold (see below)
3. A minimal events.yaml stub
4. Run the CSV derivation script and report results

## Step-by-step instructions

### Step 1 — Read these files in full before doing anything else
- constituency_data/TEMPLATE_AC_NNN_2019.md
- constituency_data/NORMALIZED_SCHEMA.md
- kaisim/pipeline/skills/structured-data-layer/SKILL.md
- constituency_data/constituencies/095_bangaon_uttar/2019/095_bangaon_uttar_2019.md  ← reference implementation

### Step 2 — Extract this AC's full 2019 vote breakdown from the CSV
Run:
  python3 -c "
  import csv
  with open('data/2019_AssemblySegmentLevelVotingData.csv', encoding='utf-8-sig') as f:
      rows = list(csv.DictReader(f))
  ac = [r for r in rows if 'West Bengal' in r.get('State-UT Code & Name','') and r['AC NO'].strip() == '{{AC_NO_INT}}']
  for r in ac:
      print(r['PARTY'], r['VOTES SECURED EVM'], 'electors='+r['TOTAL ELECTORS'])
  "

### Step 3 — Research (web search)
Search for the following, in order of priority:
1. "{{AC_NAME}} assembly constituency West Bengal Wikipedia" — get: LS constituency it belongs to, reservation status (GEN/SC/ST), geographic description, sub-units/blocks
2. "{{AC_NAME}} constituency Census 2011 West Bengal community development block" — get: CDB population, rural/urban split, GP list
3. "{{AC_NAME}} constituency demographics religion caste West Bengal" — get: religion breakdown, SC/ST population share
4. District Wikipedia page for {{AC_NAME}}'s district — get: district religion/caste table from Census 2011 as a fallback for demographic data
5. "{{AC_NAME}} West Bengal election 2019 results ECI" — confirm vote shares match the CSV data

Reservation status (GEN/SC/ST) MUST come from Delimitation Commission 2008 — check Wikipedia or ECI. It is NOT in the 2019 votes CSV.

### Step 4 — Create directory scaffold
```bash
mkdir -p constituency_data/constituencies/{{AC_NO}}_{{SLUG}}/2019/raw
mkdir -p constituency_data/constituencies/{{AC_NO}}_{{SLUG}}/2019/csv
mkdir -p constituency_data/constituencies/{{AC_NO}}_{{SLUG}}/2019/audit
mkdir -p constituency_data/constituencies/{{AC_NO}}_{{SLUG}}/2021
mkdir -p constituency_data/constituencies/{{AC_NO}}_{{SLUG}}/2024
```

### Step 5 — Write events.yaml stub
Write constituency_data/constituencies/{{AC_NO}}_{{SLUG}}/events.yaml with this minimal content (fill in real values from your research):

```yaml
# AC {{AC_NO}} — {{AC_NAME}} events
# Stub created during batch-1 expansion. Full event timeline to be added in future sprint.
cutoff_date: '2026-04-26'
events:
- slug: ls_2019_{{SLUG}}_result
  date: '2019-05-23'
  temporal: episodic
  scope: AC
  intensity: 5
  headline: "2019 LS result for {{AC_NAME}} segment: {{TOP3_BRIEF}}"
  summary: "2019 Lok Sabha result within AC {{AC_NO}} segment. Calibration anchor."
  tags: []
  valence: {}
  broadcast: true
  sources:
  - data/2019_AssemblySegmentLevelVotingData.csv
```

### Step 6 — Write the 2019 calibrated MD
File path: constituency_data/constituencies/{{AC_NO}}_{{SLUG}}/2019/{{AC_NO}}_{{SLUG}}_2019.md

Follow TEMPLATE_AC_NNN_2019.md and NORMALIZED_SCHEMA.md exactly. Rules:
- Section IDs A through H are load-bearing — do not rename or merge
- The section heading `### C.N` and `### D.N` format must be followed exactly
- Every cell needs a Tier (A/B/C/D/E) and a Source
- FREEZE RULE: the file must not reference any event after 2019. Forbidden keywords: 2020, 2021, 2022, 2023, 2024, 2025, 2026, COVID-19, coronavirus, Amphan, SSC scam, RG Kar, Lakshmir Bhandar, SIR
- Use Tier A for: 2019 LS vote data from the CSV, ECI electorate numbers
- Use Tier B/C for: Census 2011 CDB-level data you find via web search
- Use Tier D for: journalistic estimates
- Use Tier E for: projections and any imputed values where no direct source was found
- C.14 (asset/media) and C.15 (amenities) do NOT sum to 100 — these are independent ownership rates
- All other C sections must sum to 100.00 (add a Sum row)
- Sub-unit decomposition (section A, bottom row): divide the AC into 2 sub-units minimum (urban vs rural, or by block) for GP-conditioning in sections D.11–D.14. If you cannot find block-level split, use district urban/rural ratio as Tier-E proxy.

For demographic data that is unavailable at AC level, use district-level Census 2011 data as Tier-E fallback, citing the district and noting it is a district rollup.

Section H (Post-2019 validation anchors) should include the 2021 AE result for this AC if you can find it — but mark it clearly as OUT-OF-SAMPLE only.

### Step 7 — Run CSV derivation
From project root:
```bash
python3 kaisim/scripts/derive_calibrated_2019_csvs.py {{AC_NO_PADDED}}
```

Report: whether it exited 0, any errors printed, which CSV files were created in constituency_data/constituencies/{{AC_NO}}_{{SLUG}}/2019/csv/.

### Step 8 — Final report
Return a summary with:
- AC number and name
- Reservation status found
- Which sections had Tier-A data vs Tier-E fallbacks
- Whether derivation script succeeded (exit 0 / errors)
- Any data gaps you could not fill
```

---

**The 20 agent invocations** (substitute values from this table):

| AC_NO | AC_NO_INT | AC_NAME | SLUG | ELECTORS | TOTAL_VOTES | TOP3_VOTE_PCT |
|---|---|---|---|---|---|---|
| 001 | 1 | Mekliganj | mekliganj | 216864 | 186768 | BJP 46.7%, AITC 44.1%, CPIM 4.4% |
| 002 | 2 | Mathabhanga | mathabhanga | 241785 | 205518 | BJP 52.1%, AITC 41.9%, AIFB 2.8% |
| 004 | 4 | Cooch Behar Dakshin | cooch_behar_dakshin | 223411 | 180842 | BJP 47.8%, AITC 44.5%, AIFB 4.0% |
| 005 | 5 | Sitalkuchi | sitalkuchi | 275720 | 234468 | AITC 46.8%, BJP 46.3%, AIFB 3.0% |
| 006 | 6 | Sitai | sitai | 277195 | 222772 | AITC 55.3%, BJP 39.7%, INC 2.0% |
| 007 | 7 | Dinhata | dinhata | 288755 | 228252 | BJP 50.4%, AITC 43.6%, AIFB 2.6% |
| 008 | 8 | Natabari | natabari | 235277 | 204796 | BJP 51.0%, AITC 42.0%, AIFB 3.7% |
| 009 | 9 | Tufanganj | tufanganj | 225957 | 199554 | BJP 49.5%, AITC 45.7%, RSP 2.7% |
| 010 | 10 | Kumargram | kumargram | 262525 | 219829 | BJP 52.8%, AITC 39.7%, RSP 4.3% |
| 012 | 12 | Alipurduars | alipurduars | 249960 | 208442 | BJP 55.1%, AITC 37.4%, RSP 4.1% |
| 013 | 13 | Falakata | falakata | 244579 | 206388 | BJP 52.9%, AITC 39.8%, RSP 5.0% |
| 014 | 14 | Madarihat | madarihat | 203374 | 155313 | BJP 60.2%, AITC 32.0%, RSP 3.6% |
| 015 | 15 | Dhupguri | dhupguri | 251681 | 215112 | BJP 49.2%, AITC 40.9%, CPIM 6.1% |
| 016 | 16 | Maynaguri | maynaguri | 251373 | 220665 | BJP 50.2%, AITC 43.5%, CPIM 2.7% |
| 017 | 17 | Jalpaiguri | jalpaiguri | 255369 | 214625 | BJP 52.3%, AITC 34.0%, CPIM 7.6% |
| 018 | 18 | Rajganj | rajganj | 233915 | 204573 | AITC 46.3%, BJP 44.2%, CPIM 4.9% |
| 019 | 19 | Dabgram-Fulbari | dabgram_fulbari | 283995 | 237413 | BJP 63.4%, AITC 27.1%, CPIM 5.6% |
| 020 | 20 | Mal | mal | 242267 | 198646 | BJP 50.8%, AITC 38.7%, CPIM 4.6% |
| 021 | 21 | Nagrakata | nagrakata | 226235 | 177813 | BJP 58.4%, AITC 30.2%, RSP 6.0% |
| 022 | 22 | Kalimpong | kalimpong | 205462 | 144141 | BJP 67.2%, AITC 23.8%, IND 3.2% |

---

## Task 3: Validate batch output

**Files:** read-only checks

- [ ] **Step 1: Check all 20 MDs were written**

```bash
python3 -c "
from pathlib import Path
base = Path('constituency_data/constituencies')
batch1 = [
    ('001','mekliganj'), ('002','mathabhanga'), ('004','cooch_behar_dakshin'),
    ('005','sitalkuchi'), ('006','sitai'), ('007','dinhata'), ('008','natabari'),
    ('009','tufanganj'), ('010','kumargram'), ('012','alipurduars'),
    ('013','falakata'), ('014','madarihat'), ('015','dhupguri'), ('016','maynaguri'),
    ('017','jalpaiguri'), ('018','rajganj'), ('019','dabgram_fulbari'), ('020','mal'),
    ('021','nagrakata'), ('022','kalimpong'),
]
ok, fail = 0, 0
for ac, slug in batch1:
    md = base / f'{ac}_{slug}' / '2019' / f'{ac}_{slug}_2019.md'
    csv_dir = base / f'{ac}_{slug}' / '2019' / 'csv'
    md_ok = md.exists() and md.stat().st_size > 5000
    csv_count = len(list(csv_dir.glob('*.csv'))) if csv_dir.exists() else 0
    status = 'OK' if md_ok and csv_count >= 5 else 'FAIL'
    if status == 'OK': ok += 1
    else: fail += 1
    print(f'{status}  AC{ac}  md={md_ok}({md.stat().st_size if md.exists() else 0}b)  csvs={csv_count}')
print(f'---')
print(f'passed={ok}  failed={fail}')
"
```

Expected: 20 lines print `OK`, final line `passed=20  failed=0`.

- [ ] **Step 2: Spot-check freeze rule compliance on 3 random ACs**

```bash
python3 -c "
import random, re
from pathlib import Path
base = Path('constituency_data/constituencies')
slugs = [('001','mekliganj'), ('010','kumargram'), ('019','dabgram_fulbari')]
forbidden = ['2020','2021','2022','2023','2024','2025','2026','COVID','coronavirus','Amphan','SSC scam','RG Kar','Lakshmir Bhandar']
for ac, slug in slugs:
    md = base / f'{ac}_{slug}' / '2019' / f'{ac}_{slug}_2019.md'
    if not md.exists():
        print(f'MISSING {md}'); continue
    text = md.read_text()
    hits = [kw for kw in forbidden if kw in text]
    # Section H is exempt from freeze rule — strip it before checking
    text_no_h = re.split(r'## H\.', text)[0]
    hits = [kw for kw in forbidden if kw in text_no_h]
    print(f'AC{ac}: {\"CLEAN\" if not hits else \"LEAKAGE: \" + str(hits)}')
"
```

Expected: all 3 lines print `CLEAN`. Any `LEAKAGE` hits need manual review of that AC's MD.

- [ ] **Step 3: Report elapsed time and note for batch sizing**

Record the wall-clock time from Task 2 Step 1 dispatch to Task 3 Step 1 completion. This is the benchmark for estimating cost/time of subsequent 14 batches covering the remaining 264 constituencies.

- [ ] **Step 4: Commit all 20 new constituency directories**

```bash
git add constituency_data/constituencies/001_mekliganj \
        constituency_data/constituencies/002_mathabhanga \
        constituency_data/constituencies/004_cooch_behar_dakshin \
        constituency_data/constituencies/005_sitalkuchi \
        constituency_data/constituencies/006_sitai \
        constituency_data/constituencies/007_dinhata \
        constituency_data/constituencies/008_natabari \
        constituency_data/constituencies/009_tufanganj \
        constituency_data/constituencies/010_kumargram \
        constituency_data/constituencies/012_alipurduars \
        constituency_data/constituencies/013_falakata \
        constituency_data/constituencies/014_madarihat \
        constituency_data/constituencies/015_dhupguri \
        constituency_data/constituencies/016_maynaguri \
        constituency_data/constituencies/017_jalpaiguri \
        constituency_data/constituencies/018_rajganj \
        constituency_data/constituencies/019_dabgram_fulbari \
        constituency_data/constituencies/020_mal \
        constituency_data/constituencies/021_nagrakata \
        constituency_data/constituencies/022_kalimpong

git commit -m "feat: add batch-1 calibrated 2019 MDs for ACs 1-2,4-10,12-22 (20 constituencies)"
```
