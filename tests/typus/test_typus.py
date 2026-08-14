from odix.typus import Typus
from odix.typus.document_style import DocumentStyle
from odix.typus.margins import Margins


def test_typus():
    margins = Margins(
        top="2cm",
        bottom="1.5cm",
        left="1.5cm",
        right="1.5cm",
    )

    document = DocumentStyle(
        document_class="book",
        page_size="a5paper",
        orientation="portrait",
        margins=margins,
        font="helvet",
        font_size="11pt",
        line_spacing=1.0,
        twoside=True,
        chapters_start_on_odd_page=True,
        table_of_contents=True,
        page_numbering=True,
        page_numbering_position="top",
        language="spanish",
        packages=[
            "inputenc",
            "fontenc",
            "graphicx",
            "amsmath",
            "xcolor",
            "setspace",
            "titlesec",
            "tcolorbox",
            "colortbl",
        ],
    )

    typus = Typus(document=document)

    assert typus.document is document


from odix.typus.loader import Loader


def test_load_default_typus():
    root = Path(__file__).parents[3]

    volume = root / "Odix" / "examples" / "Volumen_01"

    typus_file = volume / "typus.yml"

    document = Loader.load(typus_file)

    assert isinstance(document, DocumentStyle)

    assert document.page_size == "a5paper"
    assert document.orientation == "portrait"

    assert document.margins.top == "2cm"
    assert document.margins.bottom == "1.5cm"
    assert document.margins.left == "1.5cm"
    assert document.margins.right == "1.5cm"

    assert document.font_size == "11pt"
    assert document.line_spacing == 1.0

    assert document.twoside is True
    assert document.chapters_start_on_odd_page is True

    assert document.page_numbering is True
    assert document.page_numbering_position == "top"

    assert document.packages == [
        "inputenc",
        "fontenc",
        "graphicx",
        "amsmath",
        "xcolor",
        "setspace",
        "titlesec",
        "tcolorbox",
        "colortbl",
    ]


from pathlib import Path


def test_typus_from_file():
    root = Path(__file__).parents[3]

    volume = root / "Odix" / "examples" / "Volumen_01"

    typus_file = volume / "typus.yml"

    typus = Typus.from_file(typus_file)

    assert isinstance(typus, Typus)
    assert typus.document.page_size == "a5paper"
