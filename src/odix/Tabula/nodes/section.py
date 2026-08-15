# Odix - Open-source publishing system for technical books
# Copyright (C) 2026 José Manuel Naveiro
#
# This file is part of Odix.
#
# Odix is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# Odix is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Odix. If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

from typing import Any, Self

from .block import Block
from .paragraph import Paragraph


class Section(Block):
    """Represents a document section.

    A section groups other block nodes and is identified by its title
    and hierarchical level.
    """

    def __init__(
        self,
        level: int,
        title: Paragraph | None = None,
    ) -> None:
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
            self.title.context_hash if self.title else None,
        )

    @classmethod
    def from_content(
        cls,
        content: dict[str, Any],
    ) -> Self:
        """Creates a section from serialized content."""

        return cls(
            level=content["level"],
        )
