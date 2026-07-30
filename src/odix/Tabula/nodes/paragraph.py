from __future__ import annotations

from typing import Any

from .block import Block


class Paragraph(Block):
    """Represents a paragraph.

    A paragraph groups inline nodes.
    """

    def __init__(self) -> None:
        """Initializes a paragraph node."""
        super().__init__()