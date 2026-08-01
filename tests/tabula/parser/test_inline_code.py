from odix.tabula.lexer import Lexer
from odix.tabula.parser import Parser

from odix.tabula.nodes import (
    Paragraph,
    InlineCode,
)


def test_inline_code() -> None:
    lexer = Lexer()
    parser = Parser()

    markdown = "`print(x)`"

    document = parser.parse(
        lexer.tokenize(markdown)
    )

    paragraph = document.children[0]

    assert isinstance(paragraph, Paragraph)

    assert len(paragraph.children) == 1

    code = paragraph.children[0]

    assert isinstance(code, InlineCode)

    assert code.code == "print(x)"

from odix.tabula.nodes import (
    Paragraph,
    Text,
    InlineCode,
)


def test_inline_code_inside_paragraph() -> None:
    lexer = Lexer()
    parser = Parser()

    markdown = "Call `print(x)` now."

    document = parser.parse(
        lexer.tokenize(markdown)
    )

    paragraph = document.children[0]

    assert isinstance(paragraph, Paragraph)

    assert len(paragraph.children) == 3

    assert isinstance(paragraph.children[0], Text)
    assert paragraph.children[0].text == "Call "

    assert isinstance(paragraph.children[1], InlineCode)
    assert paragraph.children[1].code == "print(x)"

    assert isinstance(paragraph.children[2], Text)
    assert paragraph.children[2].text == " now."

from odix.tabula.nodes import InlineCode


def test_inline_code_is_literal() -> None:
    lexer = Lexer()
    parser = Parser()

    markdown = "`**bold**`"

    document = parser.parse(
        lexer.tokenize(markdown)
    )

    paragraph = document.children[0]

    code = paragraph.children[0]

    assert isinstance(code, InlineCode)

    assert code.code == "**bold**"

import pytest

from odix.tabula.parser.exceptions import ParserError


def test_unterminated_inline_code() -> None:
    lexer = Lexer()
    parser = Parser()

    with pytest.raises(ParserError):
        parser.parse(
            lexer.tokenize("`print(x)")
        )