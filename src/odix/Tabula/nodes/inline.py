from __future__ import annotations

from abc import ABC
from typing import Any

from .node import Node


class Inline(Node, ABC):
    """Abstract base class for all inline nodes."""

    def content(self) -> tuple[Any, ...]:
        return ()