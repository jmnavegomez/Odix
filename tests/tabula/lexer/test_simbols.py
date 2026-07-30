import pytest

from odix.tabula.lexer.lexer import Lexer
from odix.tabula.lexer.token import Token
from odix.tabula.lexer.token_type import TokenType


@pytest.mark.parametrize(
    ("symbol", "token_type", "line", "column"),
    [
        (">", TokenType.GREATER_THAN, 1, 2),
        ("!", TokenType.EXCLAMATION, 1, 2),
        ("[", TokenType.LBRACKET, 1, 2),
        ("]", TokenType.RBRACKET, 1, 2),
        ("(", TokenType.LPAREN, 1, 2),
        (")", TokenType.RPAREN, 1, 2),
        ("\n", TokenType.NEWLINE, 2, 1),
    ],
)
def test_single_symbols(
    symbol: str,
    token_type: TokenType,
    line: int,
    column: int,
) -> None:
    lexer = Lexer()

    assert lexer.tokenize(symbol) == [
        Token(token_type, symbol, 1, 1),
        Token(TokenType.EOF, "", line, column),
    ]

@pytest.mark.parametrize(
    ("text", "token_type"),
    [
        ("#", TokenType.HASH),
        ("##", TokenType.HASH),
        ("*", TokenType.ASTERISK),
        ("***", TokenType.ASTERISK),
        ("_", TokenType.UNDERSCORE),
        ("___", TokenType.UNDERSCORE),
        ("`", TokenType.BACKTICK),
        ("```", TokenType.BACKTICK),
        ("$", TokenType.DOLLAR),
        ("$$", TokenType.DOLLAR),
        ("-", TokenType.HYPHEN),
        ("---", TokenType.HYPHEN),
        ("+", TokenType.PLUS),
        ("+++", TokenType.PLUS),
        ("|", TokenType.PIPE),
        ("|||", TokenType.PIPE),
    ],
)
def test_repeated_symbols(
    text: str,
    token_type: TokenType,
) -> None:
    lexer = Lexer()

    assert lexer.tokenize(text) == [
        Token(token_type, text, 1, 1),
        Token(TokenType.EOF, "", 1, len(text) + 1),
    ]