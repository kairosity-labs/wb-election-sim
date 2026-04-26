"""Targeting strategy registry."""
from .base import ScoredEvent, TargetingStrategy
from .show_all import ShowAllStrategy
from .rule_based import RuleBasedStrategy


_REGISTRY = {
    "show_all": ShowAllStrategy,
    "rule_based": RuleBasedStrategy,
}


def make_targeting(name: str, config: dict | None = None) -> TargetingStrategy:
    if name not in _REGISTRY:
        raise ValueError(f"Unknown targeting strategy {name!r}. Known: {sorted(_REGISTRY)}")
    cls = _REGISTRY[name]
    return cls(**(config or {}))


__all__ = ["ScoredEvent", "TargetingStrategy", "make_targeting"]
