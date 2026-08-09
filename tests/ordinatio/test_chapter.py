from pathlib import Path

from odix.ordinatio import Chapter, Principium


def test_chapter_stores_title():
    chapter = Chapter(
        title="Classes",
        principia=[],
    )

    assert chapter.title == "Classes"


def test_chapter_stores_principia(tmp_path: Path):
    source_1 = tmp_path / "pill_1.md"
    source_2 = tmp_path / "pill_2.md"

    source_1.write_text("# First", encoding="utf-8")
    source_2.write_text("# Second", encoding="utf-8")

    principium_1 = Principium(source_1)
    principium_2 = Principium(source_2)

    chapter = Chapter(
        title="Classes",
        principia=[principium_1, principium_2],
    )

    assert chapter.principia == [
        principium_1,
        principium_2,
    ]