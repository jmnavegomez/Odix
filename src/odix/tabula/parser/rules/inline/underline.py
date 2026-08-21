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
from ....nodes.underline import Underline
from .emphasis import parse_inline_emphasis


def parse_underline(parser: Parser) -> Underline:
    """Parses underlined text."""

    token = parser._expect_type(TokenType.UNDERSCORE)

    if len(token.value) != 3:
        raise ParserError(
            message="Underline must start with '___'.",
            token=token,
            expected_token_type=TokenType.UNDERSCORE,
        )

    underline = Underline()

    parse_inline_emphasis(
        parser,
        underline,
        token,
        3,
    )

    return underline
