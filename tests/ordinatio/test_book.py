from odix.ordinatio import Book, Chapter, Principium
from pathlib import Path

def test_book_stores_title():
    book = Book(
        title="Desarrollo Real Python",
        chapters=[],
    )

    assert book.title == "Desarrollo Real Python"


def test_book_stores_chapters():
    chapter_1 = Chapter(
        title="Clases",
        principia=[],
    )
    chapter_2 = Chapter(
        title="Herencia",
        principia=[],
    )

    book = Book(
        title="Desarrollo Real Python",
        chapters=[chapter_1, chapter_2],
    )

    assert book.chapters == [
        chapter_1,
        chapter_2,
    ]

def test_book_structure(tmp_path: Path):
    pill_1 = tmp_path / "01_clases.md"
    pill_2 = tmp_path / "02_atributos.md"
    pill_3 = tmp_path / "03_metodos.md"

    for path in (pill_1, pill_2, pill_3):
        path.write_text("# Test", encoding="utf-8")

    chapter = Chapter(
        title="Programación Orientada a Objetos",
        principia=[
            Principium(pill_1),
            Principium(pill_2),
            Principium(pill_3),
        ],
    )

    book = Book(
        title="Desarrollo Real Python",
        chapters=[chapter],
    )

    assert book.title == "Desarrollo Real Python"
    assert len(book.chapters) == 1
    assert book.chapters[0].title == (
        "Programación Orientada a Objetos"
    )
    assert len(book.chapters[0].principia) == 3
    assert book.chapters[0].principia[0].source == pill_1
    assert book.chapters[0].principia[1].source == pill_2
    assert book.chapters[0].principia[2].source == pill_3