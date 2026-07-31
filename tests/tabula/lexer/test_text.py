from odix.tabula.lexer import Lexer
from odix.tabula.lexer import Token
from odix.tabula.lexer import TokenType


def test_empty_document() -> None:
    lexer = Lexer()

    assert lexer.tokenize("") == [
        Token(TokenType.EOF, "", 1, 1),
    ]

def test_text() -> None:
    lexer = Lexer()

    assert lexer.tokenize("Hello") == [
        Token(TokenType.TEXT, "Hello", 1, 1),
        Token(TokenType.EOF, "", 1, 6),
    ]

def test_newline() -> None:
    lexer = Lexer()

    assert lexer.tokenize("\n") == [
        Token(TokenType.NEWLINE, "\n", 1, 1),
        Token(TokenType.EOF, "", 2, 1),
    ]

def test_heading() -> None:
    lexer = Lexer()

    assert lexer.tokenize("#") == [
        Token(TokenType.HASH, "#", 1, 1),
        Token(TokenType.EOF, "", 1, 2),
    ]

def test_heading_and_text() -> None:
    lexer = Lexer()

    assert lexer.tokenize("# Title") == [
        Token(TokenType.HASH, "#", 1, 1),
        Token(TokenType.TEXT, " Title", 1, 2),
        Token(TokenType.EOF, "", 1, 8),
    ]

def test_heading_level_2() -> None:
    lexer = Lexer()

    assert lexer.tokenize("## Title") == [
        Token(TokenType.HASH, "##", 1, 1),
        Token(TokenType.TEXT, " Title", 1, 3),
        Token(TokenType.EOF, "", 1, 9),
    ]

def test_heading_level_6() -> None:
    lexer = Lexer()

    assert lexer.tokenize("###### Title") == [
        Token(TokenType.HASH, "######", 1, 1),
        Token(TokenType.TEXT, " Title", 1, 7),
        Token(TokenType.EOF, "", 1, 13),
    ]

def test_multiple_headings() -> None:
    lexer = Lexer()

    assert lexer.tokenize("# One\n## Two") == [
        Token(TokenType.HASH, "#", 1, 1),
        Token(TokenType.TEXT, " One", 1, 2),
        Token(TokenType.NEWLINE, "\n", 1, 6),
        Token(TokenType.HASH, "##", 2, 1),
        Token(TokenType.TEXT, " Two", 2, 3),
        Token(TokenType.EOF, "", 2, 7),
    ]
