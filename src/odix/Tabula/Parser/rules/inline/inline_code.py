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

    parser._expect(TokenType.BACKTICK)

    code = parse_literal_until(
        parser,
        TokenType.BACKTICK,
        1,
    )

    inline_code = InlineCode()

    inline_code.add_child(
        Text(code)
    )

    return inline_code