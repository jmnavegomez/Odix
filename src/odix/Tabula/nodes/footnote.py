from __future__ import annotations

from .block import Block


class Footnote(Block):
    """Represents a footnote."""

    def __init__(self, key: str) -> None:
        """
        Initialize a footnote.

        Args:
            key: Unique footnote key.
        """
        super().__init__()
        self.key = key
