from __future__ import annotations

from collections.abc import Iterable

from .chapter import Chapter


class Metadata:
    """Metadata of an Odix publication."""

    def __init__(
        self,
        title: str,
        author: str | None = None,
        subtitle: str | None = None,
        date: str | None = None,
        edition: str | None = None,
    ) -> None:
        self._title = title
        self._author = author
        self._subtitle = subtitle
        self._date = date
        self._edition = edition

    @property
    def title(self) -> str:
        """Returns the book title."""
        return self._title

    @property
    def author(self) -> str | None:
        """Returns the book author."""
        return self._author

    @property
    def subtitle(self) -> str | None:
        """Returns the book subtitle."""
        return self._subtitle

    @property
    def date(self) -> str | None:
        """Returns the publication date."""
        return self._date

    @property
    def edition(self) -> str | None:
        """Returns the book edition."""
        return self._edition

class Bibliography:
    """Bibliography configuration of an Odix publication."""

    def __init__(
        self,
        file: str,
        style: str = "plain",
    ) -> None:
        self._file = file
        self._style = style

    @property
    def file(self) -> str:
        """Returns the bibliography file."""
        return self._file

    @property
    def style(self) -> str:
        """Returns the bibliography style."""
        return self._style


class Book:
    """A book of an Odix publication."""

    def __init__(
        self,
        metadata: Metadata,
        chapters: Iterable[Chapter],
        bibliography: Bibliography | None = None,
    ) -> None:
        self._metadata = metadata
        self._chapters = list(chapters)
        self._bibliography = bibliography

    @property
    def metadata(self) -> Metadata:
        """Returns the book metadata."""
        return self._metadata

    @property
    def title(self) -> str:
        """Returns the book title."""
        return self._metadata.title

    @property
    def chapters(self) -> list[Chapter]:
        """Returns the chapters contained in the book."""
        return self._chapters

    @property
    def bibliography(self) -> Bibliography | None:
        """Returns the book bibliography."""
        return self._bibliography