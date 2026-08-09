from __future__ import annotations

from pathlib import Path

from .document_style import DocumentStyle
from .loader import Loader


class Typus:
    """Defines the style of an Odix publication."""

    def __init__(
        self,
        document: DocumentStyle,
    ) -> None:
        self._document = document

    @property
    def document(self) -> DocumentStyle:
        """Returns the document style."""
        return self._document

    @classmethod
    def from_file(
        cls,
        path: str | Path,
    ) -> Typus:
        """Loads a Typus configuration from a YAML file."""
        document = Loader.load(path)

        return cls(
            document=document,
        )