from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.inline import Inline
from ..inline.asterisk import parse_asterisk
from ..inline.bold import parse_bold
from ..inline.citation import parse_citation
from ..inline.colon import parse_colon
from ..inline.cross_reference import parse_cross_reference
from ..inline.hyphen import parse_hyphen
from ..inline.inline_code import parse_inline_code
from ..inline.italic import parse_italic
from ..inline.math import parse_math_inline
from ..inline.module import parse_module
from ..inline.plus import parse_plus
from ..inline.strike import parse_strike
from ..inline.text import parse_text
from ..inline.underline import parse_underline
from ..inline.underscore import parse_underscore


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

    # Citation (··key··)
    if (
        parser._match(TokenType.MIDDLE_DOT)
        and len(parser._current.value) == 2
    ):
        return parse_citation(parser)

    # Italic(·text·)
    if (
        parser._match(TokenType.MIDDLE_DOT)
        and len(parser._current.value) == 1
    ):
        return parse_italic(parser)

    # Underline(___text___)
    if (
        parser._match(TokenType.UNDERSCORE)
        and len(parser._current.value) == 3
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

    # Inline math ($...$)
    if (
        parser._match(TokenType.DOLLAR)
        and len(parser._current.value) == 2
    ):
        return parse_cross_reference(parser)
    
    # Inline math ($...$)
    if (
        parser._match(TokenType.DOLLAR)
        and len(parser._current.value) == 1
    ):
        return parse_math_inline(parser)

    # Plain text
    if parser._match(TokenType.TEXT):
        return parse_text(parser)

    # Inline asterisk
    if parser._match(TokenType.ASTERISK):
        return parse_asterisk(parser)
    
    # Inline colon
    if (
        parser._match(TokenType.COLON)
    ):
        return parse_colon(parser)

    # Inline underscore
    if (
        parser._match(TokenType.UNDERSCORE)
    ):
        return parse_underscore(parser)

    # Inline underscore
    if (
        parser._match(TokenType.HYPHEN)
    ):
        return parse_hyphen(parser)
    
    # Inline plus
    if (
        parser._match(TokenType.PLUS)
    ):
        return parse_plus(parser)

    # Inline module
    if (
        parser._match(TokenType.MODULE)
    ):  
        value = parse_module(parser)
        return value
    
    raise NotImplementedError(
        f"Unsupported inline token "
        f"{parser._current.type.name}."
    )
