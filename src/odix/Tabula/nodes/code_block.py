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

from typing import Any

from .block import Block


class CodeBlock(Block):
    """Represents a block of source code."""

    def __init__(
        self,
        language: str | None = None,
    ) -> None:
        """Initialize a code block.

        Args:
            language: Programming language used for syntax highlighting.
        """
        super().__init__()

        self.language = language

    def content(self) -> tuple[Any, ...]:
        """Returns the semantic content.

        Returns:
            Tuple containing the programming language.
        """
        return (self.language,)

    @classmethod
    def from_content(
        cls,
        content: tuple[str | None],
    ) -> CodeBlock:
        """Creates a code block from serialized content.

        Args:
            content: Serialized semantic content.

        Returns:
            Deserialized code block.
        """
        return cls(content[0])
