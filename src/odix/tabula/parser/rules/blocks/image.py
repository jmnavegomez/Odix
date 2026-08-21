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

from ....lexer.token import Token
from ....lexer.token_type import TokenType
from ....nodes.image import Image
from ..inline.sequence import parse_literal_until


def parse_image(parser: Parser, initial_token: Token) -> Image:
    """Parses an image block.

    Expected syntax::

        ::image
        figures/example.png
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed image.
    """

    parser._expect_type(TokenType.NEWLINE)

    source = parse_literal_until(
        parser,
        initial_token,
        2,
    ).strip()

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return Image(source)
