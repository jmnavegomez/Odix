# Odix - Open-source publishing system for technical books
# Copyright (C) 2026 José Manuel Naveiro
#
# This file is part of Odix.
#
# Odix is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# Odix is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Odix. If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

from typing import TYPE_CHECKING

from ...exceptions import ParserError

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.section import Section
from ....nodes.text import Text
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

    token = parser._expect_type(TokenType.HASH)

    level = len(token.value)

    if not 1 <= level <= 6:
        raise ParserError(
            message=f"Invalid heading level ({level}). Markdown headings must have between 1 and 6 '#'.",
            token=parser.current,
            expected_token_type=TokenType.HASH,
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
