from __future__ import annotations

from pathlib import Path

from odix.ordinatio import Book, Chapter, Principium
from ..scriptorium import Compiler
from ..scriptorium import Language
from ..tabula import Tabula
from ..typus import Typus


class Impressio:
    """Publishes an Odix book as a LaTeX document."""

    def __init__(
        self,
        book: Book,
        typus: Typus,
    ) -> None:
        self._book = book
        self._typus = typus

        self._FONTS = {
            "computer-modern": None,
            "palatino": "mathpazo",
            "helvetica": "helvet",
            "times": "mathptmx",
        }

    @property
    def book(self) -> Book:
        """Returns the book to publish."""
        return self._book

    @property
    def typus(self) -> Typus:
        """Returns the publication style."""
        return self._typus

    def _render_principium(
        self,
        principium: Principium,
    ) -> str:
        """Renders a principium as LaTeX."""

        tabula = Tabula(principium.source)

        compiler = Compiler(
            Language.LATEX,
        )

        return compiler.compile(
            tabula.ast,
        )

    def _render_chapter(
        self,
        chapter: Chapter,
    ) -> str:
        """Renders a chapter and its principia as LaTeX."""

        parts = [
            rf"\chapter{{{chapter.title}}}",
            "",
        ]

        for principium in chapter.principia:
            parts.append(
                self._render_principium(principium)
            )

        return "\n".join(parts)

    def _render_body(self) -> str:
        """Renders the complete body of the book."""

        chapters = [
            self._render_chapter(chapter)
            for chapter in self._book.chapters
        ]

        return "\n\n".join(chapters)

    def _render_preamble(self) -> str:
        """Renders the LaTeX preamble from Typus."""

        document = self._typus.document
        margins = document.margins
        language = document.language

        options = [
            document.font_size,
            document.page_size,
        ]

        if document.orientation != "portrait":
            options.append(document.orientation)

        if document.twoside:
            options.append("twoside")

        document_class = (
            rf"\documentclass[{','.join(options)}]"
            rf"{{{document.document_class}}}"
        )

        packages = "\n".join(
            rf"\usepackage{{{package}}}"
            for package in document.packages
        )

        font_package = self._FONTS[document.font]

        if font_package is not None:
            packages += "\n" + rf"\usepackage{{{font_package}}}"

        geometry = (
            f"\\usepackage["
            f"top={margins.top},"
            f"bottom={margins.bottom},"
            f"left={margins.left},"
            f"right={margins.right}"
            f"]{{geometry}}"
        )

        babel = rf"\usepackage[{language}]{{babel}}"

        style = "\n".join(
            [
                r"\setcounter{secnumdepth}{1}",
                r"\setstretch{1.25}",
                "",
                r"\definecolor{chaptercolor}{HTML}{24527A}",
                r"\definecolor{primary}{HTML}{24527A}",
                r"\definecolor{secondary}{HTML}{4F81A1}",
                r"\definecolor{codebg}{HTML}{F4F6F8}",
                "",
                r"\titleformat{\chapter}",
                r"  {\Huge\bfseries\color{chaptercolor}}",
                r"  {\thechapter}",
                r"  {1em}",
                r"  {}",
            ]
        )

        return "\n".join(
            [
                document_class,
                "",
                packages,
                geometry,
                babel,
                "",
                style,
            ]
        )

    def _render_document(self) -> str:
        """Renders the complete LaTeX document."""

        document = self._typus.document

        preamble = self._render_preamble()
        
        if document.chapters_table_of_contents:
            table_of_contents = "\n" + "\\setcounter{tocdepth}{1}"
            table_of_contents += "\n" + rf"\tableofcontents"
        else:
            table_of_contents = ""

        body = self._render_body()

        return "\n".join(
            [
                preamble,
                "",
                r"\begin{document}",
                "",
                table_of_contents,
                body,
                "",
                r"\end{document}",
                "",
            ]
        )

    def publish(
        self,
        path: str | Path,
    ) -> None:
        """Publishes the book to a LaTeX file."""

        path = Path(path)

        latex = self._render_document()

        path.write_text(
            latex,
            encoding="utf-8",
        )