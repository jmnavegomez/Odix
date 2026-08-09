from __future__ import annotations

from typing import Iterable

from .chapter import Chapter


class Book:
    """A book of an Odix publication."""

    def __init__(
        self,
        title: str,
        chapters: Iterable[Chapter],
    ) -> None:
        self._title = title
        self._chapters = list(chapters)

    @property
    def title(self) -> str:
        """Returns the book title."""
        return self._title

    @property
    def chapters(self) -> list[Chapter]:
        """Returns the chapters contained in the book."""
        return self._chapters