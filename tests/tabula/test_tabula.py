import pytest

from odix import Tabula
from odix.tabula.nodes import Document, Paragraph, Text


def test_from_content():
    content = "# Título\n\nTexto de prueba."

    tabula = Tabula.from_content(content)

    assert isinstance(tabula.ast, Document)
    assert tabula.path is None


def test_from_content_creates_expected_ast():
    content = "# Título"

    tabula = Tabula.from_content(content)

    assert isinstance(tabula.ast.children[0].title, Paragraph)
    assert isinstance(tabula.ast.children[0].title.children[0], Text)
    assert tabula.ast.children[0].title.children[0].text == "Título"


def test_from_file(tmp_path):
    path = tmp_path / "document.md"
    path.write_text("# Título", encoding="utf-8")

    tabula = Tabula.from_file(path)

    assert isinstance(tabula.ast, Document)
    assert tabula.path == path


def test_from_file_accepts_string_path(tmp_path):
    path = tmp_path / "document.md"
    path.write_text("# Título", encoding="utf-8")

    tabula = Tabula.from_file(str(path))

    assert tabula.path == path


def test_from_content_and_from_file_are_equivalent(tmp_path):
    content = "# Título\n\nTexto de prueba."

    path = tmp_path / "document.md"
    path.write_text(content, encoding="utf-8")

    from_content = Tabula.from_content(content)
    from_file = Tabula.from_file(path)

    assert from_content.ast == from_file.ast


def test_constructor_requires_path_or_document():
    with pytest.raises(ValueError):
        Tabula()


def test_constructor_rejects_invalid_document():
    with pytest.raises(TypeError):
        Tabula(document="not a document")


def test_from_file_raises_for_missing_file(tmp_path):
    path = tmp_path / "missing.md"

    with pytest.raises(FileNotFoundError):
        Tabula.from_file(path)
