from __future__ import annotations

from typing import TYPE_CHECKING

from ...exceptions import ParserError

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.strike import Strike

from .emphasis import parse_inline_emphasis


def parse_strike(parser: Parser) -> Strike:
    """Parses strikethrough text."""

    token = parser._expect(TokenType.HYPHEN)

    if len(token.value) != 2:
        raise ParserError(
            "Strikethrough must start with '--'."
        )

    strike = Strike()

    parse_inline_emphasis(
        parser,
        strike,
        TokenType.HYPHEN,
        2,
    )

    return strike