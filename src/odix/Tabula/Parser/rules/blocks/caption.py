from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.caption import Caption

from ..inline.sequence import parse_inline_content


def parse_caption(parser: Parser) -> Caption:
    """Parses a figure caption.

    Expected syntax::

        ::caption
        Caption text.
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed caption.
    """

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    paragraph = parse_inline_content(
        parser,
        TokenType.COLON,
    )

    parser._expect(TokenType.COLON)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    caption = Caption()

    caption.children = paragraph.children

    for child in caption.children:
        child.parent = caption

    return caption