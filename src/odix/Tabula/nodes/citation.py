from __future__ import annotations

from .inline import Inline


class Citation(Inline):
    """Represents a bibliography citation."""

    def __init__(self, key: str) -> None:
        """
        Initialize a citation.

        Args:
            key: Referenced bibliography key.
        """
        super().__init__()
        self.key = key
