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

    @classmethod
    def from_content(
        cls,
        content: tuple[Any, ...],
    ) -> Self:
        """Creates a text node from serialized content."""

        return cls(content[0])
