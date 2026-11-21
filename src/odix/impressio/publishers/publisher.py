
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

from odix.ordinatio import Book, Principium
from odix.tabula import Tabula
from odix.tabula.parser import ParserError
from odix.typus import Typus


class Publisher:
    """Base class for Odix publishing formats."""

    def __init__(
        self,
        book: Book,
        typus: Typus,
    ) -> None:
        self._book = book
        self._typus = typus

    @property
    def book(self) -> Book:
        """Returns the book to publish."""
        return self._book

    @property
    def typus(self) -> Typus:
        """Returns the publication style."""
        return self._typus

    def _parse_principium(
        self,
        principium: Principium,
    ) -> Tabula:
        """Parses a principium into a Tabula document."""

        try:
            return Tabula(principium.source)

        except ParserError as error:
            print(f"Error in principium: {principium.source}")
            print(f"    -Final token line: {error.token.line}")
            print(f"    -Final token column: {error.token.column}")
            print(f"    -Gotten token: {error.token.type.name}")

            if error.expected_token is not None:
                print()
                print(f"    -Initial token line: {error.expected_token.line}")
                print(f"    -Initial token column: {error.expected_token.column}")
                print(f"    -Expected token: {error.expected_token.type.name}")

            raise

    def publish(
        self,
        path: str | Path,
    ) -> None:
        """Publishes the book in the selected format."""
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement publish()."
        )
