from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.caption import Caption
from ....nodes.label import Label
from ....nodes.table import Table
from ..inline.sequence import parse_inline_content, parse_literal_until
from .rows import parse_row


def parse_table(parser: Parser) -> Table:
    """Parses a Markdown table."""

    table = Table()

    while parser._match(TokenType.PIPE):

        if _is_table_metadata(parser):
            _parse_table_metadata(parser, table)
        else:
            table.add_child(parse_row(parser))

    return table


def _is_table_metadata(parser: Parser) -> bool:
    """Checks whether the current pipe starts table metadata."""

    token = parser._peek()

    return (
        token.type is TokenType.COLON
        and len(token.value) == 2
    )


def _parse_table_metadata(
    parser: Parser,
    table: Table,
) -> None:
    """Parses table caption or label."""

    if parser._match(TokenType.PIPE):
        parser._advance()

    parser._expect(TokenType.COLON)

    name = parser._expect(TokenType.TEXT).value

    parser._expect(TokenType.COLON)

    if name == "caption":
        value = parse_inline_content(
            parser,
            TokenType.PIPE,
        )

        parser._expect(TokenType.PIPE)

        caption = Caption()
        caption.add_child(value)
        table.add_child(caption)

    elif name == "label":
        value = parse_literal_until(
            parser= parser,
            closing_type= TokenType.PIPE,
            closing_length=1,
        ).strip()
        
        table.add_child(Label.from_content(value))

    else:
        raise NotImplementedError(
            f"Unknown table metadata: {name}"
        )

    if parser._match(TokenType.NEWLINE):
        parser._advance()

