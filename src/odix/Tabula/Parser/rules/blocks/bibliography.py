from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType
from ..inline.sequence import parse_literal_until

from ....nodes.bibliography import Bibliography
from ....nodes.reference import Reference

def parse_bibliography(parser: Parser) -> Bibliography:
    """Parses a bibliography block.

    Expected syntax::

        ::bibliography
        ...
        ::

    Args:
        parser: Parser instance.

    Returns:
        Parsed bibliography.
    """

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    bibliography = Bibliography()

    while not (
        parser._match(TokenType.COLON)
        and len(parser._current.value) == 2
    ):
        bibliography.add_child(Reference(parse_literal_until(parser,TokenType.NEWLINE,1)))

    parser._expect(TokenType.COLON)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return bibliography