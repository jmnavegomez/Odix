from __future__ import annotations

from typing import Any

from .nodes import Node


class Visitor:
    """Base class for visitors over a Tabula AST.

    A visitor traverses an AST and performs operations on its nodes.
    Dispatch is based on the node class name. For example, a ``Section``
    node is handled by a method named ``visit_section``.

    Subclasses should implement ``visit_<node_name>()`` methods for the
    node types they are interested in. Nodes without a dedicated method
    are handled by ``generic_visit()``.
    """

    def visit(self, node: Node) -> Any:
        """Visits a node.

        Dispatches to the corresponding ``visit_<node_name>()`` method if
        it exists. Otherwise, falls back to ``generic_visit()``.

        Args:
            node: Node to visit.

        Returns:
            Value returned by the visitor method.
        """
        method_name = f"visit_{node.__class__.__name__.lower()}"
        visitor = getattr(self, method_name, self.generic_visit)

        return visitor(node)

    def generic_visit(self, node: Node) -> Any:
        """Visits all child nodes.

        This default implementation recursively visits every child of the
        given node and returns their results.

        Args:
            node: Node whose children will be visited.

        Returns:
            Any containing the result of visiting each child.
        """
        return [self.visit(child) for child in node.children]