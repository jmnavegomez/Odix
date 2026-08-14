from __future__ import annotations

from typing import Any

from .block import Block


class CodeBlock(Block):
    """Represents a block of source code."""

    def __init__(
        self,
        language: str | None = None,
    ) -> None:
        """Initialize a code block.

        Args:
            language: Programming language used for syntax highlighting.
        """
        super().__init__()

        self.language = language

    def content(self) -> tuple[Any, ...]:
        """Returns the semantic content.

        Returns:
            Tuple containing the programming language.
        """
        return (self.language,)

    @classmethod
    def from_content(
        cls,
        content: tuple[str | None],
    ) -> CodeBlock:
        """Creates a code block from serialized content.

        Args:
            content: Serialized semantic content.

        Returns:
            Deserialized code block.
        """
        return cls(content[0])
