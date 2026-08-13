from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.cross_reference import CrossReference

from .sequence import parse_literal_until


def parse_cross_reference(parser: Parser) -> CrossReference:
    """Parses a cross reference.

    Expected syntax::

        $$ec:23$$

    Args:
        parser: Parser instance.

    Returns:
        Parsed reference.
    """

    parser._expect(TokenType.DOLLAR)

    key = parse_literal_until(
        parser,
        TokenType.DOLLAR,
        2,
    ).strip()

    return CrossReference(key)