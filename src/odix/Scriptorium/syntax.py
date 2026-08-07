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
    "Section6": {
        Language.LATEX: Syntax(
            r"\subparagraph{",
            "}\n",
        ),
        Language.HTML: Syntax(
            "<h6>",
            "</h6>\n",
        ),
        Language.MARKDOWN: Syntax(
            "###### ",
            "\n\n",
        ),  
    },
    "MathInline": {
        Language.LATEX: Syntax(
            "$",
            "$\n",
        ),
        Language.HTML: Syntax(
            r"\(",
            r"\)",
        ),
        Language.MARKDOWN: Syntax(
            "$",
            "$",
        ),
    },
    "Underline": {
        Language.LATEX: Syntax(
            r"\underline{",
            "}",
        ),
        Language.HTML: Syntax(
            "<u>",
            "</u>",
        ),
        Language.MARKDOWN: Syntax(
            "<u>",
            "</u>",
        ),
    },

    "Strike": {
        Language.LATEX: Syntax(
            r"\sout{",
            "}",
        ),
        Language.HTML: Syntax(
            "<del>",
            "</del>",
        ),
        Language.MARKDOWN: Syntax(
            "~~",
            "~~",
        ),
    },

    "MathBlock": {
        Language.LATEX: Syntax(
            "$$\n",
            "$$\n",
        ),
        Language.HTML: Syntax(
            r"\[",
            r"\]",
        ),
        Language.MARKDOWN: Syntax(
            "$$\n",
            "\n$$",
        ),
    },

    "CodeBlock": {
        Language.LATEX: Syntax(
            r"\begin{verbatim}" "\n",
            "\n" r"\end{verbatim}",
        ),
        Language.HTML: Syntax(
            "<pre><code>",
            "</code></pre>",
        ),
        Language.MARKDOWN: Syntax(
            "```\n",
            "\n```",
        ),
    },

    "Quote": {
        Language.LATEX: Syntax(
            r"\begin{quote}" "\n",
            "\n" r"\end{quote}",
        ),
        Language.HTML: Syntax(
            "<blockquote>",
            "</blockquote>",
        ),
        Language.MARKDOWN: Syntax(
            "> ",
            "",
        ),
    },

    "List": {
        Language.LATEX: Syntax(
            r"\begin{itemize}" "\n",
            "\n" r"\end{itemize}",
        ),
        Language.HTML: Syntax(
            "<ul>",
            "</ul>",
        ),
        Language.MARKDOWN: Syntax("",""),
    },

    "ListItem": {
        Language.LATEX: Syntax(
            r"\item ",
            "",
        ),
        Language.HTML: Syntax(
            "<li>",
            "</li>",
        ),
        Language.MARKDOWN: Syntax(
            "- ",
            "",
        ),
    },

    "Table": {
        Language.LATEX: Syntax(
            r"\begin{tabular}",
            r"\end{tabular}",
        ),
        Language.HTML: Syntax(
            "<table>",
            "</table>",
        ),
        Language.MARKDOWN: Syntax("",""),
    },

    "Row": {
        Language.LATEX: Syntax(
            "",
            r" \\",
        ),
        Language.HTML: Syntax(
            "<tr>",
            "</tr>",
        ),
        Language.MARKDOWN: Syntax("","|"),
    },

    "Cell": {
        Language.LATEX: Syntax(
            "",
            " & ",
        ),
        Language.HTML: Syntax(
            "<td>",
            "</td>",
        ),
        Language.MARKDOWN: Syntax("|",""),
    },

    "Figure": {
        Language.LATEX: Syntax(
            "\\begin{figure}\n",
            "\n\\end{figure}\n",
        ),
        Language.HTML: Syntax(
            "<figure>",
            "</figure>",
        ),
        Language.MARKDOWN: Syntax("",""),
    },

    "Caption": {
        Language.LATEX: Syntax(
            r"\caption{",
            "}",
        ),
        Language.HTML: Syntax(
            "<figcaption>",
            "</figcaption>",
        ),
        Language.MARKDOWN: Syntax("",""),
    },

    "Image": {
        Language.LATEX: Syntax(
            r"\includegraphics{",
            "}",
        ),
        Language.HTML: Syntax(
            "<img src=\"",
            "\">",
        ),
        Language.MARKDOWN: Syntax(
            "![](",
            ")",
        ),
    },

    "Link": {
        Language.LATEX: Syntax(
            r"\url{",
            "}",
        ),
        Language.HTML: Syntax(
            "<a href=\"",
            "\"></a>",
        ),
        Language.MARKDOWN: Syntax(
            "<",
            ">",
        ),
    },

    "Citation": {
        Language.LATEX: Syntax(
            r"\cite{",
            "}",
        ),
        Language.HTML: Syntax(
            "<cite>",
            "</cite>",
        ),
        Language.MARKDOWN: Syntax(
            "[@",
            "]",
        ),
    },

    "Reference": {
        Language.LATEX: Syntax(
            r"\bibitem{",
            "}",
        ),
        Language.HTML: Syntax(
            "<li id=\"",
            "\">",
        ),
        Language.MARKDOWN: Syntax("",""),
    },

    "Bibliography": {
        Language.LATEX: Syntax(
            "\\begin{thebibliography}{}\n",
            "\n\\end{thebibliography}\n",
        ),
        Language.HTML: Syntax(
            "<section class=\"bibliography\">",
            "</section>",
        ),
        Language.MARKDOWN: Syntax("",""),
    },

    "Footnote": {
        Language.LATEX: Syntax(
            r"\footnote{",
            "}",
        ),
        Language.HTML: Syntax(
            "<aside>",
            "</aside>",
        ),
        Language.MARKDOWN: Syntax(
            "[^",
            "]",
        ),
    },

    "PageBreak": {
        Language.LATEX: Syntax(
            r"\newpage",
        ),
        Language.HTML: Syntax(
            "<hr class=\"page-break\">",
        ),
        Language.MARKDOWN: Syntax(
            "\\newpage",
        ),
    },
}