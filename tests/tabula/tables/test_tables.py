from odix.tabula.lexer import Lexer
from odix.tabula.lexer import TokenType


def test_table_tokens() -> None:
    lexer = Lexer()

    markdown = (
        "| Nombre | Edad |\n"
        "| Jose | 30 |\n"
    )

    tokens = lexer.tokenize(markdown)

    expected = [
        (TokenType.PIPE, "|"),
        (TokenType.TEXT, " Nombre "),
        (TokenType.PIPE, "|"),
        (TokenType.TEXT, " Edad "),
        (TokenType.PIPE, "|"),
        (TokenType.NEWLINE, "\n"),

        (TokenType.PIPE, "|"),
        (TokenType.TEXT, " Jose "),
        (TokenType.PIPE, "|"),
        (TokenType.TEXT, " 30 "),
        (TokenType.PIPE, "|"),
        (TokenType.NEWLINE, "\n"),

        (TokenType.EOF, ""),
    ]

    assert len(tokens) == len(expected)

    for token, (token_type, value) in zip(tokens, expected):
        assert token.type is token_type
        assert token.value == value