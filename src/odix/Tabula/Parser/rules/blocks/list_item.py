from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.list_item import ListItem

from ..inline.sequence import parse_inline_content


def parse_list_item(parser: Parser) -> ListItem:
    """Parses a list item.

    Args:
        parser: Parser instance.

    Returns:
        Parsed list item.
    """

    parser._advance()      # Consume '-' or '+'

    item = ListItem()

    paragraph = parse_inline_content(
        parser,
        TokenType.NEWLINE,
        TokenType.EOF,
    )

    item.add_child(paragraph)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return item