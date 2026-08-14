from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

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

_DIRECTIVE_PARSERS: dict[str, Callable[[Parser], Block]] = {
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

    parser._expect(TokenType.COLON)

    name = parser._expect(
        TokenType.TEXT
    ).value.strip().lower()

    method = _DIRECTIVE_PARSERS.get(name)

    if method is None:
        raise NotImplementedError(
            f"Unknown directive: {name}"
        )

    return method(parser)