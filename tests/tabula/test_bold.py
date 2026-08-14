from odix.tabula.lexer import Lexer
from odix.tabula.nodes import (
    Bold,
    Document,
    Paragraph,
    Text,
)
from odix.tabula.parser import Parser


def test_parse_bold() -> None:
    lexer = Lexer()
    parser = Parser()

    markdown = "**Hello**"

    tokens = lexer.tokenize(markdown)
    document = parser.parse(tokens)

    assert isinstance(document, Document)

    assert len(document.children) == 1

    paragraph = document.children[0]

    assert isinstance(paragraph, Paragraph)

    assert len(paragraph.children) == 1

    bold = paragraph.children[0]

    assert isinstance(bold, Bold)

    assert len(bold.children) == 1

    text = bold.children[0]

    assert isinstance(text, Text)

    assert text.text == "Hello"

def test_parse_bold_inside_paragraph() -> None:
    lexer = Lexer()
    parser = Parser()

    markdown = "Hello **world**!"

    tokens = lexer.tokenize(markdown)
    document = parser.parse(tokens)

    paragraph = document.children[0]

    assert isinstance(paragraph, Paragraph)

    assert len(paragraph.children) == 3

    assert isinstance(paragraph.children[0], Text)
    assert paragraph.children[0].text == "Hello "

    assert isinstance(paragraph.children[1], Bold)
    assert isinstance(paragraph.children[1].children[0], Text)
    assert paragraph.children[1].children[0].text == "world"

    assert isinstance(paragraph.children[2], Text)
    assert paragraph.children[2].text == "!"
