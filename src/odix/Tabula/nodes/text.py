from __future__ import annotations

from typing import Any

from .inline import Inline


class Text(Inline):
    """Represents a plain text fragment."""

    def __init__(self, text: str) -> None:
        """Initializes a text node.

        Args:
            text: Plain text.
        """
        super().__init__()

        self.text = text

    def content(self) -> tuple[Any, ...]:
        """Returns the semantic content of the text node.

        Returns:
            Tuple containing the text.
        """
        return (self.text,)