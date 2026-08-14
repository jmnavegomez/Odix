from odix.ordinatio import Ordinatio
from pathlib import Path

def test_ordinatio_loads_book():
    root = Path(__file__).parents[3]

    book_file = (
        root
        / "Odix"
        / "examples"
        / "Volumen_01"
        / "book.yml"
    )

    book = Ordinatio.from_file(book_file)

    assert book.title == "Desarrollo Real de Python"