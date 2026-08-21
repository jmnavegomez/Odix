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

from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token import Token
from ....lexer.token_type import TokenType
from ....nodes.block import Block
from .bibliography import parse_bibliography
from .caption import parse_caption
from .figure import parse_figure
from .footnote import parse_footnote
from .image import parse_image
from .math_block import parse_math_block
from .page_break import parse_page_break
from .reference import parse_reference

_DIRECTIVE_PARSERS: dict[str, Callable[[Parser, Token], Block]] = {
    "math": parse_math_block,
    "pagebreak": parse_page_break,
    "image": parse_image,
    "caption": parse_caption,
    "footnote": parse_footnote,
    "reference": parse_reference,
    "bibliography": parse_bibliography,
    "figure": parse_figure,
}


def parse_directive(parser: Parser) -> Block:
    """Parse a directive block."""

    initial_token = parser._expect_type(TokenType.COLON)

    name = parser._expect_type(TokenType.TEXT).value.strip().lower()

    method = _DIRECTIVE_PARSERS.get(name)

    if method is None:
        raise NotImplementedError(f"Unknown directive: {name}")

    return method(parser, initial_token)
