# Kaisim — Architecture

Kaisim is a two-phase pipeline for simulating elections:

1. **Phase 1 — persona generation**: synthesize a representative population
   of voter personas from joint demographic distributions, validate against
   marginals + joints, render each persona's "self prompt" (a first-person
   biography the LLM uses as system prompt).
2. **Phase 2 — belief evolution**: simulate that population living through
   a chronology of news events, with each agent's beliefs updated by an LLM
   per event, then queried for a final vote.

This file documents Phase-2 internals. Phase 1 is documented separately in
[`HOWTO_NEW_SIMULATION.md`](../HOWTO_NEW_SIMULATION.md).

## Top-level contracts

| Concept | Implementation | One-line role |
|---|---|---|
| `Persona` | `pipeline/core/persona.py` | A synthetic voter — fields + narrative.self_prompt |
| `Agent` | `pipeline/simulation/core/agent.py` | Persona + tags + media engagement + memory stream |
| `MemoryStream` | `pipeline/simulation/core/memory.py` | Append-only log of (timestamp, kind, content, importance) |
| `NewsPool` | `pipeline/simulation/core/event.py` | YAML-loaded events with tags/scope/intensity/valence |
| `Ticker` | `pipeline/simulation/core/clock.py` | Period iterator (month/week/quarter) with reflection trigger |
| `TargetingStrategy` | `pipeline/simulation/targeting/base.py` | Decides which events reach which agents per period |
| `Updater` | `pipeline/simulation/updaters/base.py` | One LLM call: persona + memory + event → reaction + delta |
| `Orchestrator` | `pipeline/simulation/orchestrator.py` | Async ticker loop fanning out updates over agents |
| `BeliefAnalysis` | `pipeline/simulation/belief_analysis.py` | Post-hoc plots + reports |

## Tick loop (single period)

```
for period in ticker:                                    # e.g. 2020-01, 2020-02, ...
    candidate_events = news_pool.active_in(period)
    async with Semaphore(max_concurrent):
        for agent in agents:                             # async-fanned
            selected = targeting.select(agent, candidate_events, period)
            for event in selected:
                feed_entry = score(agent, event)         # for audit
                if feed_entry.accepted:
                    delta = await updater.update(agent, event, period)
                    agent.memory_stream.add(delta.memory_item)
                    write_disk(delta)                    # incremental flush
            if ticker.should_reflect(period):
                await reflection_updater.compress_old_memories(agent)
```

After the final tick, the `final_query` updater asks every agent: *which
party will you vote for, why, what were the top drivers?*

## Pipeline layers

```
┌──────────────────────────────────────────────────────────────────┐
│  Phase 2 — Simulation                                            │
│                                                                  │
│  ┌───────────────┐  ┌────────────────┐  ┌────────────────┐       │
│  │  NewsPool     │  │  Targeting     │  │  Updaters      │       │
│  │  (events.yml) │→ │  Strategy      │→ │  (LLM calls)   │       │
│  │               │  │  (rule_based,  │  │  • park_min    │       │
│  │               │  │   show_all)    │  │  • reflection  │       │
│  └───────────────┘  └────────────────┘  │  • final_query │       │
│                              ▲          └────────────────┘       │
│                              │                  │                │
│                              │                  ▼                │
│                     ┌────────────────────────────────────┐       │
│                     │  Orchestrator (async tick loop)    │       │
│                     │  • per-period fan-out              │       │
│                     │  • semaphore concurrency           │       │
│                     │  • incremental disk flush          │       │
│                     └────────────────────────────────────┘       │
│                              │                                   │
│                              ▼                                   │
│                     ┌────────────────────────────────────┐       │
│                     │  Per-agent run state               │       │
│                     │  • memory_stream.jsonl             │       │
│                     │  • feeds.jsonl                     │       │
│                     │  • structured_history.jsonl        │       │
│                     │  • final_vote.json                 │       │
│                     └────────────────────────────────────┘       │
│                              │                                   │
│                              ▼                                   │
│                     ┌────────────────────────────────────┐       │
│                     │  belief_analysis.py                │       │
│                     │  • 8 plots                         │       │
│                     │  • per-event tables                │       │
│                     │  • per-demographic tables          │       │
│                     │  • Markdown report                 │       │
│                     └────────────────────────────────────┘       │
└──────────────────────────────────────────────────────────────────┘
```

## Design principles

### 1. LLM does cognition. Python does bookkeeping.

The Park-minimal updater gives the LLM the rich persona, the recent
memory window, and the new event — and asks it to decide engagement,
reaction, importance, party-lean change, trust changes. **Python does
not pre-compute a deterministic "expected reaction" then ask the LLM
to rationalize it.** The LLM is the cognition; Python only handles
selection (which events reach which agent), storage (memory stream
appends), and orchestration (when to reflect, when to query final vote).

This is deliberate. Earlier iterations wrapped LLM calls in deterministic
math (Hegselmann-Krause pre-filters, Friedkin-Johnsen blending, asymmetric
update-rates) to enforce "behavioral realism." The result: the LLM's
contribution became cosmetic. Reverting to Park-minimal restored the
qualitative richness — agents started reasoning about specific dates,
scheme names, leader names — and trust evolution became readable.

### 2. Pluggable strategies, not branching logic

`TargetingStrategy` is a `Protocol`. Implementing a new targeting policy
is a 50-line file in `targeting/`; it does not require touching the
orchestrator. Same for `Updater`: `park_minimal`, `reflection`, and
`final_query` are independent files; you can swap in `psychological_scaffold`
or `embedding_retrieval` without changing the loop.

### 3. Append-only, incremental flush

Every memory item, feed entry, and structured delta is JSON-encoded and
appended to a per-agent JSONL file *as it's generated*. This means:
  - You can `tail -f` any agent's memory stream live.
  - Killing the process loses no per-agent state up to the last flush.
  - Analysis can run on a partially-completed run.

### 4. Async fan-out per period

Inside one tick all per-agent work runs concurrently, bounded by an
asyncio semaphore. Concurrency 25-50 keeps Anthropic Haiku happy and
finishes 100 agents × 50 ticks (~2,500 LLM calls) in 12-18 minutes.

### 5. Reproducibility

Each run dir contains `config.snapshot.yaml` — the resolved config that
produced this run, including the exact persona-set hash and events-file
hash. Re-running the same snapshot reproduces results modulo LLM
non-determinism.

### 6. Pluggable LLM backend (cloud + local)

Both Phase-1 (`LLMBatchSampler`) and Phase-2 (`Orchestrator`) reach the LLM
through `pipeline.providers.make_provider(name, model, **kwargs)`. The
provider is selected per `simulation_config.yaml` / `persona_config.yaml`
under the `llm:` block:

```yaml
llm:
  provider: "anthropic"           # anthropic | openai
  model: "claude-haiku-4-5"
  reasoning: null
  temperature: 0.7
  max_tokens: 4000
```

Because the OpenAI provider supports an arbitrary `base_url`, the same
backend works against any OpenAI-compatible local server (sglang, vLLM,
ollama, llama.cpp, LM Studio):

```yaml
llm:
  provider: "openai"
  model: "Qwen/Qwen2.5-72B-Instruct"      # whatever your server is serving
  base_url: "http://localhost:30000/v1"   # sglang default; vLLM uses :8000/v1
  api_key: "EMPTY"
```

Or set `OPENAI_BASE_URL` + `OPENAI_API_KEY` env vars to redirect every call
without touching configs. Local servers handle prompt caching transparently
(sglang RadixAttention; vLLM prefix cache) — no API surface needed.

### 7. Events YAML resolution

The simulation reads news events from a YAML the orchestrator builds into a
`NewsPool`. Resolution order:

1. `input.events_file` — explicit path, relative to sim_dir or absolute. Legacy.
2. `ac_id` (preferred) → `constituency_data/constituencies/<ac_id>/events.yaml`.
   If `ac_id` is just a 3-digit AC number (e.g. `"095"`), the loader globs
   `constituency_data/constituencies/095_*` and uses the first match.
3. Fallback: `sim_dir / news/events.yaml`.

For new ACs, prefer `ac_id` — this lets a single canonical events YAML
under `constituency_data/` serve all simulations targeting that constituency,
without copying files around.

## Where to read next

- [`AGENT.md`](AGENT.md) — what an agent IS and how it's defined
- [`INFORMATION_SYSTEM.md`](INFORMATION_SYSTEM.md) — how news flows to agents
- [`COST_ANALYSIS.md`](COST_ANALYSIS.md) — wall time + $ per run
- [`CASE_STUDY_WB_2021_AC095.md`](CASE_STUDY_WB_2021_AC095.md) — the WB run
- [`METHODOLOGY.pdf`](METHODOLOGY.pdf) — visual methodology summary
