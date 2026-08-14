from __future__ import annotations

from ..tabula.nodes import Node


class Visitor:
    """Base visitor for Tabula AST nodes."""

    def visit(
        self,
        node: Node,
    ) -> str:
        """Visits a node.

        Args:
            node: Node to visit.

        Returns:
            Generated output.
        """

        method_name = f"visit_{node.__class__.__name__.lower()}"

        visitor = getattr(
            self,
            method_name,
            self.generic_visit,
        )

        return visitor(node)

    def generic_visit(
        self,
        node: Node,
    ) -> str:
        """Visits a node using the default implementation.

        Args:
            node: Node to visit.

        Returns:
            Generated output.
        """

        return self.visit_children(node)

    def visit_children(
        self,
        node: Node,
    ) -> str:
        """Visits all children of a node.

        Args:
            node: Parent node.

        Returns:
            Concatenated output of all children.
        """

        return "".join(self.visit(child) for child in node.children)
