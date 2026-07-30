from __future__ import annotations

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