from __future__ import annotations

from typing import TYPE_CHECKING

from ...exceptions import ParserError

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.underline import Underline

from .emphasis import parse_inline_emphasis


def parse_underline(parser: Parser) -> Underline:
    """Parses underlined text."""

    token = parser._expect(TokenType.UNDERSCORE)

    if len(token.value) != 2:
        raise ParserError(
            "Underline must start with '__'."
        )

    underline = Underline()

    parse_inline_emphasis(
        parser,
        underline,
        TokenType.UNDERSCORE,
        2,
    )

    return underline