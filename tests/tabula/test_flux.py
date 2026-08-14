from odix.tabula.lexer import Lexer
from odix.tabula.parser import Parser

from odix.tabula.nodes import (
    Document,
    Paragraph,
    Section,
    Text,
)


def test_heading_document() -> None:
    lexer = Lexer()
    parser = Parser()

    tokens = lexer.tokenize("# Introduction")

    document = parser.parse(tokens)

    assert isinstance(document, Document)

    assert len(document.children) == 1

    section = document.children[0]

    assert isinstance(section, Section)
    assert section.level == 1

    assert isinstance(section.title, Paragraph)

    assert len(section.title.children) == 1

    text = section.title.children[0]

    assert isinstance(text, Text)
    assert text.content() == ("Introduction",)

    assert len(section.children) == 0

from odix.tabula.lexer import Lexer
from odix.tabula.parser import Parser

from odix.tabula.nodes import (
    Document,
    Paragraph,
    Section,
    Text,
)


def test_parse_heading_and_paragraph() -> None:
    lexer = Lexer()
    parser = Parser()

    markdown = (
        "# Frase latina\n"
        "Lorem ipsum dolor sit amet."
    )

    tokens = lexer.tokenize(markdown)
    document = parser.parse(tokens)

    for token in tokens:
        print(token)

    for child in document.children:
        print(type(child), child)

    assert isinstance(document, Document)

    assert len(document.children) == 1

    section = document.children[0]
    paragraph = section.children[0]

    assert isinstance(section, Section)
    assert isinstance(paragraph, Paragraph)

    # Título de la sección
    assert isinstance(section.title, Paragraph)
    assert len(section.title.children) == 1

    title = section.title.children[0]

    assert isinstance(title, Text)
    assert title.text == "Frase latina"

    # Párrafo
    assert len(paragraph.children) == 1

    text = paragraph.children[0]

    assert isinstance(text, Text)
    assert text.text == "Lorem ipsum dolor sit amet."