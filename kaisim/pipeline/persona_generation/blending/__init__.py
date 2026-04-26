"""Blending registry — name → factory."""
from .log_odds_mean import LogOddsMean
from .naive_bayes import NaiveBayes
from . import welfare_overlap


VOTE_BLENDER_FACTORY = {
    "log_odds_mean": LogOddsMean,
    "naive_bayes": NaiveBayes,
}


def make_vote_blender(method: str):
    if method not in VOTE_BLENDER_FACTORY:
        raise ValueError(
            f"Unknown vote blending method {method!r}. "
            f"Known: {sorted(VOTE_BLENDER_FACTORY)}"
        )
    return VOTE_BLENDER_FACTORY[method]()


def make_welfare_overlap(method: str, precedence: list[str] | None = None):
    return welfare_overlap.make(method, precedence)
