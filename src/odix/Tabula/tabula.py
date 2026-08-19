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
        path: Path | None = None,
        document: Document | None = None,
    ) -> None:
        """Initializes a Tabula document.

        Args:
            path: Source or serialized Tabula file path.
            document: Existing document loaded from disk.

        Raises:
            TypeError: If ``document`` is not a Document.
            ValueError: If neither ``path`` nor ``document`` is provided.
        """
        self._path = path

        if document is not None:
            if not isinstance(document, Document):
                raise TypeError("The root node must be a Document.")

            self._ast = document
            return

        if path is None:
            raise ValueError(
                "Either 'path' or 'document' must be provided."
            )

        self._ast = self._parse(
            path.read_text(encoding="utf-8"),
        )

    @classmethod
    def from_content(cls, content: str) -> Tabula:
        instance = cls.__new__(cls)
        instance._path = None
        instance._ast = cls._parse(content)
        return instance

    @classmethod
    def from_file(cls, path: str | Path) -> Tabula:
        path = Path(path)

        instance = cls.__new__(cls)
        instance._path = path
        instance._ast = cls._parse(
            path.read_text(encoding="utf-8"),
        )

        return instance
    
    @staticmethod
    def _parse(
        content: str,
    ) -> Document:
        """Parses Markdown content into a Document AST."""

        lexer = Lexer()
        parser = Parser()

        tokens = lexer.tokenize(content)
        document = parser.parse(tokens)

        if not isinstance(document, Document):
            raise TypeError("The root node must be a Document.")

        return document

    def _set_path(
        self,
        path: Path,
    ) -> Tabula:
        """Sets the source path and returns this instance."""
        self._path = path
        return self

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