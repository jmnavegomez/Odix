# Odix - Open-source publishing system for technical books
# Copyright (C) 2026 José Manuel Naveiro
#
# This file is part of Odix.
#
# Odix is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# Odix is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Odix. If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

import argparse
import json
from pathlib import Path

from odix import Impressio, Ordinatio, Tabula, Typus
from odix.exceptions import OdixError
from odix.tabula import Serializer


def build(
    book_file: Path,
    typus_file: Path,
) -> None:
    """Builds a book from YAML configuration files."""

    book = Ordinatio.from_file(
        book_file,
    )

    typus = Typus.from_file(
        typus_file,
    )

    impressio = Impressio(
        book=book,
        typus=typus,
    )

    output = book_file.with_suffix(".tex")

    impressio.publish(
        output,
    )

    print(f"Book published to: {output}")


def tabula(document_file: Path) -> None:
    """Displays the Tabula AST of a Markdown document."""

    document = Tabula.from_file(document_file)

    print(
        json.dumps(
            Serializer().visit(document.ast),
            indent=4,
            ensure_ascii=False,
        )
    )


def main() -> None:
    """Runs the Odix command-line interface."""

    parser = argparse.ArgumentParser(
        prog="odix",
        description=("An open-source publishing system " "for technical books."),
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    build_parser = subparsers.add_parser(
        "build",
        help="Build a book from YAML configuration files.",
    )

    build_parser.add_argument(
        "book",
        type=Path,
        help="Path to the book.yml file.",
    )

    build_parser.add_argument(
        "--typus",
        type=Path,
        required=True,
        help="Path to the Typus configuration file.",
    )

    tabula_parser = subparsers.add_parser(
        "tabula",
        help="Display the Tabula AST of a Markdown document.",
    )

    tabula_parser.add_argument(
        "document",
        type=Path,
        help="Path to the Markdown document.",
    )

    args = parser.parse_args()

    try:
        if args.command == "build":
            build(
                book_file=args.book,
                typus_file=args.typus,
            )
        elif args.command == "tabula":
            tabula(
                document_file=args.document,
            )
    except OdixError as error:
        print()
        print(f"Error: {error}")
        print()


if __name__ == "__main__":
    main()
