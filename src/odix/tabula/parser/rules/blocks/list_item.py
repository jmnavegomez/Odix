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
from ....nodes.list_item import ListItem
from ..inline.sequence import parse_inline_content


def parse_list_item(parser: Parser) -> ListItem:
    """Parses a list item.

    Args:
        parser: Parser instance.

    Returns:
        Parsed list item.
    """

    parser._advance()  # Consume '-' or '+'

    item = ListItem()

    paragraph = parse_inline_content(
        parser,
        TokenType.NEWLINE,
        TokenType.EOF,
    )

    item.add_child(paragraph)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return item
