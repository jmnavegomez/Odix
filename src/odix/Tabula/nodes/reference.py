from __future__ import annotations

from typing import Any, Self

from .block import Block


class Reference(Block):
    """Represents a bibliography entry."""

    def __init__(self, key: str) -> None:
        """
        Initialize a bibliography reference.

        Args:
            key: Unique bibliography key.
        """
        super().__init__()
        self.key = key

    @classmethod
    def from_content(cls, content: Any) -> Self:
        return cls(content)
