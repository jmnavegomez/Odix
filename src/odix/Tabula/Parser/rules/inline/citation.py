from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ....nodes.citation import Citation
from .sequence import parse_literal_until


def parse_citation(parser: Parser) -> Citation:
    """Parses a bibliography citation.

    Expected syntax::

        ··smith2025··

    Args:
        parser: Parser instance.

    Returns:
        Parsed citation.
    """

    parser._expect(TokenType.MIDDLE_DOT)

    key = parse_literal_until(
        parser,
        TokenType.MIDDLE_DOT,
        2,
    ).strip()

    return Citation(key)