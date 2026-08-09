from pathlib import Path

from odix.ordinatio import Book
from odix.ordinatio.loader import Loader


def test_load_book(tmp_path: Path):
    principium_01 = tmp_path / "principium_01.md"
    principium_02 = tmp_path / "principium_02.md"
    principium_03 = tmp_path / "principium_03.md"

    principium_01.touch()
    principium_02.touch()
    principium_03.touch()

    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
title: Volumen 01

chapters:
  - title: Capítulo 1
    principia:
      - principium_01.md
      - principium_02.md

  - title: Capítulo 2
    principia:
      - principium_03.md
""",
        encoding="utf-8",
    )

    book = Loader.load(book_file)

    assert isinstance(book, Book)
    assert book.title == "Volumen 01"

    assert len(book.chapters) == 2

    assert book.chapters[0].title == "Capítulo 1"
    assert len(book.chapters[0].principia) == 2

    assert book.chapters[1].title == "Capítulo 2"
    assert len(book.chapters[1].principia) == 1

def test_load_book_resolves_principium_paths(tmp_path: Path):
    principium = tmp_path / "principium_01.md"
    principium.touch()

    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
title: Volumen 01

chapters:
  - title: Capítulo 1
    principia:
      - principium_01.md
""",
        encoding="utf-8",
    )

    book = Loader.load(book_file)

    assert (
        book.chapters[0].principia[0].source
        == principium
    )

import pytest

def test_load_empty_yaml(tmp_path: Path):
    book_file = tmp_path / "book.yml"
    book_file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="empty"):
        Loader.load(book_file)

def test_load_missing_title(tmp_path: Path):
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
chapters: []
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="title"):
        Loader.load(book_file)

def test_load_missing_chapters(tmp_path: Path):
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
title: Volumen 01
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="chapters"):
        Loader.load(book_file)

def test_load_missing_principia(tmp_path: Path):
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
title: Volumen 01

chapters:
  - title: Capítulo 1
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="principia"):
        Loader.load(book_file)

def test_load_missing_principium(tmp_path: Path):
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
title: Volumen 01

chapters:
  - title: Capítulo 1
    principia:
      - principium_01.md
""",
        encoding="utf-8",
    )

    with pytest.raises(FileNotFoundError, match="principium_01.md"):
        Loader.load(book_file)

from pathlib import Path

# from odix.ordinatio.loader import Loader


def test_load_example_book():
    root = Path(__file__).parents[3]
    book_file = root / "Odix" / "examples" / "Volumen_01" / "book.yml"

    book = Loader.load(book_file)

    assert book.title == "Volumen 01"
    assert len(book.chapters) == 3

    assert book.chapters[0].title == "Capítulo 1"
    assert len(book.chapters[0].principia) == 2

    assert book.chapters[1].title == "Capítulo 2"
    assert len(book.chapters[1].principia) == 2

    assert book.chapters[2].title == "Capítulo 3"
    assert len(book.chapters[2].principia) == 3