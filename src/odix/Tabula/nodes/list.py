from __future__ import annotations

from .block import Block


class List(Block):
    """Represents a list in the document."""

    def __init__(self, ordered: bool = False) -> None:
        """
        Initialize a list node.

        Args:
            ordered: Whether the list is ordered (numbered).
        """
        super().__init__()
        self.ordered = ordered
