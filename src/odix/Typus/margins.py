from __future__ import annotations


class Margins:
    """Defines the document margins."""

    def __init__(
        self,
        top: str,
        bottom: str,
        left: str,
        right: str,
    ) -> None:
        self._top = top
        self._bottom = bottom
        self._left = left
        self._right = right

    @property
    def top(self) -> str:
        return self._top

    @property
    def bottom(self) -> str:
        return self._bottom

    @property
    def left(self) -> str:
        return self._left

    @property
    def right(self) -> str:
        return self._right
