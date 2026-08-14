from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.inline import Inline
from ...exceptions import ParserError


def parse_inline_emphasis(
    parser: Parser,
    node: Inline,
    closing_type: TokenType,
    closing_length: int,
) -> None:
    """Parses inline content until a closing delimiter is found.

    Parsed inline nodes are attached directly to ``node``.

    Args:
        parser: Parser instance.
        node: Inline node that will receive the parsed children.
        closing_type: Token type that closes the inline element.
        closing_length: Required delimiter length.

    Raises:
        ParserError: If the closing delimiter is not found.
    """
    # Local import to avoid circular imports.
    from ..dispatchers.inline import parse_inline

    # Parse nested inline elements until the closing delimiter
    # of the current emphasis node is reached.
    while not parser._match(TokenType.EOF):

        inline = parse_inline(
            parser,
            closing_type,
            closing_length,
        )

        # The closing delimiter belongs to this node.
        if inline is None:
            break

        node.add_child(inline)

    # Reaching EOF means that the emphasis was never closed.
    if parser._match(TokenType.EOF):
        raise ParserError("Unterminated inline element.")

    # Consume the closing delimiter.
    parser._expect(closing_type)
