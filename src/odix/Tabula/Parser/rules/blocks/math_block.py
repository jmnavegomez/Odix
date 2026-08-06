from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.math_block import MathBlock

from ..inline.sequence import parse_literal_until


def parse_math_block(parser: Parser) -> MathBlock:
    """Parses a math block.

    Expected syntax::

        ::math
        E = mc^2
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed math block.
    """

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    expression = parse_literal_until(
        parser,
        TokenType.COLON,
        2,
    ).strip()

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return MathBlock(expression)