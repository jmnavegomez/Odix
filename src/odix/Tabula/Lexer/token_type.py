from __future__ import annotations

from enum import Enum, auto


class TokenType(Enum):
    """Enumeration of lexical token types."""

    TEXT = auto()
    NEWLINE = auto()

    HASH = auto()
    ASTERISK = auto()
    UNDERSCORE = auto()
    BACKTICK = auto()
    DOLLAR = auto()

    GREATER_THAN = auto()

    HYPHEN = auto()
    PLUS = auto()
    PIPE = auto()

    LBRACKET = auto()
    RBRACKET = auto()

    LPAREN = auto()
    RPAREN = auto()

    EXCLAMATION = auto()

    EOF = auto()