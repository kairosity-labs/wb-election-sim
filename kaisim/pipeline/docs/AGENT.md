# Kaisim — What is an Agent?

An **agent** is a synthetic voter that lives through a chronology of news,
forms beliefs, and ultimately votes. Each agent wraps a **persona** with
runtime simulation state.

```
Agent
├── Persona                       # static — generated in Phase 1
│   ├── id                        #   "default_n100_v1_p0042"
│   ├── fields                    #   structured demographic dict
│   │   ├── religion, caste, age_cohort, gender, mother_tongue
│   │   ├── education, workforce_status, occupation, economic_status
│   │   ├── gp_location, household_type, marital_status, migration
│   │   ├── asset_media           #   {TV, Radio, Mobile, Smartphone, ...}
│   │   ├── amenities             #   {Drinking_water, Electricity, LPG, ...}
│   │   ├── welfare_exposure      #   {Krishak_Bandhu, Kanyashree, ...}
│   │   ├── welfare_dominant      #   the most-touched scheme
│   │   └── vote_2019_LS          #   2019 LS vote (the "anchor prior")
│   └── narrative
│       └── self_prompt           #   first-person bio LLM uses as system prompt
│
├── Runtime state                 # mutable — built in Phase 2
│   ├── tags                      #   set of identity tags (matua_refugee, etc.)
│   ├── media_engagement          #   0.3-1.5 multiplier on news reception
│   └── memory_stream             #   append-only log of MemoryItem
│       └── MemoryItem(timestamp, kind, content, importance,
│                     triggering_event_slug, structured_delta)
│
└── Disk artifacts                # written incrementally during the run
    ├── persona.json              #   snapshot
    ├── memory_stream.jsonl       #   one MemoryItem per line
    ├── feeds.jsonl               #   one news-delivery decision per line
    ├── structured_history.jsonl  #   one structured delta per line
    ├── final_vote.json           #   final-query result
    ├── belief_narrative.md       #   regenerated belief summary
    └── agent_meta.json           #   tags, media_engagement, etc.
```

## Personas — the static substrate

Personas are **synthesized in Phase 1** from joint demographic distributions
(census + NFHS + electoral surveys). For an n=100 persona set, a typical
generation pipeline:

1. Sample demographic axes from joint constraints (religion × caste ×
   gender × age × education × ...).
2. Verify against marginals (Pearson chi-square, z-score).
3. Render `narrative.self_prompt` via an LLM call seeded with the structured
   fields ("You are a 24-year-old Namasudra-Matua woman from Akaipur GP...").

The persona's `self_prompt` is what makes it feel real. Sample (a real
n=100 persona from `wb_2021_ac095`):

> You are Rimpa Halder, a 24-year-old Namasudra-Matua Hindu woman living
> in Akaipur GP, married a year ago to a man whose elder brother works
> construction in Kerala. Your family originally came from Khulna in the
> 1970s. You completed Higher Secondary from the local school — you
> received a Kanyashree stipend for three years which helped your father
> keep you in school rather than marrying you off at sixteen. ...
> Your husband voted BJP in the 2019 Lok Sabha because of the CAB. You
> voted AITC. You do not say this openly because the household is divided,
> but Mamata-didi's schemes have touched your life in concrete ways. ...

The LLM sees this as the system prompt for *every* update call. It is
the load-bearing element of behavioral realism.

## What's interesting in the WB persona set

From the n=100 set actually used in the audited run:

- **Inter-religious schisms inside one household.** Personas where the
  spouse voted opposite — woman AITC because of Lakshmir Bhandar / Kanyashree,
  husband BJP because of CAA / migration. These produce the most authentic
  switcher narratives because the LLM has *internal conflict* to resolve.
- **Matua refugee continuity.** ~36% of personas are Namasudra-Matua;
  many have grandparents who came from Khulna / Jessore in the 1970s —
  the persona prompt makes the Bangladesh-origin felt concretely (relatives
  still there, citizenship anxiety, NRC fear) rather than abstractly.
- **Multi-generational welfare exposure.** A persona may have one parent
  on Khadya Sathi (rice subsidy), one teen daughter on Kanyashree
  (girl-education stipend), grandmother on Swasthya Sathi (insurance),
  grandfather on PM-Kisan (farmer income). This four-program touch is
  what makes "scheme delivery" the dominant frame for AITC support.
- **Petrapole economy.** Bangaon Uttar contains the Petrapole India-Bangladesh
  land-port. Personas with `occupation=Trader / Truck driver / Daily-wage
  hand` near Petrapole get a distinct sub-narrative (border-trade
  disruption from BD politics, BSF jurisdiction expansion, etc.).

Less interesting (but realistic) personas:

- Default-template farmers without strong tag overlap on key events tend
  to receive < 10 events over 4 years and show flat trust traces.
  These are real silent-majority voters, but make boring narratives.

## Tags — derived per-agent identity

Tags are derived from persona fields by `derived/persona_tags.py` (per-sim).
They are how the targeting system matches events to agents. WB-2021-AC95
tag derivation:

```python
tags = set()
if persona["fields"]["caste"] == "Namasudra_Matua":
    tags.add("matua_refugee" if migration == "Bangladesh" else "matua_local")
if persona["fields"]["gender"] == "Female":
    tags.add("woman")
if persona["fields"]["age_cohort"] in ("63_67", "68plus"):
    tags.add("elderly")
if persona["fields"]["caste"] == "UC_bhadralok":
    tags.add("upper_caste_hindu"); tags.add("bhadralok")
if persona["fields"]["religion"] == "Muslim":
    tags.add("muslim_voter")
# ... economic, welfare-beneficiary, partisan tags ...
if persona["fields"].get("vote_2019_LS") == "BJP":
    tags.add("bjp_supporter")
```

A tag overlap with an event's `tags:` list adds to the event's targeting
score (see `INFORMATION_SYSTEM.md`).

## Media engagement — derived per-agent gain

A multiplier on the targeting score:

```python
score = 0.3                        # base — illiterate, no media
if persona["fields"]["asset_media"]["Smartphone"]: score += 0.5
if persona["fields"]["asset_media"]["TV"]:        score += 0.3
if persona["fields"]["education"] in (
        "Higher_Secondary", "Graduate", "Postgraduate"): score += 0.2
return min(score, 1.5)
```

Range 0.3 to 1.5. A high-engagement urban graduate gets 5× the news
firehose of a low-engagement rural illiterate; this is a primary mechanism
for the realistic ignore-rate observed (~7% in WB, much higher among
elderly + low-education segments).

## Memory stream — accumulated belief substrate

A `MemoryItem` is one of:

| kind | populated by | content |
|---|---|---|
| `reaction` | park_minimal updater | LLM monologue about a delivered event |
| `reflection` | reflection updater | LLM gist compressing older memories |
| `noticed` | (unused — placeholder for ambient sensing) | — |

Reactions are dense (one per accepted event). Reflections compress: every
12 ticks (configurable), older raw memories are replaced by a single
`reflection` MemoryItem holding their gist. This caps memory window growth
at roughly O(ticks/12) reflections + last-N raw reactions — typically
10-20 items in the LLM's context window even after 53 ticks.

### Why retrieval is unnecessary at this scale

Park's "Generative Agents" used embedding retrieval over thousands of
micro-observations per agent per day. Kaisim has ≤ 38 events × 100 agents
over 53 ticks; per-agent memory tops out at ~30 items. The full memory
stream fits in context; retrieval would add latency without adding signal.

If a future sim has >100 events per agent (e.g., a live-feed news
ingestion experiment), drop in an embedding retriever as a new updater
strategy.

## Final vote — the integration point

After the last tick, `final_query.py` runs one LLM call per agent with
`reasoning=medium`. The LLM sees:
  - the persona (`self_prompt`)
  - the full reflection-compressed memory stream
  - the choice menu (BJP / AITC / INC / LF / Other / NOTA)

It returns: `{vote, reasoning, confidence, primary_drivers}`.

This is where movement crystallizes. ~80% of accepted events emit
`party_lean_change=no_change` during the tick loop; the final_query is
the moment the LLM integrates the *whole* memory stream against persona
commitments and produces a vote.

The `reasoning` field is the gold of every run. Sample:

> *"I have seen Didi's schemes reach my hands — my cycle, my rice at two
> rupees, my mother-in-law alive. When I look at Shantanu's CAA promise
> now, on polling day, I see only fourteen certificates and a few hundred
> digital files for lakhs of people like my husband's grandfather. 'Can
> apply' is not a certificate in hand. ... I will vote for the woman who
> gave me things I can hold, and who promises to protect me from the one
> thing that truly frightens me."*

That's what an agent looks like, fully alive.
