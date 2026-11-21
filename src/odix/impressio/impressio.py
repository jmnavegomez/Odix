
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

from odix.ordinatio import Book
from odix.scriptorium import Language
from odix.typus import Typus

from .publishers.latex import LatexPublisher


class Impressio:
    """Publishes an Odix book using the selected publishing format."""

    def __init__(
        self,
        book: Book,
        typus: Typus,
        language: Language = Language.LATEX,
    ) -> None:
        self._book = book
        self._typus = typus
        self._language = language

    @property
    def book(self) -> Book:
        """Returns the book to publish."""
        return self._book

    @property
    def typus(self) -> Typus:
        """Returns the publication style."""
        return self._typus

    @property
    def language(self) -> Language:
        """Returns the selected publication language."""
        return self._language

    def _get_publisher(self):
        """Returns the publisher associated with the selected language."""

        publishers = {
            Language.LATEX: LatexPublisher,
        }

        try:
            publisher_class = publishers[self._language]
        except KeyError:
            raise ValueError(
                f"No publisher available for language: {self._language}"
            ) from None

        return publisher_class(
            self._book,
            self._typus,
        )

    def publish(
        self,
        path: str | Path,
    ) -> None:
        """Publishes the book using the selected publisher."""

        publisher = self._get_publisher()
        publisher.publish(path)
