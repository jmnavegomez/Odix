from __future__ import annotations

from typing import Any

from ..visitor import Visitor
from ..nodes import Node
from ..nodes import Section
from ..nodes import Image


class Serializer(Visitor):
    """Serializes a Tabula AST into a Python dictionary.

    The resulting dictionary contains only the semantic information
    required to reconstruct the AST. Derived attributes such as
    ``parent``, ``path`` or hashes are intentionally omitted.
    """

    def generic_visit(self, node: Node) -> dict[str, Any]:
        """Serializes a node and its subtree.

        Args:
            node: Node to serialize.

        Returns:
            Dictionary representing the node.
        """
        
        return {
            "type": node.__class__.__name__,
            "content": node.content(),
            "children": [self.visit(child) for child in node.children],
        }

    def visit_section(self, node: Section):
        return {
            "type": "Section",
            "content": {
                "level": node.level,
                "title": (
                    self.visit(node.title)
                    if node.title is not None
                    else None
                ),
            },
            "children": [
                self.visit(child)
                for child in node.children
            ],
        }

    def visit_image(self, node: Image):
            return {
                "type": "Image",
                "content": {
                    "source": node.source,
                },
                "children": [
                    self.visit(child)
                    for child in node.children
                ],
            }