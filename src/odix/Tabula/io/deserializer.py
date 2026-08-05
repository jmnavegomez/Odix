from __future__ import annotations

from typing import Any

from ..nodes import (
    Node,
    Document,
    Paragraph,
    Section,
    Text,
    Bold,
    Italic,
    InlineCode,
    Underline,
    Strike,
    List,
    ListItem,
    Quote,
)


class Deserializer:
    """Deserializes a Python dictionary into a Tabula AST."""

    def __init__(self) -> None:
        """Initializes the deserializer."""

        self._node_types: dict[str, type[Node]] = {
                    "Document": Document,
                    "Paragraph": Paragraph,
                    "Section": Section,

                    "Text": Text,
                    "Bold": Bold,
                    "Italic": Italic,
                    "Underline": Underline,
                    "Strike": Strike,
                    "InlineCode": InlineCode,

                    "List": List,
                    "ListItem": ListItem,
                    "Quote": Quote,

                    # "CodeBlock": CodeBlock,
                    # "MathBlock": MathBlock,

                    # "Table": Table,
                    # "Row": Row,
                    # "Cell": Cell,

                    # "Image": Image,
                    # "Figure": Figure,
                    # "Caption": Caption,

                    # "Link": Link,
                    # "Citation": Citation,
                    # "Reference": Reference,
                    # "Footnote": Footnote,
                    # "Bibliography": Bibliography,

                    # "HorizontalRule": HorizontalRule,
                    # "PageBreak": PageBreak,
        }

        self._special_deserializers = {
            Section: self._deserialize_section,
        }

    def deserialize(
        self,
        data: dict[str, Any],
    ) -> Node:
        """Deserializes a node.

        Args:
            data: Serialized node.

        Returns:
            Deserialized node.

        Raises:
            ValueError: If the node type is unknown.
        """

        node_type = data["type"]

        try:
            node_class = self._node_types[node_type]
        except KeyError:
            raise ValueError(
                f"Unknown node type '{node_type}'."
            )

        builder = self._special_deserializers.get(node_class)

        if builder is None:
            node = node_class.from_content(
                data["content"],
            )
        else:
            node = builder(data)

        for child in data["children"]:
            node.add_child(
                self.deserialize(child)
            )

        return node

    def _deserialize_section(
        self,
        data: dict[str, Any],
    ) -> Section:
        """Deserializes a section node.

        Args:
            data: Serialized section.

        Returns:
            Deserialized section.
        """

        content = data["content"]

        section = Section.from_content(content)

        if content["title"] is not None:
            section.title = self.deserialize(
                content["title"],
            )

        return section