from __future__ import annotations

from enum import Enum, auto


class TokenType(Enum):
    """Enumeration of lexical token types."""

    TEXT = auto()
    NEWLINE = auto()

    HASH = auto()
    ASTERISK = auto()
    MIDDLE_DOT = auto()      # ·Nuevo·
    UNDERSCORE = auto()
    BACKTICK = auto()
    DOLLAR = auto()
    COLON = auto()

    GREATER_THAN = auto()
    LESS_THAN = auto()

    HYPHEN = auto()
    PLUS = auto()
    PIPE = auto()
    MODULE = auto()      # %Nuevo%
    AMPERSAND = auto()   # &Nuevo&
    CARET = auto()   # ^Nuevo^
    TILDE = auto()   # ~Nuevo~

    LBRACKET = auto()
    RBRACKET = auto()

    LPAREN = auto()
    RPAREN = auto()

    EXCLAMATION = auto()

    EOF = auto()