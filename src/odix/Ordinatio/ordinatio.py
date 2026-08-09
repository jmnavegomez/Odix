from __future__ import annotations

from pathlib import Path

from .book import Book
from .loader import Loader


class Ordinatio:
    """Public interface for loading Odix book structures."""

    @classmethod
    def from_file(cls, path: str | Path) -> Book:
        """Loads a book structure from a YAML file."""
        return Loader.load(path)