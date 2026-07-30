from __future__ import annotations

from dataclasses import dataclass

from .token_type import TokenType


@dataclass(slots=True, frozen=True)
class Token:
    """Represents a lexical token."""

    type: TokenType
    value: str
    line: int
    column: int