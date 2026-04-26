"""Ticker — advances simulation time in configurable units.

The Ticker yields successive (period_start, period_end) tuples covering
the simulation window. The orchestrator processes each period in turn:
queries the news pool for events active in the period, hands them to
each agent's targeting strategy, and dispatches LLM updates.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Iterator


@dataclass
class Period:
    start: date
    end: date
    index: int                  # 0-based period number from sim start

    @property
    def label(self) -> str:
        # Friendly label for logs/filenames
        if self.start.year == self.end.year and self.start.month == self.end.month:
            return self.start.strftime("%Y-%m")
        return f"{self.start.isoformat()}_to_{self.end.isoformat()}"


def _add_months(d: date, n: int) -> date:
    """Add n months to date `d`, clamping to month-end."""
    m = d.month + n
    y = d.year + (m - 1) // 12
    m = ((m - 1) % 12) + 1
    # Clamp day to month length
    import calendar
    last = calendar.monthrange(y, m)[1]
    return date(y, m, min(d.day, last))


class Ticker:
    """Yields successive Period objects covering [start, end] in chunks of
    `tick_unit × tick_size`. Supports week / month / quarter."""

    def __init__(self, start: date, end: date, tick_unit: str = "month",
                 tick_size: int = 1, reflection_every_n_ticks: int = 12):
        self.start = start
        self.end = end
        self.tick_unit = tick_unit
        self.tick_size = max(1, int(tick_size))
        self.reflection_every_n_ticks = int(reflection_every_n_ticks)

    def periods(self) -> Iterator[Period]:
        cursor = self.start
        idx = 0
        while cursor <= self.end:
            if self.tick_unit == "week":
                period_end = cursor + timedelta(days=7 * self.tick_size - 1)
            elif self.tick_unit == "month":
                period_end = _add_months(cursor, self.tick_size) - timedelta(days=1)
            elif self.tick_unit == "quarter":
                period_end = _add_months(cursor, 3 * self.tick_size) - timedelta(days=1)
            else:
                raise ValueError(f"Unknown tick_unit: {self.tick_unit!r}")
            period_end = min(period_end, self.end)
            yield Period(start=cursor, end=period_end, index=idx)
            # Advance
            if self.tick_unit == "week":
                cursor = cursor + timedelta(days=7 * self.tick_size)
            elif self.tick_unit == "month":
                cursor = _add_months(cursor, self.tick_size)
            elif self.tick_unit == "quarter":
                cursor = _add_months(cursor, 3 * self.tick_size)
            idx += 1

    def should_reflect(self, period: Period) -> bool:
        return self.reflection_every_n_ticks > 0 and \
               (period.index + 1) % self.reflection_every_n_ticks == 0

    def total_periods(self) -> int:
        return sum(1 for _ in self.periods())
