from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.label import Label
from ....nodes.math_block import MathBlock
from ..inline.sequence import parse_literal_until


def parse_math_block(parser: Parser) -> MathBlock:
    """Parses a math block.

    Expected syntax::

        ::math
        E = mc^2
        label
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
        TokenType.NEWLINE,
        1,
    ).strip()

    math_block = MathBlock(expression)

    if not parser._match(TokenType.COLON):
        label = parse_literal_until(
            parser,
            TokenType.NEWLINE,
            1,
        ).strip()
        math_block.add_child(Label(label))

    parser._expect(TokenType.COLON)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return math_block
