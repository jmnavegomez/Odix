from odix.typus import Typus
from odix.typus.document_style import DocumentStyle
from odix.typus.margins import Margins


def test_typus():
    margins = Margins(
        top="2cm",
        bottom="2cm",
        left="2cm",
        right="2cm",
    )

    document = DocumentStyle(
        page_size="a5paper",
        orientation="portrait",
        margins=margins,
        font_size="12pt",
        line_spacing=1.0,
        twoside=False,
        chapters_start_on_odd_page=False,
        page_numbering=True,
        page_numbering_position="top",
        packages=["graphicx"],
    )

    typus = Typus(document=document)

    assert typus.document is document

    from pathlib import Path

from odix.typus.document_style import DocumentStyle
from odix.typus.loader import Loader


def test_load_default_typus():
    root = Path(__file__).parents[3]

    typus_file = (
        root
        / "Odix"
        / "src"
        / "odix"
        / "typus"
        / "typus_default.yml"
    )

    document = Loader.load(typus_file)

    assert isinstance(document, DocumentStyle)

    assert document.page_size == "a5paper"
    assert document.orientation == "portrait"

    assert document.margins.top == "2cm"
    assert document.margins.bottom == "2cm"
    assert document.margins.left == "2cm"
    assert document.margins.right == "2cm"

    assert document.font_size == "12pt"
    assert document.line_spacing == 1.0

    assert document.twoside is False
    assert document.chapters_start_on_odd_page is False

    assert document.page_numbering is True
    assert document.page_numbering_position == "top"

    assert document.packages == [
        "inputenc",
        "fontenc",
        "babel",
        "graphicx",
        "amsmath",
    ]
    
from pathlib import Path

from odix.typus import Typus


def test_typus_from_file():
    root = Path(__file__).parents[3]

    typus_file = (
        root
        / "Odix"
        / "src"
        / "odix"
        / "typus"
        / "typus_default.yml"
    )

    typus = Typus.from_file(typus_file)

    assert isinstance(typus, Typus)
    assert typus.document.page_size == "a5paper"