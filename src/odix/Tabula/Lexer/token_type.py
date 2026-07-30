from __future__ import annotations

from enum import Enum, auto


class TokenType(Enum):
    """Enumeration of all supported Markdown token types."""

    TEXT = auto()
    NEWLINE = auto()
    EOF = auto()

    HEADING = auto()

    BOLD = auto()
    ITALIC = auto()
    UNDERLINE = auto()
    STRIKE = auto()

    LINK = auto()
    INLINE_CODE = auto()
    CODE_BLOCK = auto()

    QUOTE = auto()

    LIST_MARKER = auto()

    MATH_INLINE = auto()
    MATH_BLOCK = auto()

    IMAGE = auto()

    TABLE_SEPARATOR = auto()

    HORIZONTAL_RULE = auto()
    PAGE_BREAK = auto()

    FOOTNOTE = auto()

    CITATION = auto()