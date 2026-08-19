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

import yaml

from .book import Bibliography, Book, Metadata
from .chapter import Chapter
from .principium import Principium


class Loader:
    """Loads an Odix book from a YAML file."""

    @classmethod
    def load(cls, path: str | Path) -> Book:
        """Loads a book from a YAML file."""
        path = Path(path)

        data = yaml.safe_load(path.read_text(encoding="utf-8"))

        if data is None:
            raise ValueError("The YAML file is empty.")

        if "metadata" not in data:
            raise ValueError("The book configuration is missing 'metadata'.")

        metadata_data = data["metadata"]

        if "title" not in metadata_data:
            raise ValueError("The metadata configuration is missing 'title'.")

        if "chapters" not in data:
            raise ValueError("The book configuration is missing 'chapters'.")

        metadata = Metadata(
            title=metadata_data["title"],
            author=metadata_data.get("author"),
            subtitle=metadata_data.get("subtitle"),
            date=metadata_data.get("date"),
            edition=metadata_data.get("edition"),
        )

        bibliography = None

        if "bibliography" in data:
            bibliography_data = data["bibliography"]

            if "file" not in bibliography_data:
                raise ValueError("The bibliography configuration is missing 'file'.")

            bibliography = Bibliography(
                file=bibliography_data["file"],
                style=bibliography_data.get("style", "plain"),
            )

        chapters = []

        for chapter_data in data["chapters"]:
            if "title" not in chapter_data:
                raise ValueError("The chapter configuration is missing 'title'.")

            if "principia" not in chapter_data:
                raise ValueError("The chapter configuration is missing " "'principia'.")

            principia = []

            for principium_path in chapter_data["principia"]:
                source = path.parent / principium_path

                if not source.exists():
                    raise FileNotFoundError(source)

                principia.append(Principium(source))

            chapters.append(
                Chapter(
                    title=chapter_data["title"],
                    principia=principia,
                )
            )

        return Book(
            metadata=metadata,
            bibliography=bibliography,
            chapters=chapters,
        )
