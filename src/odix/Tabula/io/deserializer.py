from __future__ import annotations

from typing import Any

from ..nodes import (
    Bibliography,
    Bold,
    Caption,
    Cell,
    Citation,
    CodeBlock,
    CrossReference,
    Document,
    Figure,
    Footnote,
    Image,
    InlineCode,
    Italic,
    Label,
    Link,
    List,
    ListItem,
    MathBlock,
    MathInline,
    Node,
    PageBreak,
    Paragraph,
    Quote,
    Reference,
    Row,
    Section,
    Strike,
    Table,
    Text,
    Underline,
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
            "CodeBlock": CodeBlock,
            "MathBlock": MathBlock,
            "MathInline": MathInline,
            "Table": Table,
            "Row": Row,
            "Cell": Cell,
            "Image": Image,
            "Figure": Figure,
            "Caption": Caption,
            "Link": Link,
            "Citation": Citation,
            "Reference": Reference,
            "Footnote": Footnote,
            "Bibliography": Bibliography,
            "Label": Label,
            "CrossReference": CrossReference,
            # "HorizontalRule": HorizontalRule,
            "PageBreak": PageBreak,
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
            raise ValueError(f"Unknown node type '{node_type}'.")

        builder = self._special_deserializers.get(node_class)

        if builder is None:
            node = node_class.from_content(
                data["content"],
            )
        else:
            node = builder(data)

        for child in data["children"]:
            node.add_child(self.deserialize(child))

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

    def _deserialize_image(
        self,
        data: dict[str, Any],
    ) -> Image:
        """Deserializes a section node.

        Args:
            data: Serialized section.

        Returns:
            Deserialized section.
        """

        content = data["content"]

        if content["source"] is not None:
            image = Image.from_content(content["source"])

            return image

        return Image("")

    def _deserialize_mathblock(
        self,
        data: dict[str, Any],
    ) -> MathBlock:
        """Deserializes a math block node.

        Args:
            data: Serialized section.

        Returns:
            Deserialized section.
        """

        content = data["content"]

        if content["expression"] is not None:
            math_block = MathBlock.from_content(content["expression"])

            return math_block

        return MathBlock("")

    def _deserialize_mathinline(
        self,
        data: dict[str, Any],
    ) -> MathInline:
        """Deserializes a math inline node.

        Args:
            data: Serialized math inline.

        Returns:
            Deserialized math inline.
        """

        content = data["content"]

        if content["expression"] is not None:
            math_inline = MathInline.from_content(content["expression"])

            return math_inline

        return MathInline("")

    def _deserialize_reference(
        self,
        data: dict[str, Any],
    ) -> Reference:
        """Deserializes a math block node.

        Args:
            data: Serialized section.

        Returns:
            Deserialized section.
        """

        content = data["content"]

        if content["key"] is not None:
            reference = Reference.from_content(content["key"])

            return reference

        return Reference("")
