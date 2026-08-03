from __future__ import annotations

from enum import Enum


class Language(Enum):
    """Supported output languages."""

    LATEX = "latex"
    HTML = "html"
    MARKDOWN = "markdown"