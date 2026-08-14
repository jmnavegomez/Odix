from __future__ import annotations

from dataclasses import dataclass

from .reader_type import ReaderType
from .token_type import TokenType


@dataclass(frozen=True, slots=True)
class Reader:
    """Configuration for a token reader."""

    reader_type: ReaderType
    token_type: TokenType
