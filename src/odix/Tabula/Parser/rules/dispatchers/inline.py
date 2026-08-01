from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.inline import Inline

from ..inline.bold import parse_bold
from ..inline.italic import parse_italic
from ..inline.underline import parse_underline
from ..inline.strike import parse_strike
from ..inline.text import parse_text

from ..inline.inline_code import parse_inline_code


def parse_inline(
    parser: Parser,
    stop_type: TokenType | None = None,
    stop_length: int | None = None,
) -> Inline | None:
    """Parses the next inline element.

    Args:
        parser: Parser instance.

    Returns:
        Parsed inline node.

        Returns ``None`` when the closing delimiter specified by
        ``stop_type`` and ``stop_length`` is reached.

    Raises:
        NotImplementedError: If the inline element is not implemented.
    """
    if (
        stop_type is not None
        and parser._match(stop_type)
        and len(parser._current.value) == stop_length
    ):
        return None

    # Bold (**text**)
    if (
        parser._match(TokenType.ASTERISK)
        and len(parser._current.value) == 2
    ):
        return parse_bold(parser)

    # Italic(*text*)
    if (
        parser._match(TokenType.ASTERISK)
        and len(parser._current.value) == 1
    ):
        return parse_italic(parser)

    # Underline(__text__)
    if (
        parser._match(TokenType.UNDERSCORE)
        and len(parser._current.value) == 2
    ):
        return parse_underline(parser)

    # Strike(--text--)
    if (
        parser._match(TokenType.HYPHEN)
        and len(parser._current.value) == 2
    ):
        return parse_strike(parser)

    # Inline code (`code`)
    if (
        parser._match(TokenType.BACKTICK)
        and len(parser._current.value) == 1
    ):
        return parse_inline_code(parser)

    # Plain text
    if parser._match(TokenType.TEXT):
        return parse_text(parser)

    raise NotImplementedError(
        f"Unsupported inline token "
        f"{parser._current.type.name}."
    )