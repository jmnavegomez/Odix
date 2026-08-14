from odix.typus.document_style import DocumentStyle
from odix.typus.margins import Margins


def test_document_style():
    margins = Margins(
        top="2cm",
        bottom="1.5cm",
        left="1.5cm",
        right="1.5cm",
    )

    style = DocumentStyle(
            document_class="book",
            page_size="a5paper",
            orientation="portrait",
            margins=margins,
            font="helvet",
            font_size="11pt",
            line_spacing=1.0,
            twoside=True,
            chapters_start_on_odd_page=True,
            table_of_contents= True,
            page_numbering=True,
            page_numbering_position="top",
            language= "spanish",
            packages=[
                    "inputenc",
                    "fontenc",
                    "graphicx",
                    "amsmath",
                ],
            )

    assert style.page_size == "a5paper"
    assert style.orientation == "portrait"

    assert style.margins is margins

    assert style.font_size == "11pt"
    assert style.line_spacing == 1.0

    assert style.twoside is True
    assert style.chapters_start_on_odd_page is True

    assert style.page_numbering is True
    assert style.page_numbering_position == "top"

    assert style.packages == [
        "inputenc",
        "fontenc",
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
            document_class="book",
            page_size="a5paper",
            orientation="portrait",
            margins=margins,
            font="helvet",
            font_size="11pt",
            line_spacing=1.0,
            twoside=True,
            chapters_start_on_odd_page=True,
            table_of_contents= True,
            page_numbering=True,
            page_numbering_position="top",
            language= "spanish",
            packages= packages,
            )

    packages.append("amsmath")

    assert style.packages == ["graphicx"]