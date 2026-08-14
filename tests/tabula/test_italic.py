from odix.tabula.lexer import Lexer
from odix.tabula.nodes import (
    Italic,
    Paragraph,
    Text,
)
from odix.tabula.parser import Parser


def test_parse_italic() -> None:
    lexer = Lexer()
    parser = Parser()

    document = parser.parse(
        lexer.tokenize("·italic·")
    )

    paragraph = document.children[0]

    assert isinstance(paragraph, Paragraph)

    assert len(paragraph.children) == 1

    italic = paragraph.children[0]

    assert isinstance(italic, Italic)

    assert len(italic.children) == 1

    text = italic.children[0]

    assert isinstance(text, Text)
    assert text.text == "italic"