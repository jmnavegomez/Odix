from odix.tabula.nodes import (
    Paragraph,
    Bold,
    Italic,
    Underline,
    Strike,
    Text,
)

from odix.tabula.lexer import Lexer
from odix.tabula.parser import Parser

def test_multiple_inline_styles() -> None:
    lexer = Lexer()
    parser = Parser()

    markdown = (
        "Hello **bold** *italic* "
        "__underline__ --strike--."
    )

    document = parser.parse(
        lexer.tokenize(markdown)
    )

    paragraph = document.children[0]

    bold = paragraph.children[1]

    print(type(bold).__name__)
    print(len(bold.children))

    for child in bold.children:
        print(type(child).__name__, child.content())

    assert len(paragraph.children) == 9

    assert isinstance(paragraph.children[0], Text)
    assert isinstance(paragraph.children[1], Bold)
    assert isinstance(paragraph.children[2], Text)
    assert isinstance(paragraph.children[3], Italic)
    assert isinstance(paragraph.children[4], Text)
    assert isinstance(paragraph.children[5], Underline)
    assert isinstance(paragraph.children[6], Text)
    assert isinstance(paragraph.children[7], Strike)
    assert isinstance(paragraph.children[8], Text)
    assert paragraph.children[8].text == "."

if __name__ == "__main__":
    test_multiple_inline_styles()