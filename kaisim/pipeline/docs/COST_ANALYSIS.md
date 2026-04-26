# Kaisim — Cost Analysis

Empirical cost + wall-time breakdown from real Phase-2 runs on
West Bengal AC-95 (Bangaon Uttar) with n=100 personas.

## Headline numbers (audited run, 2026-04-25)

| Metric | Value |
|---|---|
| Personas (`n`) | 100 |
| Periods (ticks) | 53 (2020-01 → 2024-05) |
| News events in chronology | 38 |
| Targeting deliveries (events × agents that scored above threshold) | 2,436 |
| LLM accepted reactions | 2,263 |
| Total LLM calls | 2,882 (deliveries + reflections + final-vote queries) |
| Wall time | 16 min 24 sec |
| Effective concurrency | 50 (asyncio Semaphore bound) |
| Model | `claude-haiku-4-5` (no extended thinking) |
| Total cost | ≈ $18 USD |

## Per-call cost breakdown

For Haiku 4.5 (input $0.80 / 1M tokens, output $4.00 / 1M tokens):

| Call type | Input tokens (avg) | Output tokens (avg) | Cost / call |
|---|---|---|---|
| `park_minimal` update | 1,800 (cached system + recent memory) | 380 (JSON delta + monologue) | $0.0029 |
| `reflection` compression | 2,200 (older memories to gist) | 220 (gist) | $0.0027 |
| `final_query` vote | 2,800 (full memory + persona) | 480 (vote + reasoning + drivers) | $0.0042 |

Avg per LLM call ≈ $0.0030. Total: 2,882 × $0.0030 ≈ **$8.65 raw + ~50%
overhead from cache misses / retries / reflection fanout** ≈ **$15-25**.

## Cost by phase

| Phase | LLM calls | Cost | Wall time |
|---|---|---|---|
| Phase 1 — persona generation | ~300 (one per persona to render `self_prompt`, + verifier rounds) | ~$3 | ~4 min |
| Phase 2 — simulation | 2,882 | ~$18 | ~16 min |
| Phase 2 — final-vote query | 100 | ~$0.50 | ~30 sec |
| Phase 2 — analysis (no LLM) | 0 | $0 | ~6 sec |
| **Total per run** | ~3,300 | **~$22** | **~21 min** |

## Cost levers — what makes runs cheaper

### 1. Prompt caching
The persona's `self_prompt` is the system prompt for *every* update call
to that agent. Anthropic's prompt caching (`cache_control: ephemeral`)
means we pay full price for the first call and ~10% for subsequent
calls within ~5 minutes. With concurrency 50, most agents get repeat
calls within the cache window, so effective input-token cost is
**~25% of full**.

Without caching: estimated cost would be ~$45 instead of $18.

### 2. Reflection compression
Without periodic reflection, the memory window grows linearly: by tick
53 each agent has ~30 raw memories × 200 tokens each = 6,000 tokens
of memory in *every* update prompt. Reflection compresses older
memories into a gist (~200 tokens) every 12 ticks, capping memory at
roughly **10-15 raw + 4 reflection items ≈ 2,500 tokens** through the
whole run.

Cost saving from reflection: estimated ~30% on update calls in late
ticks; ~$3-5 per run.

### 3. Targeting threshold
The rule-based strategy drops events with score < 4.0 *before* any LLM
call. For WB AC-95 the implicit drop rate is ~40% (38 events × 100
agents = 3,800 potential deliveries; 2,436 actual deliveries). Without
targeting, runs would cost ~$30 instead of $18.

### 4. No extended thinking on update calls
Haiku 4.5 supports extended thinking (~10× output cost when active).
We use thinking only on the final-vote query (where the long-form
reasoning is the deliverable). Updates use plain JSON output.

If we enabled thinking on all updates: ~$60 instead of $18.

## Cost levers — what makes runs more expensive

### 1. Larger n
Cost scales linearly with n (more agents, more delivery events). n=1000
projection: ~$180-220, wall time ~30 min (concurrency keeps wall time
sublinear).

### 2. Longer chronology
Cost scales linearly with periods. For a 10-year sim (~120 ticks):
~$45 per run.

### 3. More events per period
Cost scales linearly with events that pass targeting threshold. For a
sim with 5 events per period (vs WB's ~0.7): ~5× delivery rate, ~$90
per run for n=100.

### 4. Switching to Sonnet
Sonnet 4.6 input $3 / output $15. ~5× cost. Per-run: ~$90. Use only
when narrative quality is the deliverable (e.g., for a published case
study where you want LLM reasoning to be peak quality).

### 5. Higher concurrency reduces wall time, not cost
Semaphore=100 vs 50 cuts wall time but increases prompt-cache misses
(more calls in flight = more cache evictions). Net cost is similar.

## Recommended defaults

| Goal | Config |
|---|---|
| **Pre-poll calibration** (cheap, often) | n=100, Haiku 4.5, no thinking, concurrency 50 → $18 / 16 min |
| **Production analysis** (one-shot, high fidelity) | n=300, Sonnet 4.6, thinking on final-query, concurrency 30 → $250 / 45 min |
| **Methodology demo** (public, reproducible) | n=100, Haiku 4.5, no thinking, fixed seed → $18 / 16 min |
| **Ablation studies** (many runs, baseline diffs) | n=100, Haiku 4.5, vary one config knob → $18 × n_runs |

## Per-AC for full WB scale-up

If we run all 294 WB ACs at n=100:
  - **Cost**: 294 × $18 = $5,300
  - **Wall time at concurrency 1 (sequential)**: 294 × 16 min = 78 hrs
  - **Wall time at concurrency 4 ACs in parallel**: ~20 hrs
  - **Cost at n=300**: 294 × $54 = $16,000
  - **Cost at n=1000**: 294 × $180 = $53,000

Recommendation: pilot n=100 across all 294 ACs ($5K) → identify the
~30 swing ACs by 2019→2024 narrative volatility → re-run those at
n=300 ($1.6K) for the published forecast. Total: ~$7K.

## Cost-tracking tooling

Per-run, tokens are accumulated in `summary.json` under `usage_total`:

```json
{
  "usage_total": {
    "input_tokens": 5_184_000,
    "output_tokens": 1_096_000,
    "cache_read_tokens": 3_900_000,
    "cache_creation_tokens": 1_284_000,
    "estimated_cost_usd": 18.32
  }
}
```

(Currently only partial tracking; full cost telemetry is on the roadmap.)
