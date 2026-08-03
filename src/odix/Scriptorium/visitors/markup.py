from __future__ import annotations

from ...tabula.nodes import (
    Node,
    Document,
    Paragraph,
    Section,
    Text,
    Bold,
    Italic,
    InlineCode,
)

from ..visitor import Visitor
from ..writer import Writer


class MarkupVisitor(Visitor):
    """Generates markup from a Tabula AST."""

    def __init__(
        self,
        writer: Writer,
    ) -> None:
        """Initializes the visitor.

        Args:
            writer: Markup writer.
        """

        super().__init__()

        self._writer = writer

        self._commands: dict[
            type[Node],
            str,
        ] = {
            Paragraph: "Paragraph",
            Bold: "Bold",
            Italic: "Italic",
            InlineCode: "InlineCode",
        }

    def generic_visit(
        self,
        node: Node,
    ) -> str:
        """Visits a node using the default implementation.

        Args:
            node: Node to visit.

        Returns:
            Generated markup.
        """

        command = self._commands.get(type(node))

        if command is None:
            return self.visit_children(node)

        return self._writer.command(
            command,
            self.visit_children(node),
        )

    def visit_document(
        self,
        node: Document,
    ) -> str:
        """Visits a document.

        Args:
            node: Document node.

        Returns:
            Generated markup.
        """

        return self.visit_children(node)

    def visit_section(
        self,
        node: Section,
    ) -> str:
        """Visits a section.

        Args:
            node: Section node.

        Returns:
            Generated markup.
        """

        title = ""

        if node.title is not None:
            title = self.visit(node.title)

        return (
            self._writer.command(
                "Section",
                title,
                level=node.level,
            )
            + self.visit_children(node)
        )

    @staticmethod
    def visit_text(
        node: Text,
    ) -> str:
        """Visits a text node.

        Args:
            node: Text node.

        Returns:
            Text content.
        """

        return node.text