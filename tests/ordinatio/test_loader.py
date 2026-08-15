from pathlib import Path

from odix.ordinatio import Book
from odix.ordinatio.loader import Loader


def test_load_book(tmp_path: Path) -> None:
    principium_01 = tmp_path / "intro_python.md"
    principium_02 = tmp_path / "variables.md"
    principium_03 = tmp_path / "tipos_datos.md"

    principium_01.touch()
    principium_02.touch()
    principium_03.touch()

    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
metadata:
  title: Volumen 01
  subtitle: Introducción a Python
  author: José Manuel
  date: "2026"
  edition: 1ª edición

bibliography:
  file: references.bib
  style: plain

chapters:
  - title: Capítulo 1
    principia:
      - intro_python.md
      - variables.md

  - title: Capítulo 2
    principia:
      - tipos_datos.md
""",
        encoding="utf-8",
    )

    book = Loader.load(book_file)

    assert isinstance(book, Book)

    assert book.metadata.title == "Volumen 01"
    assert book.metadata.subtitle == "Introducción a Python"
    assert book.metadata.author == "José Manuel"
    assert book.metadata.date == "2026"
    assert book.metadata.edition == "1ª edición"

    assert book.bibliography is not None
    assert book.bibliography.file == "references.bib"
    assert book.bibliography.style == "plain"

    assert len(book.chapters) == 2

    assert book.chapters[0].title == "Capítulo 1"
    assert len(book.chapters[0].principia) == 2

    assert book.chapters[1].title == "Capítulo 2"
    assert len(book.chapters[1].principia) == 1


def test_load_book_resolves_principium_paths(
    tmp_path: Path,
) -> None:
    principium = tmp_path / "principium_01.md"
    principium.touch()

    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
metadata:
  title: Volumen 01

chapters:
  - title: Capítulo 1
    principia:
      - principium_01.md
""",
        encoding="utf-8",
    )

    book = Loader.load(book_file)

    assert book.chapters[0].principia[0].source == principium


import pytest


def test_load_empty_yaml(tmp_path: Path):
    book_file = tmp_path / "book.yml"
    book_file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="empty"):
        Loader.load(book_file)


def test_load_missing_metadata_title(tmp_path: Path) -> None:
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
metadata:
  author: José Manuel

chapters: []
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="title"):
        Loader.load(book_file)


def test_load_missing_metadata(tmp_path: Path) -> None:
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
chapters: []
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="metadata"):
        Loader.load(book_file)


def test_load_missing_chapters(tmp_path: Path) -> None:
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
metadata:
  title: Volumen 01
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="chapters"):
        Loader.load(book_file)


def test_load_missing_principia(tmp_path: Path) -> None:
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
metadata:
  title: Volumen 01

chapters:
  - title: Capítulo 1
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="principia"):
        Loader.load(book_file)


def test_load_missing_principium(tmp_path: Path) -> None:
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
metadata:
  title: Volumen 01

chapters:
  - title: Capítulo 1
    principia:
      - principium_01.md
""",
        encoding="utf-8",
    )

    with pytest.raises(
        FileNotFoundError,
        match="principium_01.md",
    ):
        Loader.load(book_file)


def test_load_book_without_bibliography(
    tmp_path: Path,
) -> None:
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
metadata:
  title: Volumen 01

chapters: []
""",
        encoding="utf-8",
    )

    book = Loader.load(book_file)

    assert book.bibliography is None


def test_load_bibliography(tmp_path: Path) -> None:
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
metadata:
  title: Volumen 01

bibliography:
  file: references.bib
  style: plain

chapters: []
""",
        encoding="utf-8",
    )

    book = Loader.load(book_file)

    assert book.bibliography is not None
    assert book.bibliography.file == "references.bib"
    assert book.bibliography.style == "plain"


def test_load_bibliography_default_style(
    tmp_path: Path,
) -> None:
    book_file = tmp_path / "book.yml"
    book_file.write_text(
        """
metadata:
  title: Volumen 01

bibliography:
  file: references.bib

chapters: []
""",
        encoding="utf-8",
    )

    book = Loader.load(book_file)

    assert book.bibliography is not None
    assert book.bibliography.file == "references.bib"
    assert book.bibliography.style == "plain"


from pathlib import Path

# from odix.ordinatio.loader import Loader


def test_load_example_book() -> None:
    root = Path(__file__).parents[3]
    book_file = root / "Odix" / "examples" / "Volumen_01" / "book.yml"

    book = Loader.load(book_file)

    assert book.title == "Odix"

    assert book.metadata.subtitle == ("Guía de usuario")
    assert book.metadata.author == "José Manuel Naveiro"
    assert book.metadata.date == "2026"
    assert book.metadata.edition == "1ª edición"

    assert book.bibliography is not None
    assert book.bibliography.file == "references.bib"
    assert book.bibliography.style == "plain"

    assert len(book.chapters) == 4

    assert book.chapters[0].title == "First Steps"
    assert len(book.chapters[0].principia) == 2

    assert book.chapters[1].title == "Book Configuration"
    assert len(book.chapters[1].principia) == 2

    assert book.chapters[2].title == "Scripture"
    assert len(book.chapters[2].principia) == 4
