from __future__ import annotations

from .inline import Inline


class InlineCode(Inline):
    """Represents inline source code."""

    def __init__(self, code: str) -> None:
        """
        Initialize an inline code node.

        Args:
            code: Source code.
        """
        super().__init__()
        self.code = code