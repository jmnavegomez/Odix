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
