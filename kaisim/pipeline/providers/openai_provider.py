"""OpenAI provider — GPT (incl. reasoning models) with auto prompt caching.

Uses the chat-completions API. For reasoning models (o-series, gpt-5*),
sets `reasoning_effort`; for non-reasoning models, the parameter is ignored.

Prompt caching is automatic on the OpenAI side when the prompt prefix is
≥ 1024 tokens AND identical across calls. The system prompt (which is the
big static part for the persona pipeline) qualifies easily.
"""
from __future__ import annotations

import os

from openai import OpenAI

from .base import ProviderResponse


_EFFORT_MAP = {
    "low":    "low",
    "medium": "medium",
    "high":   "high",
}


def _is_reasoning_model(model: str) -> bool:
    m = model.lower()
    return m.startswith(("o1", "o3", "o4")) or "gpt-5" in m


class OpenAIProvider:
    name = "openai"

    def __init__(self, model: str = "gpt-5-mini", api_key: str | None = None):
        self.model = model
        self.client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))

    def generate(
        self,
        system: str,
        user: str,
        *,
        max_tokens: int = 16000,
        temperature: float = 0.7,
        reasoning: str | None = None,
        cache_system: bool = True,           # automatic on OpenAI; flag is a no-op
    ) -> ProviderResponse:
        kwargs = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "max_completion_tokens": max_tokens,
        }

        if _is_reasoning_model(self.model):
            if reasoning in _EFFORT_MAP:
                kwargs["reasoning_effort"] = _EFFORT_MAP[reasoning]
            # Reasoning models do not support custom temperature.
        else:
            kwargs["temperature"] = temperature

        resp = self.client.chat.completions.create(**kwargs)

        text = resp.choices[0].message.content or ""
        usage_obj = resp.usage
        usage = {
            "input_tokens": getattr(usage_obj, "prompt_tokens", 0),
            "output_tokens": getattr(usage_obj, "completion_tokens", 0),
            "reasoning_tokens": getattr(
                getattr(usage_obj, "completion_tokens_details", None),
                "reasoning_tokens", 0
            ) or 0,
            "cached_input_tokens": getattr(
                getattr(usage_obj, "prompt_tokens_details", None),
                "cached_tokens", 0
            ) or 0,
        }
        return ProviderResponse(
            text=text,
            thinking=None,                # not exposed via Chat Completions
            usage=usage,
            raw=resp,
        )
