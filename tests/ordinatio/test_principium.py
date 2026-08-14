from pathlib import Path

from odix import Tabula
from odix.ordinatio import Principium
from odix.tabula.nodes import Document


def test_principium_stores_source(tmp_path: Path):
    source = tmp_path / "pill.md"
    source.write_text(
        "# Hello\n\nThis is a test.",
        encoding="utf-8",
    )

    principium = Principium(source)

    assert principium.source == source


def test_principium_returns_tabula_document(tmp_path: Path):
    source = tmp_path / "pill.md"
    source.write_text(
        "# Hello\n\nThis is a test.",
        encoding="utf-8",
    )

    principium = Principium(source)

    assert isinstance(principium.document, Document)

def test_principium_document_matches_tabula(tmp_path: Path):
    source = tmp_path / "pill.md"
    source.write_text(
        "# Hello\n\nThis is a test.",
        encoding="utf-8",
    )

    principium = Principium(source)
    tabula = Tabula(source)

    assert type(principium.document) is type(tabula.ast)