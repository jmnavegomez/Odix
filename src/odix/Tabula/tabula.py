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

import json
from pathlib import Path

from .io.deserializer import Deserializer
from .io.serializer import Serializer
from .lexer import Lexer
from .nodes import Document, Node
from .parser import Parser


class Tabula:
    """Public interface for creating, saving and loading Tabula ASTs."""

    def __init__(
        self,
        path: str | Path,
        document: Document | None = None,
    ) -> None:
        """Initializes a Tabula document.

        Args:
            path: Markdown source file or serialized Tabula document.
            document: Existing document loaded from disk.

        Raises:
            TypeError: If ``document`` is not a Document.
        """

        self._path = Path(path)

        if document is not None:
            self._ast = document
            return

        lexer = Lexer()
        parser = Parser()

        markdown = self._path.read_text(
            encoding="utf-8",
        )

        tokens = lexer.tokenize(markdown)

        self._ast = parser.parse(tokens)

        if not isinstance(self._ast, Document):
            raise TypeError("The root node must be a Document.")

    @property
    def ast(self) -> Node:
        """Returns the AST."""

        return self._ast

    @property
    def path(self) -> Path | None:
        """Returns the source path."""

        return self._path

    def save(
        self,
        path: str | Path,
    ) -> None:
        """Saves the AST."""

        serializer = Serializer()

        data = serializer.visit(self._ast)

        Path(path).write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    @classmethod
    def load(
        cls,
        path: str | Path,
    ) -> Tabula:
        """Loads a serialized Tabula document."""

        path = Path(path)

        data = json.loads(
            path.read_text(
                encoding="utf-8",
            )
        )

        document = Deserializer().deserialize(data)

        if not isinstance(document, Document):
            raise TypeError("The root node must be a Document.")

        return cls(
            path=path,
            document=document,
        )
