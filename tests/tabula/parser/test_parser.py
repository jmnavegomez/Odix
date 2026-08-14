import pytest

from odix.tabula.lexer import Token, TokenType
from odix.tabula.parser import Parser


def test_reset() -> None:
    parser = Parser()

    tokens = [
        Token(TokenType.TEXT, "Hello", 1, 1),
        Token(TokenType.EOF, "", 1, 6),
    ]

    parser._reset(tokens, None)

    assert parser._tokens == tokens
    assert parser._position == 0
    assert parser._metadata is None


def test_current() -> None:
    parser = Parser()

    tokens = [
        Token(TokenType.TEXT, "Hello", 1, 1),
        Token(TokenType.EOF, "", 1, 6),
    ]

    parser._reset(tokens, None)

    assert parser._current == tokens[0]


def test_peek() -> None:
    parser = Parser()

    tokens = [
        Token(TokenType.TEXT, "Hello", 1, 1),
        Token(TokenType.NEWLINE, "\n", 1, 6),
        Token(TokenType.EOF, "", 2, 1),
    ]

    parser._reset(tokens, None)

    assert parser._peek() == tokens[1]


def test_peek_end_of_file() -> None:
    parser = Parser()

    tokens = [
        Token(TokenType.TEXT, "Hello", 1, 1),
        Token(TokenType.EOF, "", 1, 6),
    ]

    parser._reset(tokens, None)

    assert parser._peek(100) == tokens[-1]


def test_advance() -> None:
    parser = Parser()

    tokens = [
        Token(TokenType.TEXT, "Hello", 1, 1),
        Token(TokenType.EOF, "", 1, 6),
    ]

    parser._reset(tokens, None)

    token = parser._advance()

    assert token == tokens[0]
    assert parser._current == tokens[1]


def test_advance_eof() -> None:
    parser = Parser()

    tokens = [
        Token(TokenType.EOF, "", 1, 1),
    ]

    parser._reset(tokens, None)

    token = parser._advance()

    assert token == tokens[0]
    assert parser._current == tokens[0]


@pytest.mark.parametrize(
    ("current", "types", "expected"),
    [
        (TokenType.TEXT, (TokenType.TEXT,), True),
        (TokenType.TEXT, (TokenType.HASH,), False),
        (TokenType.TEXT, (TokenType.TEXT, TokenType.HASH), True),
        (TokenType.EOF, (TokenType.EOF,), True),
    ],
)
def test_match(
    current: TokenType,
    types: tuple[TokenType, ...],
    expected: bool,
) -> None:
    parser = Parser()

    parser._reset(
        [
            Token(current, "", 1, 1),
        ],
        None,
    )

    assert parser._match(*types) is expected


def test_expect() -> None:
    parser = Parser()

    tokens = [
        Token(TokenType.TEXT, "Hello", 1, 1),
        Token(TokenType.EOF, "", 1, 6),
    ]

    parser._reset(tokens, None)

    token = parser._expect(TokenType.TEXT)

    assert token == tokens[0]
    assert parser._current == tokens[1]


def test_expect_wrong_token() -> None:
    parser = Parser()

    parser._reset(
        [
            Token(TokenType.TEXT, "Hello", 1, 1),
            Token(TokenType.EOF, "", 1, 6),
        ],
        None,
    )

    with pytest.raises(NotImplementedError):
        parser._expect(TokenType.HASH)

from odix.tabula.nodes.text import Text
from odix.tabula.parser.rules.inline.text import parse_text


def test_parse_text():
    parser = Parser()

    parser._reset([
        Token(TokenType.TEXT, "Hello", 1, 1),
        Token(TokenType.EOF, "", 1, 6),], None)

    node = parse_text(parser)

    assert isinstance(node, Text)
    assert node.content() == ("Hello",)

    assert parser._current.type is TokenType.EOF