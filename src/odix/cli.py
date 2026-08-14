from __future__ import annotations

import argparse
from pathlib import Path

from odix.impressio import Impressio
from odix.ordinatio import Ordinatio
from odix.typus import Typus


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


def main() -> None:
    """Runs the Odix command-line interface."""

    parser = argparse.ArgumentParser(
        prog="odix",
        description=(
            "An open-source publishing system "
            "for technical books."
        ),
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

    args = parser.parse_args()

    if args.command == "build":
        build(
            book_file=args.book,
            typus_file=args.typus,
        )


if __name__ == "__main__":
    main()