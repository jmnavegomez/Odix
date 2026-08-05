from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....nodes.block import Block

from ....lexer.token_type import TokenType

from ..blocks.headings import parse_section
from ..blocks.paragraphs import parse_paragraph
from ..blocks.quotes import parse_quote
from ..blocks.lists import parse_list
from ..blocks.tables import parse_table


def parse_block(parser: Parser) -> Block:
    """Parses the next block element.

    Args:
        parser: Parser instance.

    Returns:
        Parsed block node.

    Raises:
        NotImplementedError: If the block type is not implemented.
    """

    # Headings
    if parser._match(TokenType.HASH):
        return parse_section(parser)

    # Code blocks
    if (
        parser._match(TokenType.BACKTICK)
        and len(parser._current.value) >= 3
    ):
        raise NotImplementedError

    # Math blocks
    if (
        parser._match(TokenType.DOLLAR)
        and len(parser._current.value) >= 2
    ):
        raise NotImplementedError

    # Quotes
    if parser._match(TokenType.GREATER_THAN):
        return parse_quote(parser)

    # Lists
    if (
        parser._match(
            TokenType.HYPHEN,
            TokenType.PLUS,
        )
        and len(parser._current.value) == 1
        and parser._peek() is not None
        and parser._peek().type is TokenType.TEXT
        and parser._peek().value.startswith(" ")
    ):
        return parse_list(parser)

    # Horizontal rules
    if (
        parser._match(TokenType.HYPHEN)
        and len(parser._current.value) >= 3
    ):
        raise NotImplementedError

    # Tables
    if parser._match(TokenType.PIPE):
        return parse_table(parser)

    # Markdown treats any line that does not start with a recognized
    # block marker as a paragraph.
    return parse_paragraph(parser)