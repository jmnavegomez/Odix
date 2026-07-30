from __future__ import annotations

from .block import Block


class MathBlock(Block):
    """Represents a block mathematical expression."""

    def __init__(self, expression: str) -> None:
        """
        Initialize a block math node.

        Args:
            expression: Mathematical expression.
        """
        super().__init__()
        self.expression = expression