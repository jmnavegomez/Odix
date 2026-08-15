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
