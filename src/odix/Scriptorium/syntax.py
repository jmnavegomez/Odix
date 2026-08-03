from __future__ import annotations

from dataclasses import dataclass

from .language import Language


@dataclass(frozen=True)
class Syntax:
    """Represents the syntax of a markup construct."""

    opening: str
    closing: str = ""


SYNTAX: dict[str, dict[Language, Syntax]] = {

    "Bold": {
        Language.LATEX: Syntax(
            r"\textbf{",
            "}",
        ),
        Language.HTML: Syntax(
            "<b>",
            "</b>",
        ),
        Language.MARKDOWN: Syntax(
            "**",
            "**",
        ),
    },

    "Italic": {
        Language.LATEX: Syntax(
            r"\textit{",
            "}",
        ),
        Language.HTML: Syntax(
            "<i>",
            "</i>",
        ),
        Language.MARKDOWN: Syntax(
            "*",
            "*",
        ),
    },

    "InlineCode": {
        Language.LATEX: Syntax(
            r"\texttt{",
            "}",
        ),
        Language.HTML: Syntax(
            "<code>",
            "</code>",
        ),
        Language.MARKDOWN: Syntax(
            "`",
            "`",
        ),
    },

    "Paragraph": {
        Language.LATEX: Syntax(
            "",
            "\n\n",
        ),
        Language.HTML: Syntax(
            "<p>",
            "</p>\n",
        ),
        Language.MARKDOWN: Syntax(
            "",
            "\n\n",
        ),
    },

    "Section1": {
        Language.LATEX: Syntax(
            r"\section{",
            "}\n\n",
        ),
        Language.HTML: Syntax(
            "<h1>",
            "</h1>\n",
        ),
        Language.MARKDOWN: Syntax(
            "# ",
            "\n\n",
        ),
    },

    "Section2": {
        Language.LATEX: Syntax(
            r"\subsection{",
            "}\n\n",
        ),
        Language.HTML: Syntax(
            "<h2>",
            "</h2>\n",
        ),
        Language.MARKDOWN: Syntax(
            "## ",
            "\n\n",
        ),
    },

    "Section3": {
        Language.LATEX: Syntax(
            r"\subsubsection{",
            "}\n\n",
        ),
        Language.HTML: Syntax(
            "<h3>",
            "</h3>\n",
        ),
        Language.MARKDOWN: Syntax(
            "### ",
            "\n\n",
        ),
    },

    "Section4": {
        Language.LATEX: Syntax(
            r"\paragraph{",
            "}\n",
        ),
        Language.HTML: Syntax(
            "<h4>",
            "</h4>\n",
        ),
        Language.MARKDOWN: Syntax(
            "#### ",
            "\n\n",
        ),
    },

    "Section5": {
        Language.LATEX: Syntax(
            r"\subparagraph{",
            "}\n",
        ),
        Language.HTML: Syntax(
            "<h5>",
            "</h5>\n",
        ),
        Language.MARKDOWN: Syntax(
            "##### ",
            "\n\n",
        ),
    },

}