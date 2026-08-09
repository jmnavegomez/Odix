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
            raise TypeError(
                "The Principium root must be a Document."
            )

        return tabula.ast