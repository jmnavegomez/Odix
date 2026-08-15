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

from ...tabula.nodes import (
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

        self._commands: dict[type[Node], str] = {
            Paragraph: "Paragraph",
            Bold: "Bold",
            Italic: "Italic",
            Underline: "Underline",
            Strike: "Strike",
            InlineCode: "InlineCode",
            Quote: "Quote",
            List: "List",
            ListItem: "ListItem",
            Table: "Table",
            Row: "Row",
            Cell: "Cell",
            Figure: "Figure",
            Caption: "Caption",
            Bibliography: "Bibliography",
        }

    def generic_visit(
        self,
        node: Node,
    ) -> str:
        """Visits a node using the default implementation."""

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
        """Visits a document."""

        return self.visit_children(node)

    def visit_section(
        self,
        node: Section,
    ) -> str:
        """Visits a section."""

        title = ""

        if node.title is not None:
            title = self.visit_children(node.title)

        return self._writer.command(
            "Section",
            title,
            level=node.level,
        ) + self.visit_children(node)

    @staticmethod
    def visit_text(
        node: Text,
    ) -> str:
        """Visits a text node."""
        result = node.text

        if not isinstance(node.parent, CodeBlock):
            result = result.replace("_", "\\_")
            result = result.replace("&", "\\&")
            result = result.replace("%", "\\%")
            result = result.replace("|", r"\textbar{}")
            result = result.replace("<", "\\textless{}")
            result = result.replace(">", "\\textgreater{}")
            result = result.replace("~", "\\string~")
            result = result.replace("^", "\\string^")

        return result

    def visit_mathinline(
        self,
        node: MathInline,
    ) -> str:
        """Visits an inline math node."""

        return self._writer.command(
            "MathInline",
            node.expression,
        )

    def visit_codeblock(
        self,
        node: CodeBlock,
    ) -> str:
        """Visits a code block."""

        return self._writer.command(
            "CodeBlock",
            self.visit_children(node),
        )

    def visit_image(
        self,
        node: Image,
    ) -> str:
        """Visits an image."""

        return self._writer.command(
            "Image",
            node.source,
        )

    def visit_link(
        self,
        node: Link,
    ) -> str:
        """Visits a hyperlink."""

        return self._writer.command(
            "Link",
            node.target,
        )

    def visit_reference(
        self,
        node: Reference,
    ) -> str:
        """Visits a bibliography reference."""

        return self._writer.command(
            "Reference",
            node.key,
        ) + self.visit_children(node)

    def visit_crossreference(
        self,
        node: CrossReference,
    ) -> str:
        """Visits a cross reference."""

        return self._writer.command(
            "CrossReference",
            node.key,
        )

    def visit_label(
        self,
        node: Label,
    ) -> str:
        """Visits a label."""

        return self._writer.command(
            "Label",
            node.key,
        )

    def visit_footnote(
        self,
        node: Footnote,
    ) -> str:
        """Visits a footnote."""

        return self._writer.command(
            "Reference",
            node.key,
        ) + self.visit_children(node)

    def visit_mathblock(
        self,
        node: MathBlock,
    ) -> str:
        label = next(
            (child for child in node.children if isinstance(child, Label)),
            None,
        )
        label_markup = self.visit(label) if label is not None else ""

        return self._writer.command_mathblock(
            node.expression,
            label=label_markup,
        )

    def visit_citation(
        self,
        node: Citation,
    ) -> str:
        """Visits a bibliography citation."""

        return self._writer.command(
            "Citation",
            node.key,
        )

    def visit_pagebreak(
        self,
        node: PageBreak,
    ) -> str:
        """Visits a page break."""

        return self._writer.command(
            "PageBreak",
        )

    def visit_table(
        self,
        node: Table,
    ) -> str:
        """Visits a table."""

        rows = [child for child in node.children if isinstance(child, Row)]

        if not rows:
            return ""

        caption = next(
            (child for child in node.children if isinstance(child, Caption)),
            None,
        )

        label = next(
            (child for child in node.children if isinstance(child, Label)),
            None,
        )
        caption_markup = self.visit(caption) if caption is not None else ""

        label_markup = self.visit(label) if label is not None else ""
        columns = len(rows[0].children)
        structure = "l" * columns

        content = []

        for row in rows:
            cells = [self.visit(cell).replace("\n", "") for cell in row.children]

            cells[0] = cells[0][3:]

            content.append("".join(cells) + r" \\")

        table = self._writer.command_table(
            "\n".join(content),
            structure=structure,
            caption=caption_markup,
            label=label_markup,
        )

        return table

    def visit_figure(
        self,
        node: Figure,
    ) -> str:
        """Visits a figure."""

        if not node.children:
            return ""

        content = self.visit_children(node)

        return self._writer.command_figure(
            content,
        )
