from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.paragraph import Paragraph

from ...exceptions import ParserError


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

    from ..dispatchers.inline import parse_inline

    paragraph = Paragraph()

    while not parser._match(*terminators):

        inline = parse_inline(parser)

        # parse_inline() should never return None when no
        # stop delimiter has been provided.
        assert inline is not None

        paragraph.add_child(inline)

    return paragraph


def parse_literal_until(
    parser: Parser,
    closing_type: TokenType,
    closing_length: int,
) -> str:
    """Parses literal text until a closing delimiter is found.

    Unlike ``parse_inline_content()``, this function does not parse nested
    inline elements. Every token between the delimiters is treated as plain
    text.

    Args:
        parser: Parser instance.
        closing_type: Token type that closes the literal sequence.
        closing_length: Required delimiter length.

    Returns:
        Literal text between the delimiters.

    Raises:
        ParserError: If the closing delimiter is not found.
    """
    value = ""

    while not parser._match(TokenType.EOF):

        if (
            parser._match(closing_type)
            and len(parser._current.value) == closing_length
        ):
            break
        
        value += parser._advance().value

    if parser._match(TokenType.EOF):
        raise ParserError(
            "Unterminated literal block."
        )
    
    if len(parser._current.value) != closing_length:
        raise ParserError("Invalid closing delimiter.")

    parser._advance()

    return value

def parse_literal_content(
    parser: Parser,
    *terminators: TokenType,
) -> str:
    """Parses a sequence of literal tokens.

    Unlike ``parse_inline_content()``, no inline parsing is performed.

    Args:
        parser: Parser instance.
        *terminators: Token types that terminate the sequence.

    Returns:
        Literal text.
    """
    value = ""

    while not parser._match(*terminators):
        value += parser._advance().value

    return value