from __future__ import annotations

from enum import Enum, auto


class ReaderType(Enum):
    """Enumeration of token reader types."""

    SINGLE = auto()
    REPEATED = auto()
