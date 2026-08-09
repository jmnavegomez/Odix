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

        data = yaml.safe_load(
            path.read_text(encoding="utf-8")
        )

        if data is None:
            raise ValueError(
                "The YAML file is empty."
            )

        if "document" not in data:
            raise ValueError(
                "The Typus configuration is missing "
                "'document'."
            )

        document_data = data["document"]

        if "page" not in document_data:
            raise ValueError(
                "The document configuration is missing "
                "'page'."
            )

        if "margins" not in document_data:
            raise ValueError(
                "The document configuration is missing "
                "'margins'."
            )

        if "typography" not in document_data:
            raise ValueError(
                "The document configuration is missing "
                "'typography'."
            )

        if "layout" not in document_data:
            raise ValueError(
                "The document configuration is missing "
                "'layout'."
            )

        if "numbering" not in document_data:
            raise ValueError(
                "The document configuration is missing "
                "'numbering'."
            )

        if "packages" not in document_data:
            raise ValueError(
                "The document configuration is missing "
                "'packages'."
            )

        page = document_data["page"]
        margins_data = document_data["margins"]
        typography = document_data["typography"]
        layout = document_data["layout"]
        numbering = document_data["numbering"]

        margins = Margins(
            top=margins_data["top"],
            bottom=margins_data["bottom"],
            left=margins_data["left"],
            right=margins_data["right"],
        )

        document = DocumentStyle(
            page_size=page["size"],
            orientation=page["orientation"],
            margins=margins,
            font_size=typography["font_size"],
            line_spacing=typography["line_spacing"],
            twoside=layout["twoside"],
            chapters_start_on_odd_page=(
                layout["chapters_start_on_odd_page"]
            ),
            page_numbering=numbering["pages"],
            page_numbering_position=(
                numbering["position"]
            ),
            packages=list(document_data["packages"]),
        )

        return document