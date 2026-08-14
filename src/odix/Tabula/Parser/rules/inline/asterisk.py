from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.text import Text


def parse_asterisk(parser: Parser) -> Text:
    """Parses a text node.

    Args:
        parser: Parser instance.

    Returns:
        Parsed text node.
    """

    token = parser._expect(TokenType.ASTERISK)

    return Text(token.value)
