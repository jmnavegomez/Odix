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

from pathlib import Path

import yaml

from .document_style import DocumentStyle
from .margins import Margins


class Loader:
    """Loads Typus styles from YAML files."""

    @classmethod
    def load(cls, path: str | Path) -> DocumentStyle:
        """Loads a Typus configuration from a YAML file."""
        path = Path(path)

        data = yaml.safe_load(path.read_text(encoding="utf-8"))

        if data is None:
            raise ValueError("The YAML file is empty.")

        if "document" not in data:
            raise ValueError("The Typus configuration is missing " "'document'.")

        document_data = data["document"]
        if "class" not in document_data:
            raise ValueError("The document class is missing " "'document class'.")

        if "page" not in document_data:
            raise ValueError("The document configuration is missing " "'page'.")

        if "margins" not in document_data:
            raise ValueError("The document configuration is missing " "'margins'.")

        if "typography" not in document_data:
            raise ValueError("The document configuration is missing " "'typography'.")

        if "layout" not in document_data:
            raise ValueError("The document configuration is missing " "'layout'.")

        if "numbering" not in document_data:
            raise ValueError("The document configuration is missing " "'numbering'.")

        if "language" not in document_data:
            raise ValueError("The document language is missing " "'document language'.")

        if "packages" not in document_data:
            raise ValueError("The document configuration is missing " "'packages'.")

        document_class = document_data["class"]
        page = document_data["page"]
        margins_data = document_data["margins"]
        typography = document_data["typography"]
        layout = document_data["layout"]
        numbering = document_data["numbering"]
        language = document_data["language"]

        margins = Margins(
            top=margins_data["top"],
            bottom=margins_data["bottom"],
            left=margins_data["left"],
            right=margins_data["right"],
        )

        document = DocumentStyle(
            document_class=document_class,
            page_size=page["size"],
            orientation=page["orientation"],
            margins=margins,
            font_size=typography["font_size"],
            line_spacing=typography["line_spacing"],
            font=typography["font"],
            twoside=layout["twoside"],
            chapters_start_on_odd_page=(layout["chapters_start_on_odd_page"]),
            table_of_contents=(layout["table_of_contents"]),
            page_numbering=numbering["pages"],
            page_numbering_position=(numbering["position"]),
            language=language,
            packages=list(document_data["packages"]),
        )

        return document
