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
from ....nodes.label import Label
from ....nodes.math_block import MathBlock
from ..inline.sequence import parse_literal_until


def parse_math_block(parser: Parser) -> MathBlock:
    """Parses a math block.

    Expected syntax::

        ::math
        E = mc^2
        label
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed math block.
    """

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    expression = parse_literal_until(
        parser,
        TokenType.NEWLINE,
        1,
    ).strip()

    math_block = MathBlock(expression)

    if not parser._match(TokenType.COLON):
        label = parse_literal_until(
            parser,
            TokenType.NEWLINE,
            1,
        ).strip()
        math_block.add_child(Label(label))

    parser._expect(TokenType.COLON)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return math_block
