from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.paragraph import Paragraph

from ..dispatchers.inline import parse_inline


def parse_inline_content(
    parser: Parser,
    *terminators: TokenType,
) -> Paragraph:
    """Parses a sequence of inline elements.

    Parsing stops when one of the terminating token types is reached.

    Args:
        parser: Parser instance.
        *terminators: Token types that terminate the sequence.

    Returns:
        Paragraph containing the parsed inline nodes.
    """
    paragraph = Paragraph()

    while not parser._match(*terminators):

        inline = parse_inline(parser)

        # Defensive check. parse_inline() should never return None
        # when no stop delimiter has been provided.
        assert inline is not None

        paragraph.add_child(inline)

    return paragraph