"""Provider factory — name → instance."""
from __future__ import annotations

from .base import Provider, ProviderResponse


def make_provider(name: str, model: str | None = None, **kwargs) -> Provider:
    name = name.lower()
    if name == "anthropic":
        from .anthropic_provider import AnthropicProvider
        return AnthropicProvider(model=model or "claude-sonnet-4-6", **kwargs)
    if name == "openai":
        from .openai_provider import OpenAIProvider
        return OpenAIProvider(model=model or "gpt-5-mini", **kwargs)
    raise ValueError(f"Unknown provider {name!r}. Known: anthropic, openai")


__all__ = ["Provider", "ProviderResponse", "make_provider"]
