from __future__ import annotations

from ..nodes.document import Document
from ..nodes.metadata import Metadata
from ..lexer.token import Token
from ..lexer.token_type import TokenType

from .rules.dispatchers.blocks import parse_block

class Parser:
    """Syntactic analyzer for Tabula documents."""

    def __init__(self) -> None:
        """Initializes the parser."""

        self._tokens: list[Token] = []
        self._position = 0
        self._metadata: Metadata | None = None

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

    def _expect(self, token_type: TokenType) -> Token:
        """Consumes the current token if it matches the expected type.

        Args:
            token_type: Expected token type.

        Returns:
            Consumed token.

        Raises:
            UnexpectedTokenError: If the current token does not match.
        """
        if not self._match(token_type):
            raise NotImplementedError("Parser exceptions not implemented yet.")

        return self._advance()

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

        document = Document(metadata)

        while not self._match(TokenType.EOF):
            document.add_child(
                parse_block(self)
            )

        return document