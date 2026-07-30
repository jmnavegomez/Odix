from __future__ import annotations

from .token import Token
from .token_type import TokenType


class Lexer:
    """Tokenizes Markdown documents."""

    def __init__(self) -> None:
        """Initialize the lexer."""
        self._text = ""
        self._position = 0
        self._line = 1
        self._column = 1

        self._token_readers = {
            "#": self._read_heading,
            "\n": self._read_newline,
        }

    @property
    def _current(self) -> str | None:
        """Return the current character."""
        if self._position >= len(self._text):
            return None

        return self._text[self._position]

    def _reset(self, text: str) -> None:
        """Reset the lexer state."""
        self._text = text
        self._position = 0
        self._line = 1
        self._column = 1

    def _advance(self) -> None:
        """Advance one character."""
        if self._current == "\n":
            self._line += 1
            self._column = 1
        else:
            self._column += 1

        self._position += 1

    def _read_heading(self) -> Token:
        """Read a Markdown heading marker."""
        start_line = self._line
        start_column = self._column

        level = 0

        while self._current == "#":
            level += 1
            self._advance()

        return Token(
            TokenType.HEADING,
            "#" * level,
            start_line,
            start_column,
        )

    def _read_newline(self) -> Token:
        """Read a newline."""
        token = Token(
            TokenType.NEWLINE,
            "\n",
            self._line,
            self._column,
        )

        self._advance()

        return token

    def _read_text(self) -> Token:
        """Read plain text."""
        start_line = self._line
        start_column = self._column

        value = ""

        while (
            self._current is not None
            and self._current not in self._token_readers
        ):
            value += self._current
            self._advance()

        return Token(
            TokenType.TEXT,
            value,
            start_line,
            start_column,
        )

    def tokenize(self, text: str) -> list[Token]:
        """
        Tokenize a Markdown document.

        Args:
            text: Markdown document.

        Returns:
            List of tokens.
        """
        self._reset(text)

        tokens: list[Token] = []

        while self._current is not None:

            if self._current in self._token_readers:
                tokens.append(
                    self._token_readers[self._current]()
                )
            else:
                token = self._read_text()

                if token.value:
                    tokens.append(token)

        tokens.append(
            Token(
                TokenType.EOF,
                "",
                self._line,
                self._column,
            )
        )

        return tokens