from __future__ import annotations

from ...exceptions import ParserError

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.text import Text

from ....nodes.section import Section

from ..inline.sequence import parse_inline_content


def parse_section(parser: Parser) -> Section:
    """Parses a section heading.

    Args:
        parser: Parser instance.

    Returns:
        Parsed section node.

    Raises:
        ParserError: If the heading level is invalid.
    """

    token = parser._expect(TokenType.HASH)

    level = len(token.value)

    if not 1 <= level <= 6:
        raise ParserError(
            f"Invalid heading level ({level}). "
            "Markdown headings must have between 1 and 6 '#'."
        )

    title = parse_inline_content(
        parser,
        TokenType.NEWLINE,
        TokenType.EOF,
    )

    if title.children:
        first = title.children[0]

        if isinstance(first, Text):
            first.text = first.text.lstrip()

            if not first.text:
                title.children.pop(0)

    section = Section(
        level=level,
        title=title,
    )
    
    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return section