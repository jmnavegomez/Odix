from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.bold import Bold

from ...exceptions import ParserError

from .emphasis import parse_inline_emphasis


def parse_bold(parser: Parser) -> Bold:
    """Parses bold text.

    Args:
        parser: Parser instance.

    Returns:
        Parsed bold node.

    Raises:
        ParserError: If the opening delimiter is invalid.
    """
    delimiter = parser._expect(TokenType.ASTERISK)

    if len(delimiter.value) != 2:
        raise ParserError(
            "Bold text must start with '**'."
        )

    bold = Bold()

    parse_inline_emphasis(
        parser,
        bold,
        TokenType.ASTERISK,
        2,
    )

    return bold