from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.figure import Figure

from ..dispatchers.blocks import parse_block


def parse_figure(parser: Parser) -> Figure:
    """Parses a figure block.

    Expected syntax::

        ::figure
        ...
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed figure.
    """

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    figure = Figure()

    while not (
        parser._match(TokenType.COLON)
        and len(parser._current.value) == 2
    ):
        figure.add_child(parse_block(parser))

    parser._expect(TokenType.COLON)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return figure