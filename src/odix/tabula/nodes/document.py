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

from .metadata import Metadata
from .node import Node


class Document(Node):
    """Root node of a Tabula abstract syntax tree.

    A document represents the complete AST. It stores the document
    metadata and contains all top-level block nodes.
    """

    def __init__(self, metadata: Metadata | None = None) -> None:
        """Initializes a document node.

        Args:
            metadata: Document metadata.
        """
        super().__init__()
        self.metadata = metadata

    def content(self) -> tuple[Any, ...]:
        """Returns the semantic content of the document.

        Returns:
            Tuple containing the semantic content of the document metadata.
        """
        if self.metadata is None:
            return ()

        return self.metadata.content()
