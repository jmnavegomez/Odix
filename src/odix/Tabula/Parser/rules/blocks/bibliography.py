from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...parser import Parser

from ....lexer.token_type import TokenType

from ....nodes.bibliography import Bibliography

from ..dispatchers.blocks import parse_block

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
        bibliography.add_child(parse_block(parser))

    parser._expect(TokenType.COLON)

    if parser._match(TokenType.NEWLINE):
        parser._advance()

    return bibliography