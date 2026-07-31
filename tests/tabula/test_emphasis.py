from odix.tabula.nodes import (
    Paragraph,
    Bold,
    Italic,
    Underline,
    Strike,
)

from odix.tabula.lexer import Lexer
from odix.tabula.parser import Parser

def test_parse_multiple_emphasis() -> None:
    lexer = Lexer()
    parser = Parser()

    markdown = (
        "**bold** /n *italic* /n __underline__ /n --strike--"
    )

    document = parser.parse(
        lexer.tokenize(markdown)
    )

    paragraph = document.children[0]

    assert isinstance(paragraph.children[0], Bold)
    assert isinstance(paragraph.children[2], Italic)
    assert isinstance(paragraph.children[4], Underline)
    assert isinstance(paragraph.children[6], Strike)