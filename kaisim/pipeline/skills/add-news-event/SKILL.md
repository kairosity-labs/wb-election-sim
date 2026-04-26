---
name: add-news-event
description: Add a new news/event entry to a Kaisim simulation's events YAML — with proper tags, valence per identity tag, scope, intensity, and source URLs. Use when the user wants to "add a news event", "include event X in the simulation", "add to the event chronology", or "make sure event Y reaches voters".
---

# Kaisim — Add a News Event

You are adding one entry to a simulation's `news/events_<period>.yaml` file.
Each event has strict metadata that drives downstream selection + belief updates.

## Step 1 — Verify date is BEFORE election cutoff

Read the YAML's `cutoff_date:` field. The new event's `date` (or
`date_start`) MUST be on or before the cutoff.

Common mistake: adding a post-election event "for context". Don't.

## Step 2 — Decide temporal type

  - **`episodic`** = single-date shock (cyclone landfall, court ruling, defection)
  - **`chronic`** = multi-month drift (COVID era, scheme rollout, ongoing scandal)

Episodic uses `date:`. Chronic uses `date_start:` + `date_end:`.

## Step 3 — Decide scope

  - `national` — top of national news cycle (CAA Rules, Modi rallies)
  - `state` — top of state news cycle (Sandeshkhali, SSC scam, WB AE results)
  - `district` — district-level resonance (specific to N24P / N. Bengal)
  - `AC` — hyper-local (Thakurnagar visits, Petrapole-specific)

**Pitfall:** if news got national TV coverage, scope is at least `state`,
even if it physically happened in one district. Sandeshkhali was technically
district-located but its news scope was `state`.

## Step 4 — Decide intensity (1-5)

  - `5` — top-of-mind for the affected demographic for weeks (CAA Rules,
    Lakshmir Bhandar launch, Partha arrest)
  - `4` — major news, persistent for days (Sandeshkhali, Cyclone Amphan)
  - `3` — notable, but quickly displaced (BSF jurisdiction extension,
    cabinet reshuffle without local figure)
  - `2` — minor, mostly registers in narrow demographic
  - `1` — barely noticed by general public (procedural court hearings)

## Step 5 — Tag the event

Use only tags from the controlled vocabulary (see other events for
reference). If you need a new tag, add it AND document it in
`derived/persona_tags.py` so personas can match it.

Standard tags:
  - **Identity**: matua_refugee, woman, elderly, upper_caste_hindu, bhadralok,
    muslim_voter
  - **Economic**: cultivator, ag_labourer, urban_trader, petrapole_economy,
    out_migrant_household, school_age_household
  - **Welfare beneficiary**: lakshmir_bhandar_beneficiary,
    krishak_bandhu_beneficiary, swasthya_sathi_beneficiary,
    khadya_sathi_beneficiary, kanyashree_household, sabuj_sathi_household
  - **Partisan**: bjp_supporter, tmc_supporter

## Step 6 — Set valence per tag

For each tag, decide the directional pull:
  - `positive` — this event makes that group MORE likely to support the
    party that benefits
  - `negative` — this event pushes that group AWAY from the party
    associated
  - `ambient` — touches them but doesn't shift politically

**Critical asymmetry**: the SAME event often has OPPOSITE valence for
different identities. CAA Rules: `matua_refugee: positive`,
`muslim_voter: negative`. Don't forget the opposite-valence pair.

## Step 7 — Set broadcast flag

  - `true` — reached via TV / radio / state press; everyone with media
    engagement might see it (default for `national` + `state` scope at
    intensity ≥ 4)
  - `false` — only via targeted networks (Mahasangha pamphlets, mosque
    networks, trader-WhatsApp groups). Use for AC-scope identity-specific
    events.

## Step 8 — Cite at least one real URL

Every event needs `sources:` with at least 1 real URL. Wikipedia, ECI,
mainstream press (Wire, Hindu, Indian Express), or reputable secondary
sources. **NO fabricated URLs.**

## Template

```yaml
  - slug: <short_snake_case_name>
    date: "YYYY-MM-DD"                     # OR date_start + date_end for chronic
    temporal: episodic                     # episodic | chronic
    scope: state                           # national | state | district | AC
    intensity: 4                           # 1-5
    headline: "One-sentence headline"
    summary: |
      2-3 sentences explaining what happened and why it matters for voters
      in this constituency. Be specific about geographic + identity
      relevance.
    tags: [tag1, tag2, tag3]
    valence:
      tag1: positive
      tag2: negative
      bjp_supporter: positive    # always include party-supporter valence
      tmc_supporter: negative
    broadcast: true
    sources:
      - https://en.wikipedia.org/wiki/...
      - https://www.thehindu.com/...
```

## Step 9 — Verify by re-running calibration

Adding an event affects targeting → may shift downstream simulation
results. After adding, re-run a small smoke test:

```bash
python kaisim/simulations/<sim>/run_simulation.py _smoke   # if smoke config exists
```

Confirm the new event appears in agents' feeds.jsonl with sensible scores.

## Reference

  - Audit framework: 3-agent ensemble for event metadata, see
    `kaisim/simulations/wb_2021_ac095/news/events_2019_2024.yaml` (audited)
  - Tag derivation: `kaisim/simulations/<sim>/derived/persona_tags.py`
  - Targeting selector: `kaisim/pipeline/simulation/targeting/rule_based.py`
