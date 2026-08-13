from __future__ import annotations

from .block import Block

from typing import Any, Self

class Label(Block):
    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key

    def content(self) -> tuple[Any, ...]:
        return (self.key,)

    @classmethod
    def from_content(cls, content: Any) -> Self:
        return cls(content)