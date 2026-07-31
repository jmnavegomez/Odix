from __future__ import annotations

from typing import TYPE_CHECKING

from ...exceptions import ParserError

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.italic import Italic

from .emphasis import parse_inline_emphasis


def parse_italic(parser: Parser) -> Italic:
    """Parses italic text."""

    parser._expect(TokenType.ASTERISK)

    italic = Italic()

    parse_inline_emphasis(
        parser,
        italic,
        TokenType.ASTERISK,
        1,
    )

    return italic