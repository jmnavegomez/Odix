from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.italic import Italic
from .emphasis import parse_inline_emphasis


def parse_italic(parser: Parser) -> Italic:
    """Parses italic text."""

    parser._expect(TokenType.MIDDLE_DOT)

    italic = Italic()

    parse_inline_emphasis(
        parser,
        italic,
        TokenType.MIDDLE_DOT,
        1,
    )

    return italic
