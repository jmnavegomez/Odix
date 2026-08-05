from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.quote import Quote

from ..inline.sequence import parse_inline_content


def parse_quote(parser: Parser) -> Quote:
    """Parses a block quote."""

    parser._expect(TokenType.GREATER_THAN)

    quote = Quote()

    paragraph = parse_inline_content(
        parser,
        TokenType.NEWLINE,
        TokenType.EOF,
    )

    quote.add_child(paragraph)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return quote