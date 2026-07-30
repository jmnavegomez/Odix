from __future__ import annotations

from typing import Any

from .block import Block


class Section(Block):
    """Represents a document section.

    A section groups other block nodes and is identified by its title
    and hierarchical level.
    """

    def __init__(self, title: str, level: int) -> None:
        """Initializes a section node.

        Args:
            title: Section title.
            level: Hierarchical section level.
        """
        super().__init__()

        self.title = title
        self.level = level

    def content(self) -> tuple[Any, ...]:
        """Returns the semantic content of the section.

        Returns:
            Tuple containing the section title and level.
        """
        return (
            self.title,
            self.level,
        )