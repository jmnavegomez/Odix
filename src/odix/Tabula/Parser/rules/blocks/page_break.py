from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.page_break import PageBreak


def parse_page_break(parser: Parser) -> PageBreak:
    """Parses a page break.

    Expected syntax::

        ::pagebreak
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed page break.
    """

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    parser._expect(TokenType.COLON)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return PageBreak()