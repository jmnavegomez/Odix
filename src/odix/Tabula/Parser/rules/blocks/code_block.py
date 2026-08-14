from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.code_block import CodeBlock
from ....nodes.text import Text
from ...exceptions import ParserError
from ..inline.code import parse_code_literal_until


def parse_code_block(parser: Parser) -> CodeBlock:
    """Parses a fenced code block."""

    opening = parser._expect(TokenType.BACKTICK)

    if len(opening.value) < 3:
        raise ParserError("A fenced code block requires at least three backticks.")

    language = None

    if parser._match(TokenType.TEXT):
        language = parser._advance().value.strip()

    parser._expect(TokenType.NEWLINE)

    code = parse_code_literal_until(
        parser,
        len(opening.value),
    )

    block = CodeBlock(language)

    block.add_child(Text(code))

    return block
