from __future__ import annotations

from typing import Any

from .node import Node
from .metadata import Metadata


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