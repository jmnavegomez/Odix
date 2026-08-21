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

from ..lexer.token import Token
from ..lexer.token_type import TokenType
from ..nodes.document import Document
from ..nodes.metadata import Metadata
from ..nodes.node import Node
from ..nodes.section import Section
from .exceptions import ParserError
from .rules.dispatchers.blocks import parse_block


class Parser:
    """Syntactic analyzer for Tabula documents."""

    def __init__(self) -> None:
        """Initializes the parser."""

        self._tokens: list[Token] = []
        self._position = 0
        self._metadata: Metadata | None = None
        self._document: Document | None = None
        self._parents: list[Node] = []

    @property
    def _current(self) -> Token:
        """Returns the current token.

        Returns:
            Current token.
        """
        return self._tokens[self._position]

    def _peek(self, offset: int = 1) -> Token:
        """Returns a look-ahead token.

        Args:
            offset: Number of tokens ahead of the current position.

        Returns:
            Token at the requested position.
        """
        index = min(
            self._position + offset,
            len(self._tokens) - 1,
        )

        return self._tokens[index]

    def _reset(
        self,
        tokens: list[Token],
        metadata: Metadata | None,
    ) -> None:
        """Resets the parser state.

        Args:
            tokens: Token sequence to parse.
            metadata: Document metadata.
        """
        self._tokens = tokens
        self._position = 0
        self._metadata = metadata

    def _advance(self) -> Token:
        """Advances to the next token.

        Returns:
            The token that was consumed.
        """
        token = self._current

        if token.type is not TokenType.EOF:
            self._position += 1

        return token

    def _match(self, *types: TokenType) -> bool:
        """Checks whether the current token matches one of the given types.

        Args:
            *types: Accepted token types.

        Returns:
            ``True`` if the current token matches, ``False`` otherwise.
        """
        return self._current.type in types

    def _expect_token(self, token: Token) -> Token:
        """Consumes the current token if it matches the expected token.

        Args:
            token_type: Expected token.

        Returns:
            Consumed token.

        Raises:
            UnexpectedTokenError: If the current token does not match.
        """
        if not self._current.value == token.value:
            raise ParserError(
                message="Unexpected token", token=self._current, expected_token=token
            )

        return self._advance()

    def _expect_type(self, token_type: TokenType) -> Token:
        """Consumes the current token if it matches the expected type.

        Args:
            token_type: Expected token type.

        Returns:
            Consumed token.

        Raises:
            UnexpectedTokenError: If the current token does not match.
        """
        if not self._match(token_type):
            raise ParserError(
                message=f"Current token type different from {token_type}",
                token=self._current,
                expected_token_type=token_type,
            )

        return self._advance()

    def _insert_section(self, section: Section) -> None:
        """Inserts a section into the document tree.

        Args:
            section: Section to insert.
        """
        while (
            len(self._parents) > 1
            and isinstance(self._parents[-1], Section)
            and self._parents[-1].level >= section.level
        ):
            self._parents.pop()

        self._parents[-1].add_child(section)
        self._parents.append(section)

    def _insert_default(self, node: Node) -> None:
        """Inserts a node using the default strategy.

        Args:
            node: Node to insert.
        """
        self._parents[-1].add_child(node)

    # Node insertion is dispatched according to the node type.
    # Most nodes use the default strategy, while hierarchical nodes
    # (such as sections) override it with a specialized handler.
    def _insert(self, node: Node) -> None:
        """Dispatches node insertion to the corresponding handler.

        Args:
            node: Node to insert.
        """
        method_name = f"_insert_{node.__class__.__name__.lower()}"
        method = getattr(
            self,
            method_name,
            self._insert_default,
        )

        method(node)

    @property
    def current(self) -> Token:
        """Returns the current token"""
        return self._current

    def parse(
        self,
        tokens: list[Token],
        metadata: Metadata | None = None,
    ) -> Document:
        """Parses a token sequence into a Tabula document.

        Args:
            tokens: Tokens produced by the lexer.
            metadata: Document metadata.

        Returns:
            Root document node.
        """
        self._reset(tokens, metadata)

        self._document = Document(metadata)
        self._parents = [self._document]

        while not self._match(TokenType.EOF):

            if self._match(TokenType.NEWLINE):
                self._advance()
                continue

            node = parse_block(self)
            self._insert(node)

        return self._document
