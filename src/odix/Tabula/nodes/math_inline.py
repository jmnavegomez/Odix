from __future__ import annotations

from .inline import Inline


class MathInline(Inline):
    """Represents an inline mathematical expression."""

    def __init__(self, expression: str) -> None:
        """
        Initialize an inline math node.

        Args:
            expression: Mathematical expression.
        """
        super().__init__()
        self.expression = expression