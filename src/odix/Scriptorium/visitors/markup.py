from __future__ import annotations

from ...tabula.nodes import (
    Node,
    Document,
    Paragraph,
    Section,
    Text,
    Bold,
    Italic,
    InlineCode,
    MathInline,
    Underline,
    Strike,
    List,
    ListItem,
    Quote,
    Row,
    Cell,
    Table,
    CodeBlock,
    MathBlock,
    PageBreak,
    Image,
    Caption,
    Reference,
    Bibliography,
    Figure,
    Link,
    Footnote,
    Citation,
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

        return (
            self._writer.command(
                "Section",
                title,
                level=node.level,
            )
            + self.visit_children(node)
        )

    @staticmethod
    def visit_text(
        node: Text,
    ) -> str:
        """Visits a text node."""
        result = node.text

        if (not isinstance(node.parent,CodeBlock)): 
            result = result.replace("_","\\_")
            result = result.replace("&","\\&")
            result = result.replace("%","\\%")
            result = result.replace("|","\\textbar{}")
            result = result.replace("<","\\textless{}")
            result = result.replace(">","\\textgreater{}")
            result = result.replace("~","\\string~")
            result = result.replace("^","\\string^")

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

    def visit_mathblock(
        self,
        node: MathBlock,
    ) -> str:
        """Visits a math block."""

        return self._writer.command(
                "MathBlock",
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

        return (
            self._writer.command(
                "Reference",
                node.key,
            )
            + self.visit_children(node)
        )

    def visit_footnote(
        self,
        node: Footnote,
    ) -> str:
        """Visits a footnote."""

        return (self._writer.command(
                    "Reference",
                    node.key,
                    )
                    + self.visit_children(node)
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

        if not node.children:
            return ""

        columns = len(
            node.children[0].children
        )

        structure = "l" * columns

        rows = []

        for row in node.children:
            cells = [
                self.visit(cell).replace("\n","")
                for cell in row.children
            ]

            cells[0] = cells[0][3:]

            rows.append(
                "".join(cells)
                + r" \\"
            )


        return self._writer.command_table(
            "\n".join(rows),
            structure=structure,
        )

    def visit_figure(
            self,
            node: Figure,
        ) -> str:
            """Visits a Figure."""
    
            if not node.children:
                return ""
    
            image = self.visit(node.children[0])

            caption = self.visit(node.children[1])

            return self._writer.command_figure(
                "".join(image+"\n"+caption),
            )