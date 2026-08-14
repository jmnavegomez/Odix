from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.figure import Figure
from ....nodes.image import Image
from ....nodes.label import Label
from ..blocks.caption import parse_inline_caption
from ..inline.sequence import parse_literal_until


def parse_figure(parser: Parser) -> Figure:
    """Parses a figure block.

    Expected syntax::

        ::figure
        file_path
        caption
        label
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed figure.
    """

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    figure = Figure()

    figure.add_child(Image(parse_literal_until(parser, TokenType.NEWLINE, 1)))
    figure.add_child(parse_inline_caption(parser))

    if not parser._match(TokenType.COLON):
        figure.add_child(Label(parse_literal_until(parser, TokenType.NEWLINE, 1)))

    parser._expect(TokenType.COLON)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return figure
