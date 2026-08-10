from pathlib import Path

from odix.impressio import Impressio
from odix.ordinatio import Ordinatio
from odix.typus import Typus


ROOT = Path(__file__).parents[1]

VOLUME = ROOT / "examples" / "Volumen_01"

BOOK_FILE = VOLUME / "book.yml"

TYPUS_FILE = (
    ROOT
    / "src"
    / "odix"
    / "typus"
    / "typus_default.yml"
)

OUTPUT_FILE = VOLUME / "Volumen_01.tex"


book = Ordinatio.from_file(
    BOOK_FILE,
)

typus = Typus.from_file(
    TYPUS_FILE,
)

impressio = Impressio(
    book=book,
    typus=typus,
)

impressio.publish(
    OUTPUT_FILE,
)

print(f"Book published to: {OUTPUT_FILE}")