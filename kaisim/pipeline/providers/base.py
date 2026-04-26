"""Provider — pluggable LLM backend (Anthropic / OpenAI / future others).

Both implementations expose the same `generate(...)` interface; the LLMBatch
sampler holds a Provider instance and doesn't care which backend it is. The
choice + model live in `persona_config.yaml` under the `llm:` block.

Reasoning levels are normalized to {None, "low", "medium", "high"}; each
provider maps these to its own knobs:
    Anthropic   thinking budget tokens  (None / 2k / 5k / 12k)
    OpenAI      reasoning_effort        (None=minimal / low / medium / high)

Caching:
    Anthropic   `cache_control: ephemeral` on the system block (5min TTL)
    OpenAI      automatic prefix caching when prompt ≥ 1024 tokens

Both implementations also surface usage tokens for cost tracking.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class ProviderResponse:
    text: str                           # main assistant text (no thinking blocks)
    thinking: str | None = None         # extended-thinking content if available
    usage: dict[str, int] = field(default_factory=dict)
    """Keys typically include: input_tokens, output_tokens,
    cache_creation_input_tokens, cache_read_input_tokens, reasoning_tokens."""
    raw: object | None = None           # provider-native response object (debug only)


class Provider(Protocol):
    name: str

    def generate(
        self,
        system: str,
        user: str,
        *,
        max_tokens: int = 16000,
        temperature: float = 0.7,
        reasoning: str | None = None,        # None | "low" | "medium" | "high"
        cache_system: bool = True,
    ) -> ProviderResponse:
        ...
