from odix.tabula.nodes import (
    Paragraph,
    Underline,
    Text,
)

from odix.tabula.lexer import Lexer
from odix.tabula.parser import Parser

def test_parse_underline() -> None:
    lexer = Lexer()
    parser = Parser()

    document = parser.parse(
        lexer.tokenize("___underline___")
    )

    paragraph = document.children[0]

    underline = paragraph.children[0]

    assert len(underline.children) == 1

    assert isinstance(underline, Underline)

    assert isinstance(underline.children[0], Text)
    assert underline.children[0].text == "underline"