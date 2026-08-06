from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ...exceptions import ParserError


def parse_code_literal_until(
    parser: Parser,
    closing_length: int,
) -> str:
    """Parses the literal contents of a fenced code block.

    Every token between the opening and closing fences is treated as
    literal text. Markdown syntax is not parsed.

    Args:
        parser: Parser instance.
        closing_length: Number of backticks required to close the block.

    Returns:
        Source code contained in the block.

    Raises:
        ParserError: If the closing fence is not found.
    """
    code = ""

    while not parser._match(TokenType.EOF):

        if (
            parser._match(TokenType.BACKTICK)
            and len(parser._current.value) >= closing_length
        ):
            break

        code += parser._advance().value

    if parser._match(TokenType.EOF):
        raise ParserError(
            "Unterminated code block."
        )

    parser._expect(TokenType.BACKTICK)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return code