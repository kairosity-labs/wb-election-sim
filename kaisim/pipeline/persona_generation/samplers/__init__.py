from .rule_based import RuleBasedSampler
from .llm_batch import LLMBatchSampler

SAMPLER_FACTORY = {
    "rule_based": RuleBasedSampler,
    "llm_batch": LLMBatchSampler,
}


def make_sampler(name: str):
    if name not in SAMPLER_FACTORY:
        raise ValueError(f"Unknown sampler {name!r}. Known: {sorted(SAMPLER_FACTORY)}")
    return SAMPLER_FACTORY[name]
