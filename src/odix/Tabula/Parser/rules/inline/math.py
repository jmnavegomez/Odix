from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.math_inline import MathInline

from .sequence import parse_literal_until


def parse_math_inline(parser: Parser) -> MathInline:
    """Parses an inline mathematical expression.

    Expected syntax::

        $E = mc^2$

    Args:
        parser: Parser instance.

    Returns:
        Parsed inline mathematical expression.
    """

    parser._expect(TokenType.DOLLAR)

    expression = parse_literal_until(
        parser,
        TokenType.DOLLAR,
        1,
    ).strip()

    return MathInline(expression)