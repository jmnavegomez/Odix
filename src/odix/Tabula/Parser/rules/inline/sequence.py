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
from ....nodes.paragraph import Paragraph
from ...exceptions import ParserError


def parse_inline_content(
    parser: Parser,
    *terminators: TokenType,
) -> Paragraph:
    """Parses a sequence of inline elements.

    Parsing stops when one of the terminating token types is reached.

    Args:
        parser: Parser instance.
        *terminators: Token types that terminate the sequence.

    Returns:
        Paragraph containing the parsed inline nodes.
    """

    from ..dispatchers.inline import parse_inline

    paragraph = Paragraph()

    while not parser._match(*terminators):

        inline = parse_inline(parser)

        # parse_inline() should never return None when no
        # stop delimiter has been provided.
        assert inline is not None

        paragraph.add_child(inline)

    return paragraph


def parse_literal_until(
    parser: Parser,
    closing_type: TokenType,
    closing_length: int,
) -> str:
    """Parses literal text until a closing delimiter is found.

    Unlike ``parse_inline_content()``, this function does not parse nested
    inline elements. Every token between the delimiters is treated as plain
    text.

    Args:
        parser: Parser instance.
        closing_type: Token type that closes the literal sequence.
        closing_length: Required delimiter length.

    Returns:
        Literal text between the delimiters.

    Raises:
        ParserError: If the closing delimiter is not found.
    """
    value = ""

    while not parser._match(TokenType.EOF):

        if parser._match(closing_type) and len(parser._current.value) == closing_length:
            break

        value += parser._advance().value

    if parser._match(TokenType.EOF):
        raise ParserError("Unterminated literal block.")

    if len(parser._current.value) != closing_length:
        raise ParserError("Invalid closing delimiter.")

    parser._advance()

    return value


def parse_literal_content(
    parser: Parser,
    *terminators: TokenType,
) -> str:
    """Parses a sequence of literal tokens.

    Unlike ``parse_inline_content()``, no inline parsing is performed.

    Args:
        parser: Parser instance.
        *terminators: Token types that terminate the sequence.

    Returns:
        Literal text.
    """
    value = ""

    while not parser._match(*terminators):
        value += parser._advance().value

    return value
