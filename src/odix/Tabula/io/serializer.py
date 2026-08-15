# Odix - Open-source publishing system for technical books
# Copyright (C) 2026 José Manuel Naveiro
#
# This file is part of Odix.
#
# Odix is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# Odix is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Odix. If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

from typing import Any

from ..nodes import Image, MathBlock, MathInline, Node, Reference, Section
from ..visitor import Visitor


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
                "title": (self.visit(node.title) if node.title is not None else None),
            },
            "children": [self.visit(child) for child in node.children],
        }

    def visit_image(self, node: Image):
        return {
            "type": "Image",
            "content": {
                "source": node.source,
            },
            "children": [self.visit(child) for child in node.children],
        }

    def visit_mathblock(self, node: MathBlock):
        return {
            "type": "MathBlock",
            "content": {
                "expression": node.expression,
            },
            "children": [self.visit(child) for child in node.children],
        }

    def visit_mathinline(self, node: MathInline):
        return {
            "type": "MathInline",
            "content": {
                "expression": node.expression,
            },
            "children": [self.visit(child) for child in node.children],
        }

    def visit_reference(self, node: Reference):
        return {
            "type": "Reference",
            "content": {
                "key": node.key,
            },
            "children": [self.visit(child) for child in node.children],
        }
