from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.list import List

from .list_item import parse_list_item


def parse_list(parser: Parser) -> List:
    """Parses an unordered list.

    Args:
        parser: Parser instance.

    Returns:
        Parsed list.
    """

    lst = List()

    while parser._match(
        TokenType.HYPHEN,
        TokenType.PLUS,
    ):
        lst.add_child(
            parse_list_item(parser)
        )

    return lst