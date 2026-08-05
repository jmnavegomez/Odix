from __future__ import annotations

from .inline import Inline
from .text import Text



class InlineCode(Inline):
    """Represents inline source code."""

    def __init__(self) -> None:
        """
        Initialize an inline code node.

        Args:
            code: Source code.
        """
        super().__init__()