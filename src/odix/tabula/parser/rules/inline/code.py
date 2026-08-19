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
        raise ParserError("Unterminated code block.")

    parser._expect(TokenType.BACKTICK)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return code
