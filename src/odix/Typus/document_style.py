from __future__ import annotations

from .margins import Margins


class DocumentStyle:
    """Defines the global style of an Odix document."""

    def __init__(
        self,
        page_size: str,
        orientation: str,
        margins: Margins,
        font_size: str,
        line_spacing: float,
        twoside: bool,
        chapters_start_on_odd_page: bool,
        page_numbering: bool,
        page_numbering_position: str,
        packages: list[str],
    ) -> None:
        self._page_size = page_size
        self._orientation = orientation
        self._margins = margins
        self._font_size = font_size
        self._line_spacing = line_spacing
        self._twoside = twoside
        self._chapters_start_on_odd_page = (
            chapters_start_on_odd_page
        )
        self._page_numbering = page_numbering
        self._page_numbering_position = (
            page_numbering_position
        )
        self._packages = list(packages)

    @property
    def page_size(self) -> str:
        """Returns the page size."""
        return self._page_size

    @property
    def orientation(self) -> str:
        """Returns the page orientation."""
        return self._orientation

    @property
    def margins(self) -> Margins:
        """Returns the document margins."""
        return self._margins

    @property
    def font_size(self) -> str:
        """Returns the document font size."""
        return self._font_size

    @property
    def line_spacing(self) -> float:
        """Returns the line spacing."""
        return self._line_spacing

    @property
    def twoside(self) -> bool:
        """Returns whether the document uses two-sided layout."""
        return self._twoside

    @property
    def chapters_start_on_odd_page(self) -> bool:
        """Returns whether chapters start on odd pages."""
        return self._chapters_start_on_odd_page

    @property
    def page_numbering(self) -> bool:
        """Returns whether pages are numbered."""
        return self._page_numbering

    @property
    def page_numbering_position(self) -> str:
        """Returns the page numbering position."""
        return self._page_numbering_position

    @property
    def packages(self) -> list[str]:
        """Returns the required LaTeX packages."""
        return self._packages