"""OpenAI provider — GPT (incl. reasoning models) with auto prompt caching.

Uses the chat-completions API. For reasoning models (o-series, gpt-5*),
sets `reasoning_effort`; for non-reasoning models, the parameter is ignored.

Prompt caching is automatic on the OpenAI side when the prompt prefix is
≥ 1024 tokens AND identical across calls. The system prompt (which is the
big static part for the persona pipeline) qualifies easily.

OpenAI-compatible local backends (sglang, vLLM, llama.cpp, ollama, LM Studio):
pass `base_url` to point at the local server's `/v1` endpoint and `api_key`
can be any non-empty string ('EMPTY' is the convention). Reasoning-effort
won't be sent for non-OpenAI-reasoning model names. Local servers handle
prompt caching transparently (sglang RadixAttention, vLLM prefix cache).

YAML config example for sglang:
    llm:
      provider: "openai"
      model: "Qwen/Qwen2.5-72B-Instruct"
      base_url: "http://localhost:30000/v1"
      api_key: "EMPTY"
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

    def __init__(
        self,
        model: str = "gpt-5-mini",
        api_key: str | None = None,
        base_url: str | None = None,
    ):
        """OpenAI / OpenAI-compatible provider.

        api_key:  resolved from arg → OPENAI_API_KEY env → 'EMPTY'.
                  Local servers (sglang/vLLM) accept anything.
        base_url: when set, points the client at a local OpenAI-compatible
                  server. Falls back to the OpenAI SDK default (api.openai.com).
        """
        self.model = model
        self.base_url = base_url or os.environ.get("OPENAI_BASE_URL")
        client_kwargs = {
            "api_key": api_key or os.environ.get("OPENAI_API_KEY") or "EMPTY",
        }
        if self.base_url:
            client_kwargs["base_url"] = self.base_url
        self.client = OpenAI(**client_kwargs)

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
