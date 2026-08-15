from pathlib import Path

from odix.impressio import Impressio
from odix.ordinatio import Ordinatio
from odix.typus import Typus


def test_impressio():
    root = Path(__file__).parents[3]

    volume = root / "Odix" / "examples" / "Volumen_01"

    book = Ordinatio.from_file(volume / "book.yml")

    volume = root / "Odix" / "examples" / "Volumen_01"

    typus_file = volume / "typus.yml"

    typus = Typus.from_file(typus_file)

    impressio = Impressio(
        book=book,
        typus=typus,
    )

    assert impressio.book is book
    assert impressio.typus is typus

    assert book.title == "Odix"
    assert len(book.chapters) == 4

    assert sum(len(chapter.principia) for chapter in book.chapters) == 9
