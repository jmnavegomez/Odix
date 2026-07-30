from __future__ import annotations

from .inline import Inline


class Link(Inline):
    """Represents a hyperlink."""

    def __init__(self, target: str) -> None:
        """
        Initialize a hyperlink.

        Args:
            target: Destination of the hyperlink.
        """
        super().__init__()
        self.target = target