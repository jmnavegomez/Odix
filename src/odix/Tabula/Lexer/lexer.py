from __future__ import annotations

from .reader import Reader
from .reader_type import ReaderType
from .token import Token
from .token_type import TokenType


class Lexer:
    """Lexical analyzer for Markdown documents."""

    def __init__(self) -> None:
        """Initialize the lexer."""

        self._text = ""
        self._position = 0
        self._line = 1
        self._column = 1

        self._token_readers = {
            "#": Reader(ReaderType.REPEATED, TokenType.HASH),
            "*": Reader(ReaderType.REPEATED, TokenType.ASTERISK),
            "·": Reader(ReaderType.REPEATED, TokenType.MIDDLE_DOT),  # Nuevo
            "_": Reader(ReaderType.REPEATED, TokenType.UNDERSCORE),
            "`": Reader(ReaderType.REPEATED, TokenType.BACKTICK),
            "$": Reader(ReaderType.REPEATED, TokenType.DOLLAR),
            ":": Reader(ReaderType.REPEATED, TokenType.COLON),
            "-": Reader(ReaderType.REPEATED, TokenType.HYPHEN),
            "+": Reader(ReaderType.REPEATED, TokenType.PLUS),
            "|": Reader(ReaderType.SINGLE, TokenType.PIPE),
            "%": Reader(ReaderType.SINGLE, TokenType.MODULE),  # Nuevo
            "&": Reader(ReaderType.SINGLE, TokenType.AMPERSAND),  # Nuevo
            "^": Reader(ReaderType.SINGLE, TokenType.CARET),  # Nuevo
            "~": Reader(ReaderType.SINGLE, TokenType.TILDE),  # Nuevo
            ">": Reader(ReaderType.SINGLE, TokenType.GREATER_THAN),
            "<": Reader(ReaderType.SINGLE, TokenType.LESS_THAN),
            "\n": Reader(ReaderType.SINGLE, TokenType.NEWLINE),
        }

    @property
    def _current(self) -> str | None:
        """Return the current character.

        Returns:
            The current character, or ``None`` if the end of the document has
            been reached.
        """
        if self._position >= len(self._text):
            return None

        return self._text[self._position]

    def _reset(self, text: str) -> None:
        """Reset the lexer state.

        Args:
            text: Markdown document to tokenize.
        """
        self._text = text
        self._position = 0
        self._line = 1
        self._column = 1

    def _advance(self) -> None:
        """Advance the current position by one character."""
        if self._current == "\n":
            self._line += 1
            self._column = 1
        else:
            self._column += 1

        self._position += 1

    def _read_single_symbol(
        self,
        token_type: TokenType,
    ) -> Token:
        """Read a single-character symbol.

        Args:
            token_type: Token type associated with the symbol.

        Returns:
            A token representing the current symbol.
        """

        assert self._current is not None

        token = Token(
            token_type,
            self._current,
            self._line,
            self._column,
        )

        self._advance()

        return token

    def _read_repeated_symbol(
        self,
        symbol: str,
        token_type: TokenType,
    ) -> Token:
        """Read consecutive occurrences of the same symbol.

        Args:
            symbol: Symbol to read.
            token_type: Token type associated with the symbol.

        Returns:
            A token containing the complete symbol sequence.
        """
        start_line = self._line
        start_column = self._column

        count = 0

        while self._current == symbol:
            count += 1
            self._advance()

        return Token(
            token_type,
            symbol * count,
            start_line,
            start_column,
        )

    def _read_text(self) -> Token:
        """Read plain text until a special symbol is found.

        Returns:
            A text token.
        """
        start_line = self._line
        start_column = self._column

        value = ""

        while self._current is not None and self._current not in self._token_readers:
            value += self._current
            self._advance()

        return Token(
            TokenType.TEXT,
            value,
            start_line,
            start_column,
        )

    def tokenize(self, text: str) -> list[Token]:
        """Tokenize a Markdown document.

        Args:
            text: Markdown document to tokenize.

        Returns:
            A list of lexical tokens.
        """
        self._reset(text)

        tokens: list[Token] = []

        while self._current is not None:

            if self._current in self._token_readers:

                reader = self._token_readers[self._current]

                if reader.reader_type is ReaderType.SINGLE:
                    tokens.append(self._read_single_symbol(reader.token_type))
                else:
                    tokens.append(
                        self._read_repeated_symbol(
                            self._current,
                            reader.token_type,
                        )
                    )

                continue

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
