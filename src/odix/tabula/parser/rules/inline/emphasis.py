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
from ....nodes.inline import Inline
from ...exceptions import ParserError


def parse_inline_emphasis(
    parser: Parser,
    node: Inline,
    initial_token: Token,
    closing_length: int,
) -> None:
    """Parses inline content until a closing delimiter is found.

    Parsed inline nodes are attached directly to ``node``.

    Args:
        parser: Parser instance.
        node: Inline node that will receive the parsed children.
        closing_type: Token type that closes the inline element.
        closing_length: Required delimiter length.

    Raises:
        ParserError: If the closing delimiter is not found.
    """
    # Local import to avoid circular imports.
    from ..dispatchers.inline import parse_inline

    # Parse nested inline elements until the closing delimiter
    # of the current emphasis node is reached.

    closing_type = initial_token.type

    while not parser._match(TokenType.EOF):

        inline = parse_inline(
            parser,
            stop_token=initial_token,
            stop_type=closing_type,
            stop_length=closing_length,
        )

        # The closing delimiter belongs to this node.
        if inline is None:
            break

        node.add_child(inline)

    # Reaching EOF means that the emphasis was never closed.
    if parser._match(TokenType.EOF):
        raise ParserError(
            message="Unterminated inline element.",
            token=parser.current,
            expected_token=initial_token,
        )

    # Consume the closing delimiter.
    parser._expect_type(closing_type)
