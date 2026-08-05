from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.table import Table

from .rows import parse_row


def parse_table(parser: Parser) -> Table:
    """Parses a Markdown table."""

    table = Table()

    while parser._match(TokenType.PIPE):

        row = parse_row(parser)

        table.add_child(row)

    return table