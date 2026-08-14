from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.footnote import Footnote
from ..inline.sequence import parse_literal_until


def parse_footnote(parser: Parser) -> Footnote:
    """Parses a footnote.

    Expected syntax::

        ::footnote
        note1
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed footnote.
    """

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    key = parse_literal_until(
        parser,
        TokenType.COLON,
        2,
    ).strip()

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return Footnote(key)