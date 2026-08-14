from odix.tabula.lexer import Lexer
from odix.tabula.nodes import (
    Bibliography,
    Caption,
    Figure,
    Image,
    MathBlock,
    PageBreak,
    Reference,
)
from odix.tabula.parser import Parser


def parse(markdown: str):
    lexer = Lexer()
    parser = Parser()

    tokens = lexer.tokenize(markdown)

    return parser.parse(tokens)


def test_math_block() -> None:

    document = parse("""::math
x^2 + y^2 = z^2
::""")

    assert len(document.children) == 1

    node = document.children[0]

    assert isinstance(node, MathBlock)
    assert node.expression == "x^2 + y^2 = z^2"


def test_page_break() -> None:

    document = parse("""::pagebreak
::""")

    assert len(document.children) == 1

    assert isinstance(
        document.children[0],
        PageBreak,
    )


def test_image() -> None:

    document = parse("""::image
figure.png
::""")

    assert len(document.children) == 1

    node = document.children[0]

    assert isinstance(node, Image)
    assert node.source == "figure.png"


def test_caption() -> None:

    document = parse("""::caption
Figure caption.
::""")

    assert len(document.children) == 1

    node = document.children[0]

    assert isinstance(node, Caption)

    assert len(node.children) == 1
    assert node.children[0].text == "Figure caption."


def test_reference() -> None:

    document = parse("""::reference
smith2025
::""")

    assert len(document.children) == 1

    node = document.children[0]

    assert isinstance(node, Reference)
    assert node.key == "smith2025"


def test_bibliography() -> None:

    document = parse("""::bibliography
smith2025
doe2024
miller2021
::""")

    assert len(document.children) == 1

    bibliography = document.children[0]

    assert isinstance(
        bibliography,
        Bibliography,
    )

    assert len(bibliography.children) == 3

    reference = bibliography.children[0]

    assert isinstance(reference, Reference)
    assert reference.key == "smith2025"


def test_figure() -> None:

    document = parse("""::figure
figure.png
Example figure
::""")

    assert len(document.children) == 1

    figure = document.children[0]

    assert isinstance(
        figure,
        Figure,
    )

    assert len(figure.children) == 2

    assert isinstance(
        figure.children[0],
        Image,
    )

    assert isinstance(
        figure.children[1],
        Caption,
    )

    assert figure.children[0].source == "figure.png"
