from __future__ import annotations

from typing import Any, Self

from .block import Block


class Label(Block):
    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key

    def content(self) -> tuple[Any, ...]:
        return (self.key,)

    @classmethod
    def from_content(cls, content: Any) -> Self:
        return cls(content)
