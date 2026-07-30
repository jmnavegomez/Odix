from __future__ import annotations

from .block import Block


class CodeBlock(Block):
    """Represents a block of source code."""

    def __init__(self, code: str, language: str | None = None) -> None:
        """
        Initialize a code block.

        Args:
            code: Source code.
            language: Programming language used for syntax highlighting.
        """
        super().__init__()
        self.code = code
        self.language = language