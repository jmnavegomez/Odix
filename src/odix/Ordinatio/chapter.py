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

from collections.abc import Iterable

from .principium import Principium


class Chapter:
    """A chapter of an Odix book."""

    def __init__(
        self,
        title: str,
        principia: Iterable[Principium],
    ) -> None:
        self._title = title
        self._principia = list(principia)

    @property
    def title(self) -> str:
        """Returns the chapter title."""
        return self._title

    @property
    def principia(self) -> list[Principium]:
        """Returns the principia contained in the chapter."""
        return self._principia
