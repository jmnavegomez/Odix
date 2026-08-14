import pytest

from odix.tabula.io.deserializer import Deserializer
from odix.tabula.io.serializer import Serializer
from odix.tabula.lexer.lexer import Lexer
from odix.tabula.nodes import (
    Document,
    Paragraph,
    Section,
)
from odix.tabula.parser.parser import Parser


def test_round_trip() -> None:
    source = """# A
Texto

## B
Texto

### C
Texto
"""

    lexer = Lexer()
    parser = Parser()
    serializer = Serializer()
    deserializer = Deserializer()

    tokens = lexer.tokenize(source)
    document = parser.parse(tokens)

    data = serializer.visit(document)

    restored = deserializer.deserialize(data)

    restored_data = serializer.visit(restored)

    assert restored_data == data

    assert isinstance(restored, Document)

    section = restored.children[0]
    assert isinstance(section, Section)
    assert section.level == 1

    paragraph = section.children[0]
    assert isinstance(paragraph, Paragraph)

def test_deserialize_unknown_node_type() -> None:
    """Unknown node types raise a ValueError."""

    deserializer = Deserializer()

    data = {
        "type": "UnknownNode",
        "content": (),
        "children": [],
    }

    with pytest.raises(ValueError) as exc_info:
        deserializer.deserialize(data)

    assert str(exc_info.value) == (
        "Unknown node type 'UnknownNode'."
    )