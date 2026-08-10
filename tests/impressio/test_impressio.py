from pathlib import Path

from odix.impressio import Impressio
from odix.ordinatio import Ordinatio
from odix.typus import Typus


def test_impressio():
    root = Path(__file__).parents[3]

    volume = (
        root
        / "Odix"
        / "examples"
        / "Volumen_01"
    )

    book = Ordinatio.from_file(
        volume / "book.yml"
    )

    typus = Typus.from_file(
        root
        / "Odix"
        / "src"
        / "odix"
        / "typus"
        / "typus_default.yml"
    )

    impressio = Impressio(
        book=book,
        typus=typus,
    )

    assert impressio.book is book
    assert impressio.typus is typus

    assert book.title == "Volumen 01"
    assert len(book.chapters) == 3
    assert book.title == "Volumen 01"

    assert sum(
        len(chapter.principia)
        for chapter in book.chapters
    ) == 7