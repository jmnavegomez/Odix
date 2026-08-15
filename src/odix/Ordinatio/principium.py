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

from pathlib import Path

from ..tabula import Tabula
from ..tabula.nodes import Document


class Principium:
    """A unit of knowledge in an Odix book."""

    def __init__(self, source: str | Path) -> None:
        self._source = Path(source)

    @property
    def source(self) -> Path:
        """Returns the source path."""
        return self._source

    @property
    def document(self) -> Document:
        """Returns the Tabula document."""
        tabula = Tabula(self._source)

        if not isinstance(tabula.ast, Document):
            raise TypeError("The Principium root must be a Document.")

        return tabula.ast
