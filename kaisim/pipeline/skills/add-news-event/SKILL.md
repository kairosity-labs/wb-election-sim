---
name: add-news-event
description: Research and add news events for a constituency — national/state events go to constituency_data/state_events_2019_2026.yaml (only if not already present), district/AC events go to constituency_data/constituencies/{name}/events.yaml. Use when the user says "add news events for AC NNN", "update the event chronology for <constituency>", "add event X to the simulation", or "backfill events for <year range>".
---

# Kaisim — Add News Events for a Constituency

You are adding voter-salient events for one constituency and one time window.
Events are split across two files by scope:

```
constituency_data/
  state_events_2019_2026.yaml          ← scope: national | state
  constituencies/
    {id}_{name}/
      events.yaml                      ← scope: district | AC only
```

---

## Step 1 — Identify the constituency and time window

Confirm with the user:
- AC ID + name slug (e.g. `003_cooch_behar_uttar`)
- Time window to research (e.g. `2024-01-01 to 2026-04-26`)

Find the two target files:

```bash
ls constituency_data/constituencies/{id}_{name}/events.yaml
ls constituency_data/state_events_2019_2026.yaml
```

Read both files' `cutoff_date:` fields. New events MUST have `date` (or
`date_start`) on or before the cutoff.

---

## Step 2 — Research events for the constituency

Use web search to find voter-salient events for this AC and time window.
Research in two passes:

**Pass A — National & state events** (things that affected all of WB or all
of India, but are particularly salient for this constituency's demographics):

Search: `"West Bengal {year} major news"`, `"India {year} election events"`,
`"{district} {year} news"`, `"West Bengal government scheme {year}"`.

Collect: CAA/NRC developments, WB government scheme launches, major election
results, national political events, cyclones/disasters, economic shocks.

**Pass B — Constituency-specific events** (district or AC-level):

Search: `"{constituency name} {year} news"`, `"{local leader} {year}"`,
`"{district} panchayat/election/land/violence {year}"`.

Collect: local election results, candidate defections, panchayat violence,
local economic events (crop failure, factory closure, land acquisition),
local communal incidents, constituency-specific welfare delivery news.

---

## Step 3 — Classify each event by scope

Assign one scope to each event:

| Scope | Meaning | Example |
|---|---|---|
| `national` | Top of national news cycle | CAA Rules notified, PM Modi rally |
| `state` | Top of WB state news | SSC scam arrest, WB AE result, Sandeshkhali |
| `district` | District-level resonance | Flood in specific district, district SP transfer |
| `AC` | Hyper-local to this constituency | Candidate visit, local panchayat result, specific scheme delivery |

**Pitfall:** if an event got national/state TV coverage, scope is at least
`state` even if it physically happened in one district. Route it to the
state file, not the AC file.

---

## Step 4 — Check state file before adding national/state events

For every `national` or `state` event you found:

```bash
grep "slug:" constituency_data/state_events_2019_2026.yaml | grep "<slug_candidate>"
```

Or search by headline keyword:

```bash
grep -i "<keyword>" constituency_data/state_events_2019_2026.yaml
```

**If a matching event already exists in the state file: SKIP IT.** Do not
add a duplicate. Note that the same real-world event may appear under a
slightly different slug — check by headline/keyword, not just slug.

**If the event is absent: add it to the state file.**

---

## Step 5 — Build each event's metadata

For every event (state or local), fill in all fields:

### 5a — Temporal type

- **`episodic`** — single-date shock. Use `date: "YYYY-MM-DD"`.
- **`chronic`** — multi-month drift (scheme rollout, ongoing crisis, election
  campaign period). Use `date_start:` + `date_end:`.

### 5b — Intensity (1–5)

| Score | Meaning |
|---|---|
| `5` | Top-of-mind for affected demographic for weeks |
| `4` | Major news, persistent for days |
| `3` | Notable but quickly displaced |
| `2` | Minor, registers in narrow demographic |
| `1` | Barely noticed by general public |

### 5c — Tags

Use only tags from the controlled vocabulary. Standard tags:

- **Identity**: `matua_refugee`, `woman`, `elderly`, `upper_caste_hindu`,
  `bhadralok`, `muslim_voter`, `adivasi_tribal`, `sc_voter`, `obc_voter`
- **Economic**: `cultivator`, `ag_labourer`, `urban_trader`,
  `out_migrant_household`, `school_age_household`, `industrial_worker`,
  `fisherman_prawn_farmer`, `tea_garden_worker`
- **Welfare beneficiary**: `lakshmir_bhandar_beneficiary`,
  `krishak_bandhu_beneficiary`, `swasthya_sathi_beneficiary`,
  `khadya_sathi_beneficiary`, `kanyashree_household`
- **Partisan**: `bjp_supporter`, `tmc_supporter`, `left_voter`

For AC-specific events, add AC-local tags (e.g. `petrapole_economy`,
`matua_mahasangha`, `rajbanshi_gcpa`) — document new tags in the AC's
`derived/persona_tags.py`.

### 5d — Valence per tag

For each tag on the event, decide the directional pull:

- `positive` — event makes that group more likely to support the
  party that benefits
- `negative` — pushes that group away from the associated party
- `ambient` — touches them but doesn't shift politically

**Critical rule:** the SAME event often has OPPOSITE valence for different
identity groups. Always include the opposite-valence pair. Example — CAA
notification: `matua_refugee: positive`, `muslim_voter: negative`.

### 5e — Broadcast flag

- `true` — reached via TV / state press; everyone with media engagement
  might see it (default for `national` + `state` scope at intensity ≥ 4)
- `false` — only via targeted networks (WhatsApp groups, community
  networks, local pamphlets). Use for AC-scope identity-specific events.

### 5f — Source URL

Every event needs `sources:` with at least one real URL. Acceptable:
Wikipedia, ECI (results.eci.gov.in), mainstream press (The Wire, The Hindu,
Indian Express, NDTV, Anandabazar), reputable NGO/academic sources.
**No fabricated URLs.**

---

## Step 6 — Write events to the correct file

### For national/state events not already in the state file:

Read the current state file, find the correct chronological insertion
point, and append the new entries. Keep events sorted by date.

Target: `constituency_data/state_events_2019_2026.yaml`

### For district/AC events:

Read the constituency's events file and append new entries, sorted by date.

Target: `constituency_data/constituencies/{id}_{name}/events.yaml`

**Never write a `national` or `state` event to the constituency file.**
**Never write a `district` or `AC` event to the state file.**

---

## Event template

```yaml
  - slug: <short_snake_case_identifier>
    date: "YYYY-MM-DD"                    # OR date_start + date_end for chronic
    temporal: episodic                    # episodic | chronic
    scope: state                          # national | state | district | AC
    intensity: 4                          # 1-5
    headline: "One-sentence headline describing the event"
    summary: |
      2-3 sentences. What happened, why it matters for voters in this
      constituency, and which identities it reaches most directly.
    tags: [tag1, tag2, tag3]
    valence:
      tag1: positive
      tag2: negative
      bjp_supporter: positive             # always include party-supporter valence
      tmc_supporter: negative
    broadcast: true
    sources:
      - https://en.wikipedia.org/wiki/...
      - https://www.thehindu.com/...
```

---

## Step 7 — Verify (mandatory — do not skip)

Run this single check after every write. It catches all three failure modes:
scope leakage, cross-file duplicates, and ordering errors.

```bash
python3 - <<'EOF'
import yaml
from pathlib import Path

STATE_FILE = Path("constituency_data/state_events_2019_2026.yaml")
CONSTS_DIR = Path("constituency_data/constituencies")

state_data = yaml.safe_load(STATE_FILE.read_text()) or {}
state_slugs = {e["slug"] for e in state_data.get("events", [])}
state_scopes = {e["slug"]: e.get("scope") for e in state_data.get("events", [])}

errors = []

# 1. Scope violations in the state file (district/AC events must not be there)
bad_scope_state = [s for s, sc in state_scopes.items() if sc in ("district", "AC")]
if bad_scope_state:
    errors.append(f"STATE FILE has district/AC-scoped events: {bad_scope_state}")

# 2. Cross-file duplicates — a slug must not appear in both state file AND any AC file
for ac_file in sorted(CONSTS_DIR.glob("*/events.yaml")):
    ac_data = yaml.safe_load(ac_file.read_text()) or {}
    ac_events = ac_data.get("events", [])
    ac_name = ac_file.parent.name

    # 2a. Slugs present in both files
    ac_slugs = {e["slug"] for e in ac_events}
    overlap = ac_slugs & state_slugs
    if overlap:
        errors.append(f"{ac_name}: slugs in BOTH state and AC file: {sorted(overlap)}")

    # 2b. national/state-scoped events in the AC file
    bad_scope_ac = [e["slug"] for e in ac_events if e.get("scope") in ("national", "state")]
    if bad_scope_ac:
        errors.append(f"{ac_name}: national/state events in AC file: {bad_scope_ac}")

    # 3. Chronological order
    dates = [str(e.get("date", e.get("date_start", ""))) for e in ac_events]
    if dates != sorted(dates):
        errors.append(f"{ac_name}: events not sorted chronologically")

# 3. Chronological order in state file
state_dates = [str(e.get("date", e.get("date_start", ""))) for e in state_data.get("events", [])]
if state_dates != sorted(state_dates):
    errors.append("STATE FILE: events not sorted chronologically")

if errors:
    print("VERIFICATION FAILED:")
    for e in errors:
        print(f"  ✗ {e}")
else:
    print("✓ All checks passed — no cross-file duplicates, no scope violations, all sorted.")
EOF
```

**If any check fails, fix before committing.** For cross-file duplicates,
remove the event from the AC file (it belongs only in the state file).

---

## Common pitfalls

| Pitfall | Prevention |
|---|---|
| Duplicating a state event that's already in state_events_2019_2026.yaml | Always grep by headline keyword before adding |
| Writing a state event into the AC file | Check scope before choosing target file |
| Post-cutoff date | Check `cutoff_date:` in the target file before writing |
| Fabricated source URL | Only cite URLs you retrieved from web search |
| Missing opposite-valence pair | For every tag with a strong valence, ask "who feels the opposite?" |
| Adding an event as episodic when it was a multi-month process | Use chronic + date_start/date_end for campaigns, schemes, ongoing crises |

---

## Reference

- **State events file:** `constituency_data/state_events_2019_2026.yaml`
- **AC events files:** `constituency_data/constituencies/*/events.yaml`
- **Scope/intensity worked examples:** `constituency_data/constituencies/095_bangaon_uttar/events.yaml`
- **Tag derivation:** `kaisim/simulations/<sim>/derived/persona_tags.py`
- **Targeting selector:** `kaisim/pipeline/simulation/targeting/rule_based.py`
- **Merge + split scripts:** `kaisim/scripts/merge_ac_events.py`, `kaisim/scripts/split_events_state_vs_ac.py`
