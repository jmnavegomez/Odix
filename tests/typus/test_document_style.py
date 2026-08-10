from odix.typus.document_style import DocumentStyle
from odix.typus.margins import Margins


def test_document_style():
    margins = Margins(
        top="2cm",
        bottom="2cm",
        left="2cm",
        right="2cm",
    )

    style = DocumentStyle(
        document_class="book",
        page_size="a5paper",
        orientation="portrait",
        margins=margins,
        font_size="12pt",
        line_spacing=1.0,
        twoside=False,
        chapters_start_on_odd_page=False,
        page_numbering=True,
        page_numbering_position="top",
        language = "spanish",
        packages=[
            "inputenc",
            "fontenc",
            "babel",
            "graphicx",
            "amsmath",
        ],
    )

    assert style.page_size == "a5paper"
    assert style.orientation == "portrait"

    assert style.margins is margins

    assert style.font_size == "12pt"
    assert style.line_spacing == 1.0

    assert style.twoside is False
    assert style.chapters_start_on_odd_page is False

    assert style.page_numbering is True
    assert style.page_numbering_position == "top"

    assert style.packages == [
        "inputenc",
        "fontenc",
        "babel",
        "graphicx",
        "amsmath",
    ]

def test_document_style_copies_packages():
    margins = Margins(
        top="2cm",
        bottom="2cm",
        left="2cm",
        right="2cm",
    )

    packages = ["graphicx"]

    style = DocumentStyle(
        document_class= "book",
        page_size="a5paper",
        orientation="portrait",
        margins=margins,
        font_size="12pt",
        line_spacing=1.0,
        twoside=False,
        chapters_start_on_odd_page=False,
        page_numbering=True,
        page_numbering_position="top",
        language = "english",
        packages=packages,
    )

    packages.append("amsmath")

    assert style.packages == ["graphicx"]