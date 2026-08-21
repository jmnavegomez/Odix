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
from ....nodes.inline_code import InlineCode
from ....nodes.text import Text
from ..inline.sequence import parse_literal_until


def parse_inline_code(parser: Parser) -> InlineCode:
    """Parses an inline code element.

    Inline code is delimited by single backticks and its content is treated
    as literal text. Markdown syntax inside the delimiters is not parsed.

    Args:
        parser: Parser instance.

    Returns:
        Parsed inline code node.
    """

    initial_token = parser._expect_type(TokenType.BACKTICK)

    code = parse_literal_until(
        parser,
        initial_token,
        1,
    )

    inline_code = InlineCode()

    inline_code.add_child(Text(code))

    return inline_code
