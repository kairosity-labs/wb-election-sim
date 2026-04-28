"""Orchestrator — async event-driven simulation loop.

Per period (week/month/quarter):
    1. Query NewsPool for events active in this period.
    2. For each agent (asyncio.gather):
        a. Targeting strategy selects which events reach this agent.
        b. For each selected event: LLM-update (sequential within agent;
           memory state from event N feeds into event N+1).
        c. If reflection trigger fires: compress older raw memories.
    3. After last period: parallel final_vote_query for all agents.

Parallelism is bounded by `max_concurrent_personas` (default 10) to respect
LLM API rate limits.

Each agent's outputs are flushed to disk INCREMENTALLY after each LLM call,
so a mid-run crash preserves all completed work.
"""
from __future__ import annotations

import asyncio
import json
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

from ..providers import make_provider
from ..core.persona_set import PersonaSet
from .core.agent import Agent
from .core.clock import Period, Ticker
from .core.config import SimulationConfig
from .core.event import NewsEvent, NewsPool
from .core.memory import MemoryItem
from .targeting import ScoredEvent, make_targeting
from .updaters import FinalVoteQuery, ParkMinimalUpdater, ReflectionUpdater, make_updater


@dataclass
class FeedRecord:
    period: str
    event_slug: str
    score: float
    why: str
    accepted: bool       # whether the LLM call yielded a memory item
    engagement: str = "" # what the LLM said
    reaction: str = ""


@dataclass
class AgentRunState:
    agent: Agent
    feed_log: list[FeedRecord] = field(default_factory=list)
    final_vote: dict | None = None
    n_llm_calls: int = 0
    agent_dir: Path | None = None        # populated at init for incremental flush

    def append_memory_to_disk(self, item: MemoryItem) -> None:
        """Atomically append one memory item to memory_stream.jsonl."""
        if not self.agent_dir:
            return
        with (self.agent_dir / "memory_stream.jsonl").open("a") as f:
            f.write(json.dumps(item.to_dict()) + "\n")
        if item.structured_delta:
            with (self.agent_dir / "structured_history.jsonl").open("a") as f:
                f.write(json.dumps({
                    "timestamp": item.timestamp,
                    "triggering_event_slug": item.triggering_event_slug,
                    "delta": item.structured_delta,
                }) + "\n")

    def append_feed_to_disk(self, fr: FeedRecord) -> None:
        if not self.agent_dir:
            return
        with (self.agent_dir / "feeds.jsonl").open("a") as f:
            f.write(json.dumps(asdict(fr)) + "\n")

    def write_final_vote(self) -> None:
        if not self.agent_dir or not self.final_vote:
            return
        (self.agent_dir / "final_vote.json").write_text(
            json.dumps(self.final_vote, indent=2)
        )


class Orchestrator:
    def __init__(self, config: SimulationConfig,
                 ctx_axes_load_fn=None,
                 derive_tags_fn=None,
                 derive_media_engagement_fn=None,
                 verbose: bool = True):
        self.config = config
        self.verbose = verbose

        # Provider — supports OpenAI-compatible local backends
        # (sglang / vLLM / ollama / llama.cpp / LM Studio) via base_url.
        provider_name = config.get("llm.provider", "anthropic")
        model = config.get("llm.model")
        provider_kwargs = {}
        for key in ("base_url", "api_key"):
            v = config.get(f"llm.{key}")
            if v:
                provider_kwargs[key] = v
        self.provider = make_provider(provider_name, model=model,
                                       **provider_kwargs)
        self.llm_kwargs = {
            "reasoning": config.get("llm.reasoning", "low"),
            "temperature": float(config.get("llm.temperature", 0.7)),
            "max_tokens": int(config.get("llm.max_tokens", 4000)),
            "cache_system_prompt": bool(config.get("llm.cache_system_prompt", True)),
        }

        # Updaters
        self.update_fn = make_updater(
            config.get("update.style", "park_minimal"),
            self.provider, **self.llm_kwargs,
        )
        self.reflector = ReflectionUpdater(
            self.provider, **{**self.llm_kwargs, "max_tokens": 1500}
        )
        self.final_query = FinalVoteQuery(
            self.provider, **{**self.llm_kwargs,
                              "max_tokens": 2000,
                              "reasoning": "medium"}
        )

        # Ticker
        self.ticker = Ticker(
            start=config.start_date,
            end=config.end_date,
            tick_unit=config.tick_unit,
            tick_size=config.tick_size,
            reflection_every_n_ticks=config.reflection_every_n_ticks,
        )

        # Targeting
        self.targeting = make_targeting(
            config.get("targeting.strategy", "rule_based"),
            config.get("targeting.config", {}) or {},
        )

        # Region-specific functions
        self.derive_tags_fn = derive_tags_fn or (lambda p: set())
        self.derive_media_engagement_fn = (
            derive_media_engagement_fn or (lambda p: 1.0)
        )

        # Concurrency
        self.semaphore = asyncio.Semaphore(
            int(config.get("execution.max_concurrent_personas", 10))
        )

        self.usage_total: dict[str, int] = {}

    # ----- agent init -----
    def init_agents(self, persona_set: PersonaSet,
                    out_root: Path | None = None) -> list[AgentRunState]:
        agents: list[AgentRunState] = []
        for p in persona_set.personas:
            tags = self.derive_tags_fn(p)
            media = self.derive_media_engagement_fn(p)
            ag = Agent(id=p.id, persona=p, tags=set(tags), media_engagement=float(media))
            state = AgentRunState(agent=ag)
            # Scaffold per-agent dir for incremental flush on each LLM call.
            if out_root is not None:
                agent_dir = Path(out_root) / "agents" / ag.id
                agent_dir.mkdir(parents=True, exist_ok=True)
                state.agent_dir = agent_dir
                # Snapshot persona once.
                (agent_dir / "persona.json").write_text(
                    json.dumps(ag.persona.to_dict(), indent=2)
                )
                # Truncate any pre-existing append-only files.
                for fname in ("memory_stream.jsonl", "feeds.jsonl",
                              "structured_history.jsonl"):
                    (agent_dir / fname).write_text("")
            agents.append(state)
        return agents

    # ----- main loop -----
    async def run(self, persona_set: PersonaSet, news_pool: NewsPool,
                  out_root: Path) -> dict:
        out_root = Path(out_root)
        (out_root / "agents").mkdir(parents=True, exist_ok=True)

        states = self.init_agents(persona_set, out_root)
        if self.verbose:
            print(f"Initialized {len(states)} agents.")
            print(f"Ticker: {self.config.tick_unit} ticks "
                  f"from {self.config.start_date} to {self.config.end_date} "
                  f"({self.ticker.total_periods()} periods)")
            print(f"Targeting: {self.targeting.name}")
            print()

        for period in self.ticker.periods():
            events_in_period = news_pool.first_appearances_in(period.start, period.end)
            if self.verbose:
                print(f"=== {period.label} ({len(events_in_period)} candidate events) ===")

            await asyncio.gather(*[
                self._process_agent_period(state, period, events_in_period)
                for state in states
            ])

            if self.ticker.should_reflect(period):
                if self.verbose:
                    print(f"  reflection trigger: compressing older memories")
                await asyncio.gather(*[
                    self._reflect_agent(state, period)
                    for state in states
                ])

        # Final vote query
        if self.verbose:
            print("\n=== Final vote query ===")
        await asyncio.gather(*[
            self._final_vote(state) for state in states
        ])

        # Final pass: regenerate derived artifacts (belief_narrative.md +
        # agent_meta.json) from the in-memory + incrementally-flushed state.
        for state in states:
            agent_dir = state.agent_dir or (out_root / "agents" / state.agent.id)
            agent_dir.mkdir(parents=True, exist_ok=True)
            narrative_lines = []
            for m in state.agent.memory_stream.items:
                narrative_lines.append(
                    f"## [{m.timestamp}] ({m.kind}, importance {m.importance})\n"
                )
                narrative_lines.append(m.content + "\n\n")
            (agent_dir / "belief_narrative.md").write_text("".join(narrative_lines))
            (agent_dir / "agent_meta.json").write_text(json.dumps({
                "id": state.agent.id,
                "tags": sorted(state.agent.tags),
                "media_engagement": state.agent.media_engagement,
                "initial_party": state.agent.initial_party,
                "n_memories": len(state.agent.memory_stream),
                "n_reactions": len(state.agent.memory_stream.raw_reactions()),
                "n_reflections": len(state.agent.memory_stream.reflections()),
                "n_llm_calls": state.n_llm_calls,
            }, indent=2))

        # Aggregate
        summary = {
            "n_agents": len(states),
            "n_periods": self.ticker.total_periods(),
            "total_llm_calls": sum(s.n_llm_calls for s in states),
            "vote_distribution": self._vote_distribution(states),
            "ignore_rate": self._ignore_rate(states),
            "usage_total": self.usage_total,
        }
        (out_root / "summary.json").write_text(json.dumps(summary, indent=2))
        return summary

    # ----- per-agent processing -----
    async def _process_agent_period(self, state: AgentRunState, period: Period,
                                     events: list[NewsEvent]) -> None:
        async with self.semaphore:
            scored = self.targeting.select(
                state.agent, events,
                period.start.isoformat(), period.end.isoformat(),
            )
            for se in scored:
                memory_id = f"{state.agent.id}_m{len(state.agent.memory_stream):03d}"
                item, parsed, raw = await self.update_fn.update(
                    state.agent, se.event, period.end, memory_id,
                )
                state.n_llm_calls += 1
                fr = FeedRecord(
                    period=period.label,
                    event_slug=se.event.slug,
                    score=se.score,
                    why=se.why,
                    accepted=item is not None,
                    engagement=parsed.get("engagement", "") if parsed else "",
                    reaction=parsed.get("reaction", "") if parsed else "",
                )
                state.feed_log.append(fr)
                state.append_feed_to_disk(fr)               # incremental flush
                if item:
                    state.agent.memory_stream.add(item)
                    state.append_memory_to_disk(item)       # incremental flush
                if self.verbose:
                    flag = "✓" if item else "·"
                    print(f"  {flag} {state.agent.id} ← {se.event.slug} "
                          f"(score {se.score:.1f}, {parsed.get('engagement','?') if parsed else 'parse_fail'})")

    async def _reflect_agent(self, state: AgentRunState, period: Period) -> None:
        async with self.semaphore:
            window_end = period.end.isoformat()
            raws = state.agent.memory_stream.raw_reactions()
            if not raws:
                return
            window_start = raws[0].timestamp
            memory_id = f"{state.agent.id}_r{len(state.agent.memory_stream.reflections()):02d}"
            reflection = await self.reflector.reflect(
                state.agent, window_start, window_end, memory_id,
            )
            state.n_llm_calls += 1
            # Reflection rewrote the in-memory stream; also rewrite the file
            # so it stays consistent with what the agent will see next tick.
            if reflection and state.agent_dir:
                state.agent.memory_stream.to_jsonl(
                    state.agent_dir / "memory_stream.jsonl"
                )

    async def _final_vote(self, state: AgentRunState) -> None:
        async with self.semaphore:
            res = await self.final_query.ask(state.agent, self.config.end_date)
            state.n_llm_calls += 1
            state.final_vote = res
            state.write_final_vote()           # incremental flush

    # ----- aggregates -----
    def _vote_distribution(self, states: list[AgentRunState]) -> dict[str, int]:
        from collections import Counter
        votes = [s.final_vote.get("vote") for s in states if s.final_vote]
        return dict(Counter(votes))

    def _ignore_rate(self, states: list[AgentRunState]) -> dict[str, Any]:
        total = sum(len(s.feed_log) for s in states)
        accepted = sum(1 for s in states for f in s.feed_log if f.accepted)
        return {
            "events_delivered_total": total,
            "events_accepted_total": accepted,
            "ignore_rate": round(1 - (accepted / total if total else 0.0), 3),
        }
