from __future__ import annotations

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