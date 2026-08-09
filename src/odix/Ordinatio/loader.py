from __future__ import annotations

from pathlib import Path

import yaml

from .book import Book
from .chapter import Chapter
from .principium import Principium


class Loader:
    """Loads an Odix book from a YAML file."""

    @classmethod
    def load(cls, path: str | Path) -> Book:
        """Loads a book from a YAML file."""
        path = Path(path)

        data = yaml.safe_load(
            path.read_text(encoding="utf-8")
        )

        if data is None:
            raise ValueError(
                "The YAML file is empty."
            )

        if "title" not in data:
            raise ValueError(
                "The book configuration is missing 'title'."
            )

        if "chapters" not in data:
            raise ValueError(
                "The book configuration is missing 'chapters'."
            )

        chapters = []

        for chapter_data in data["chapters"]:
            if "title" not in chapter_data:
                raise ValueError(
                    "The chapter configuration is missing 'title'."
                )

            if "principia" not in chapter_data:
                raise ValueError(
                    "The chapter configuration is missing "
                    "'principia'."
                )

            principia = []

            for principium_path in chapter_data["principia"]:
                source = path.parent / principium_path

                if not source.exists():
                    raise FileNotFoundError(source)

                principia.append(
                    Principium(source)
                )

            chapters.append(
                Chapter(
                    title=chapter_data["title"],
                    principia=principia,
                )
            )

        return Book(
            title=data["title"],
            chapters=chapters,
        )