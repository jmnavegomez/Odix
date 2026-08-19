import json

import pytest

from odix.cli import main, tabula


def test_tabula_command(capsys, tmp_path):
    document = tmp_path / "document.md"
    document.write_text("# Título", encoding="utf-8")

    tabula(document)

    captured = capsys.readouterr()

    assert '"type": "Document"' in captured.out
    assert '"Título"' in captured.out


def test_tabula_command_outputs_json(capsys, tmp_path):
    document = tmp_path / "document.md"
    document.write_text("# Título", encoding="utf-8")

    tabula(document)

    captured = capsys.readouterr()
    data = json.loads(captured.out)

    assert data["type"] == "Document"


def test_tabula_command_preserves_unicode(capsys, tmp_path):
    document = tmp_path / "document.md"
    document.write_text(
        "# Introducción\n\nTexto científico: áéíóú ñ",
        encoding="utf-8",
    )

    tabula(document)

    captured = capsys.readouterr()

    assert "Introducción" in captured.out
    assert "áéíóú ñ" in captured.out


def test_main_tabula(monkeypatch, capsys, tmp_path):
    document = tmp_path / "document.md"
    document.write_text("# Título", encoding="utf-8")

    monkeypatch.setattr(
        "sys.argv",
        ["odix", "tabula", str(document)],
    )

    main()

    captured = capsys.readouterr()

    data = json.loads(captured.out)

    assert data["type"] == "Document"


def test_main_requires_command(monkeypatch):
    monkeypatch.setattr("sys.argv", ["odix"])

    with pytest.raises(SystemExit):
        main()


def test_main_tabula_requires_document(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["odix", "tabula"],
    )

    with pytest.raises(SystemExit):
        main()
