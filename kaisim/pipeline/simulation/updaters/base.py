"""Common helpers for LLM-based updaters: prompt rendering + JSON parsing."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


_FRAMEWORK_DIR = Path(__file__).resolve().parents[1]
PROMPTS_DIR = _FRAMEWORK_DIR / "prompts"


def render_template(template_name: str, **context) -> str:
    """Lightweight Jinja2 render. Templates live in pipeline/simulation/prompts/."""
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
    env = Environment(
        loader=FileSystemLoader(str(PROMPTS_DIR)),
        undefined=StrictUndefined,
        trim_blocks=False,
        lstrip_blocks=False,
        keep_trailing_newline=True,
    )
    tpl = env.get_template(template_name)
    return tpl.render(**context)


_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL)


def parse_llm_json(text: str) -> dict | None:
    """Extract a JSON object from an LLM response, tolerating fences/prose."""
    candidates: list[str] = []
    for m in _FENCE_RE.finditer(text):
        candidates.append(m.group(1))
    candidates.append(text.strip())
    s = text.strip()
    first = s.find("{")
    if first != -1:
        candidates.append(s[first:])

    for blob in candidates:
        try:
            data = json.loads(blob)
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            continue
    # Last resort: find longest balanced { ... } via brace walk
    if first != -1:
        depth = 0
        end = -1
        for i in range(first, len(s)):
            if s[i] == "{":
                depth += 1
            elif s[i] == "}":
                depth -= 1
                if depth == 0:
                    end = i
                    break
        if end > 0:
            try:
                return json.loads(s[first:end + 1])
            except json.JSONDecodeError:
                pass
    return None
