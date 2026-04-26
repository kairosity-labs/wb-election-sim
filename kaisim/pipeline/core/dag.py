"""DAG — derive a generation order over axes from declared parent relationships.

Sources of parent relations:
    1. Joints with `semantics in {conditional, flag_rate_conditional,
       two_indicator_rates}` declare `parents → child`.
    2. Derived axes declare their `parents` directly in axes.json.
    3. The sampling spec may declare additional ordering constraints
       (e.g., "occupation depends on workforce_status").

The DAG is used by `RuleBasedSampler` to walk axes in topological order,
ensuring every parent value is available before a child is sampled. The vote
field is generated outside the DAG (post-walk) by VoteBlender.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Iterable

from .axis import Axis
from .joint import Joint


class DAG:
    def __init__(
        self,
        axes: list[Axis],
        joints: list[Joint],
        extra_edges: dict[str, list[str]] | None = None,
    ):
        self.axes_by_name = {a.name: a for a in axes if a.is_sampleable()}
        self.parents: dict[str, set[str]] = defaultdict(set)

        # Edges from derived-axis parent declarations.
        for a in axes:
            if a.kind == "derived" and a.parents:
                self.parents[a.name].update(a.parents)

        # Edges from joints (only sampling joints, not verifier-only).
        for j in joints:
            if not j.is_for_sampling():
                continue
            if j.semantics in {
                "conditional",
                "flag_rate_conditional",
                "two_indicator_rates",
            }:
                # Parent axes must be sampled before child.
                if j.child in self.axes_by_name:
                    self.parents[j.child].update(j.parents)

        # Caller-supplied extras (e.g., from sampling_spec ordering hints).
        if extra_edges:
            for child, ps in extra_edges.items():
                self.parents[child].update(ps)

        # Filter to only existing sampleable axes (drop derived parent
        # references like "asset_media_tier_derived" that are intermediates).
        for child in list(self.parents):
            self.parents[child] = {
                p for p in self.parents[child] if p in self.axes_by_name
            }

        self.topo_order = self._topo_sort()

    def _topo_sort(self) -> list[str]:
        order: list[str] = []
        visited: set[str] = set()
        temp: set[str] = set()

        def visit(node: str):
            if node in visited:
                return
            if node in temp:
                raise ValueError(f"Cycle in DAG involving {node!r}")
            temp.add(node)
            for parent in sorted(self.parents.get(node, set())):
                if parent in self.axes_by_name:
                    visit(parent)
            temp.discard(node)
            visited.add(node)
            order.append(node)

        for name in sorted(self.axes_by_name):
            visit(name)
        return order

    def parents_of(self, axis_name: str) -> list[str]:
        return sorted(self.parents.get(axis_name, set()))

    def __repr__(self) -> str:
        lines = ["DAG topological order:"]
        for name in self.topo_order:
            ps = self.parents_of(name)
            arrow = f"  ← {ps}" if ps else "  (root)"
            lines.append(f"  {name:25s}{arrow}")
        return "\n".join(lines)
