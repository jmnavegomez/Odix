from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.cell import Cell

from ..inline.sequence import parse_inline_content


def parse_cell(parser: Parser) -> Cell:

    cell = Cell()

    paragraph = parse_inline_content(
        parser,
        TokenType.PIPE,
        TokenType.NEWLINE,
        TokenType.EOF,
    )

    cell.add_child(paragraph)

    if parser._match(TokenType.PIPE):
        parser._advance()

    return cell