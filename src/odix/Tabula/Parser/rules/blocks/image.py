from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.image import Image
from ..inline.sequence import parse_literal_until


def parse_image(parser: Parser) -> Image:
    """Parses an image block.

    Expected syntax::

        ::image
        figures/example.png
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed image.
    """

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    source = parse_literal_until(
        parser,
        TokenType.COLON,
        2,
    ).strip()

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return Image(source)