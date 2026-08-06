from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.figure import Figure
from ....nodes.image import Image
from ....nodes.text import Text

from ..inline.sequence import parse_literal_until
from ..blocks.caption import parse_inline_caption



def parse_figure(parser: Parser) -> Figure:
    """Parses a figure block.

    Expected syntax::

        ::figure
        file_path
        caption
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
        figure.add_child(Image(parse_literal_until(parser,TokenType.NEWLINE,1)))
        figure.add_child(parse_inline_caption(parser))

    parser._expect(TokenType.COLON)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return figure