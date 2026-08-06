from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.reference import Reference

from ..inline.sequence import parse_literal_until


def parse_reference(parser: Parser) -> Reference:
    """Parses a bibliography reference.

    Expected syntax::

        ::reference
        smith2025
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed bibliography reference.
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

    return Reference(key)