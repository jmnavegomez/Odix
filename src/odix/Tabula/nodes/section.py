from __future__ import annotations

from typing import Any

from .block import Block
from .paragraph import Paragraph


class Section(Block):
    """Represents a document section.

    A section groups other block nodes and is identified by its title
    and hierarchical level.
    """

    def __init__(self, level: int, title: Paragraph | None = None,) -> None:
        """Initializes a section node.

        Args:
            level: Hierarchical section level.
            title: Section title.
        """
        super().__init__()

        self.level = level
        self.title = title

    def content(self) -> tuple[Any, ...]:
        """Returns the semantic content of the section.

        Returns:
            Tuple containing the section title and level.
        """
        return (
            self.level,
            self.title,
        )