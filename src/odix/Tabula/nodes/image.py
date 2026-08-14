from __future__ import annotations

from typing import Any, Self

from .block import Block


class Image(Block):
    """Represents an image."""

    def __init__(self, source: str) -> None:
        """
        Initialize an image node.

        Args:
            source: Path or URI of the image.
        """
        super().__init__()
        self.source = source

    @classmethod
    def from_content(cls, content: Any) -> Self:
        return cls(content)
