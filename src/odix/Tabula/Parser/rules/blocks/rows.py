from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.row import Row
from .cells import parse_cell


def parse_row(parser: Parser) -> Row:
    """Parses a table row."""

    row = Row()

    parser._expect(TokenType.PIPE)

    while not parser._match(TokenType.NEWLINE, TokenType.EOF):

        cell = parse_cell(parser)
        row.add_child(cell)

    if parser._match(TokenType.NEWLINE):
        parser._advance()
        
    return row