"""Anthropic provider — Claude with extended thinking + ephemeral caching."""
from __future__ import annotations

import os

from anthropic import Anthropic

from .base import ProviderResponse


_THINKING_BUDGET = {
    "low":    2000,
    "medium": 5000,
    "high":   12000,
}


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, model: str = "claude-sonnet-4-6", api_key: str | None = None):
        self.model = model
        self.client = Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))

    def generate(
        self,
        system: str,
        user: str,
        *,
        max_tokens: int = 16000,
        temperature: float = 0.7,
        reasoning: str | None = None,
        cache_system: bool = True,
    ) -> ProviderResponse:
        system_block = [{"type": "text", "text": system}]
        if cache_system:
            system_block[0]["cache_control"] = {"type": "ephemeral"}

        kwargs = {
            "model": self.model,
            "max_tokens": max_tokens,
            "system": system_block,
            "messages": [{"role": "user", "content": user}],
        }
        if reasoning in _THINKING_BUDGET:
            # Extended thinking: temperature must be 1.0; max_tokens must
            # accommodate the budget. We bump max_tokens if needed.
            budget = _THINKING_BUDGET[reasoning]
            kwargs["thinking"] = {"type": "enabled", "budget_tokens": budget}
            kwargs["temperature"] = 1.0
            if max_tokens < budget + 4000:
                kwargs["max_tokens"] = budget + 4000
        else:
            kwargs["temperature"] = temperature

        resp = self.client.messages.create(**kwargs)

        text_parts, thinking_parts = [], []
        for block in resp.content:
            t = getattr(block, "type", None)
            if t == "text":
                text_parts.append(block.text)
            elif t == "thinking":
                thinking_parts.append(getattr(block, "thinking", "") or "")

        usage = {
            "input_tokens": getattr(resp.usage, "input_tokens", 0),
            "output_tokens": getattr(resp.usage, "output_tokens", 0),
            "cache_creation_input_tokens": getattr(resp.usage, "cache_creation_input_tokens", 0) or 0,
            "cache_read_input_tokens": getattr(resp.usage, "cache_read_input_tokens", 0) or 0,
        }
        return ProviderResponse(
            text="".join(text_parts),
            thinking="\n".join(thinking_parts) if thinking_parts else None,
            usage=usage,
            raw=resp,
        )
