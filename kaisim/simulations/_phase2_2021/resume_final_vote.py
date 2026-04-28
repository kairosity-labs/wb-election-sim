"""Run JUST the final-vote phase on a run dir whose orchestrator died after
the 16-tick belief-evolution loop but before/during the final vote query.

Use case: AC 159 hit a Jinja template bug at the final-vote step (now fixed)
after spending ~5 min building per-agent belief streams. Rather than redo the
16 ticks, this loads each agent's persona.json + memory_stream.jsonl from disk,
calls FinalVoteQuery on it, and writes final_vote.json + the run summary.

Usage:
    python kaisim/simulations/_phase2_2021/resume_final_vote.py \
        kaisim/simulations/wb_2021_ac159/runs/<TS>_2021_targeted

The script picks up the run's config.snapshot.yaml so the election_context,
LLM settings, and ground_truth all match what would have run originally.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]            # kaisim/
sys.path.insert(0, str(ROOT))

from pipeline.core.persona import Persona
from pipeline.providers import make_provider
from pipeline.simulation import analytics
from pipeline.simulation.core.agent import Agent
from pipeline.simulation.core.config import SimulationConfig
from pipeline.simulation.core.memory import MemoryStream
from pipeline.simulation.updaters import FinalVoteQuery


def load_agents(run_root: Path) -> list[Agent]:
    """Reconstitute Agent objects from the per-agent run-dir artifacts."""
    agents: list[Agent] = []
    agents_dir = run_root / "agents"
    for agent_dir in sorted(agents_dir.iterdir()):
        if not agent_dir.is_dir():
            continue
        persona_d = json.loads((agent_dir / "persona.json").read_text())
        persona = Persona.from_dict(persona_d)
        mem_path = agent_dir / "memory_stream.jsonl"
        memory = MemoryStream.from_jsonl(mem_path) if mem_path.exists() else MemoryStream()
        ag = Agent(id=persona.id, persona=persona,
                   tags=set(),                # not used by final_vote
                   memory_stream=memory)
        agents.append(ag)
    return agents


async def run_resume(run_root: Path, max_concurrent: int = 100):
    cfg_path = run_root / "config.snapshot.yaml"
    raw_cfg = yaml.safe_load(cfg_path.read_text())
    sim_dir = run_root.parent.parent              # …/wb_2021_ac<NN>
    cfg = SimulationConfig(raw=raw_cfg, sim_dir=sim_dir,
                           name=raw_cfg.get("simulation", {}).get("name", "resumed"))

    # Provider — same plumbing as Orchestrator.__init__
    provider_kwargs = {}
    for k in ("base_url", "api_key"):
        v = cfg.get(f"llm.{k}")
        if v:
            provider_kwargs[k] = v
    provider = make_provider(cfg.get("llm.provider", "anthropic"),
                             model=cfg.get("llm.model"), **provider_kwargs)

    # Bump the default thread pool (same fix as Orchestrator.__init__)
    asyncio.get_running_loop().set_default_executor(
        ThreadPoolExecutor(max_workers=max(max_concurrent + 32, 256),
                           thread_name_prefix="resume_llm")
    )

    final_query = FinalVoteQuery(
        provider,
        reasoning="medium",
        temperature=float(cfg.get("llm.temperature", 0.7)),
        # Qwen 3.5 9B emits ~1500-2000 tokens of <think>...</think> before
        # the JSON answer. sglang's --reasoning-parser strips it from
        # message.content but it still counts toward max_tokens. 2000 was
        # too tight (truncated 91% of responses mid-JSON); 8000 is safe.
        max_tokens=int(cfg.get("llm.final_vote_max_tokens", 8000)),
        cache_system_prompt=bool(cfg.get("llm.cache_system_prompt", True)),
        election_context=cfg.get("election_context", {}),
    )

    sem = asyncio.Semaphore(max_concurrent)
    all_agents = load_agents(run_root)

    # Skip agents that already have a valid final_vote.json (from a prior
    # successful pass). Re-run only the failures.
    todo = [ag for ag in all_agents
            if not (run_root / "agents" / ag.id / "final_vote.json").exists()]
    print(f"Loaded {len(all_agents)} agents from {run_root}; "
          f"{len(all_agents) - len(todo)} already have final_vote, "
          f"{len(todo)} to do")
    print(f"election_context: {cfg.get('election_context', {}).get('ac_name')} on "
          f"{cfg.get('election_context', {}).get('poll_date_human')}")

    fail_dump_dir = run_root / "_resume_failures"
    fail_dump_dir.mkdir(exist_ok=True)

    async def one(ag: Agent):
        async with sem:
            res = await final_query.ask(ag, cfg.end_date)
        agent_dir = run_root / "agents" / ag.id
        if res:
            (agent_dir / "final_vote.json").write_text(json.dumps(res, indent=2))
        else:
            # Save a marker so we can investigate persistent failures later.
            (fail_dump_dir / f"{ag.id}.failed").write_text("returned None")
        return res

    results = await asyncio.gather(*[one(a) for a in todo])

    # Run analytics — vote distribution, plots, ignore-rate by demo
    print("\n=== Analytics ===")
    gt = cfg.get("ground_truth")
    summary = analytics.run_all(run_root, ground_truth=gt)

    # Persist summary.json (orchestrator usually does this)
    summary_path = run_root / "summary.json"
    summary_doc = {
        "n_agents": len(agents),
        "resumed_final_vote": True,
        "vote_distribution": summary["vote_distribution"],
    }
    summary_path.write_text(json.dumps(summary_doc, indent=2))
    print(f"Final vote distribution: {summary['vote_distribution'].get('pcts')}")
    print(f"Wrote {summary_path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir", type=Path,
                    help="Path to runs/<TS>_<config>/ to resume")
    ap.add_argument("--max-concurrent", type=int, default=100)
    args = ap.parse_args()
    asyncio.run(run_resume(args.run_dir, max_concurrent=args.max_concurrent))


if __name__ == "__main__":
    main()
