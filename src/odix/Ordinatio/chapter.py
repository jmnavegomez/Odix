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
