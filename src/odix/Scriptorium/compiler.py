from __future__ import annotations

from ..tabula.nodes import Document

from .language import Language
from .writer import Writer
from .visitors.markup import MarkupVisitor


class Compiler:
    """Compiles a Tabula document into a markup language."""

    def __init__(
        self,
        language: Language,
    ) -> None:
        """Initializes the compiler.

        Args:
            language: Target output language.
        """

        self._writer = Writer(language)
        self._visitor = MarkupVisitor(
            self._writer,
        )

    def compile(
        self,
        document: Document,
    ) -> str:
        """Compiles a document.

        Args:
            document: Document to compile.

        Returns:
            Generated markup.
        """

        return self._visitor.visit(document)