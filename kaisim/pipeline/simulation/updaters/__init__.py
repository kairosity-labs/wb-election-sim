from .park_minimal import ParkMinimalUpdater
from .reflection import ReflectionUpdater
from .final_query import FinalVoteQuery
from .vote_intention_probe import VoteIntentionProbe


_UPDATER_REGISTRY = {
    "park_minimal": ParkMinimalUpdater,
}


def make_updater(style: str, provider, **kwargs):
    if style not in _UPDATER_REGISTRY:
        raise ValueError(f"Unknown updater style {style!r}. Known: {sorted(_UPDATER_REGISTRY)}")
    return _UPDATER_REGISTRY[style](provider, **kwargs)


__all__ = ["ParkMinimalUpdater", "ReflectionUpdater", "FinalVoteQuery",
           "VoteIntentionProbe", "make_updater"]
