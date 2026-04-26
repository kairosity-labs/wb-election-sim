"""RuleBasedStrategy — score = scope + tag-overlap + intensity, gated by media engagement.

Score formula (all components linearly combined):
    score = scope_weight[event.scope]
          + (tag_overlap_per_match * |agent.tags ∩ event.tags|)
          + (intensity_bonus_value if event.intensity >= intensity_bonus_above else 0)
    if media_engagement_multiplier:
        score *= agent.media_engagement
    if event's valence for agent's prior party is "negative":
        score += loss_aversion_kicker

Cap at top-k per period via cap_per_period; threshold filters low-score noise.
"""
from __future__ import annotations

from ..core.agent import Agent
from ..core.event import NewsEvent
from .base import ScoredEvent


_DEFAULT_WEIGHTS = {
    "scope_national": 1,
    "scope_state": 2,
    "scope_district": 3,
    "scope_AC": 4,
    "tag_overlap_per_match": 2,
    "intensity_bonus_above": 4,
    "intensity_bonus_value": 1,
    "loss_aversion_kicker": 1,
}


class RuleBasedStrategy:
    name = "rule_based"

    def __init__(self, threshold: float = 3.0, cap_per_period: int = 5,
                 weights: dict | None = None,
                 media_engagement_multiplier: bool = True, **kwargs):
        self.threshold = float(threshold)
        self.cap_per_period = int(cap_per_period)
        self.weights = {**_DEFAULT_WEIGHTS, **(weights or {})}
        self.media_engagement_multiplier = bool(media_engagement_multiplier)

    def select(self, agent: Agent, candidate_events: list[NewsEvent],
               period_start_iso: str, period_end_iso: str) -> list[ScoredEvent]:
        scored: list[ScoredEvent] = []
        agent_tags = set(agent.tags)
        prior = agent.initial_party

        for e in candidate_events:
            score = 0.0
            why = []

            # 1. Scope penetration (broadcast component)
            if e.broadcast or e.scope in {"AC", "district"}:
                scope_score = self.weights.get(f"scope_{e.scope}", 0)
                score += scope_score
                why.append(f"scope:{e.scope}+{scope_score}")

            # 2. Tag overlap (targeted component)
            event_tags = set(e.tags or [])
            overlap = len(agent_tags & event_tags)
            if overlap > 0:
                tag_pts = self.weights["tag_overlap_per_match"] * overlap
                score += tag_pts
                why.append(f"tags×{overlap}+{tag_pts}")

            # 3. Intensity bonus
            if e.intensity >= self.weights["intensity_bonus_above"]:
                bonus = self.weights["intensity_bonus_value"]
                score += bonus
                why.append(f"int{e.intensity}+{bonus}")

            # 4. Media engagement multiplier
            if self.media_engagement_multiplier:
                score *= agent.media_engagement
                why.append(f"×media{agent.media_engagement:.2f}")

            # 5. Loss-aversion kicker (negative news for prior party cuts through)
            if prior:
                # Map party to tag (the events use bjp_supporter / tmc_supporter tags)
                prior_tag = {"BJP": "bjp_supporter", "AITC": "tmc_supporter"}.get(prior)
                if prior_tag and e.valence.get(prior_tag) == "negative":
                    score += self.weights["loss_aversion_kicker"]
                    why.append(f"loss_av+{self.weights['loss_aversion_kicker']}")

            if score >= self.threshold:
                scored.append(ScoredEvent(event=e, score=score, why=" ".join(why)))

        # Sort and cap
        scored.sort(key=lambda s: -s.score)
        return scored[:self.cap_per_period]
