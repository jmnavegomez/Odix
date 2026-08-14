from odix.tabula.lexer import Lexer
from odix.tabula.nodes import (
    Strike,
    Text,
)
from odix.tabula.parser import Parser


def test_parse_strike() -> None:
    lexer = Lexer()
    parser = Parser()

    document = parser.parse(
        lexer.tokenize("--strike--")
    )

    paragraph = document.children[0]

    strike = paragraph.children[0]

    assert isinstance(strike, Strike)

    assert len(strike.children) == 1

    assert isinstance(strike.children[0], Text)
    assert strike.children[0].text == "strike"