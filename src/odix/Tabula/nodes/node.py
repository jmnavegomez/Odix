from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator
from hashlib import sha256
from typing import Any, Self


class Node(ABC):
    """Base class for all Tabula nodes.

    Every element of the AST inherits from this class. A node stores its
    unique identifier, its position in the tree and its children.

    Attributes:
        id: Unique node identifier.
        parent: Parent node. ``None`` if this node is the root.
        children: Child nodes.
    """

    _next_id = 0

    def __init__(self) -> None:
        """Initializes a new node."""
        self.id = Node._next_id
        Node._next_id += 1

        self.parent: Node | None = None
        self.children: list[Node] = []

    @abstractmethod
    def content(self) -> tuple[Any, ...]:
        """Returns the semantic content of the node.

        The returned tuple must contain every attribute that uniquely
        defines the semantic content of the node. Child nodes must not be
        included, since they are incorporated automatically when computing
        the context hash.

        Returns:
            Tuple containing the semantic content of the node.
        """

    def _normalize_for_hash(
        self,
        value: Any,
    ) -> Any:
        """Converts semantic content into a hashable representation."""

        if isinstance(value, Node):
            return value.content_hash

        if isinstance(value, tuple):
            return tuple(
                self._normalize_for_hash(item)
                for item in value
            )

        if isinstance(value, list):
            return [
                self._normalize_for_hash(item)
                for item in value
            ]

        if isinstance(value, dict):
            return {
                key: self._normalize_for_hash(item)
                for key, item in value.items()
            }

        return value

    @property
    def content_hash(self) -> str:
        """Returns the hash of the node semantic content."""

        normalized = self._normalize_for_hash(
            self.content()
        )

        serialized = repr(normalized).encode("utf-8")

        return sha256(serialized).hexdigest()

    @property
    def context_hash(self) -> str:
        """Returns the hash of the subtree rooted at this node.

        The context hash is computed from the node content hash and the
        context hashes of all its children.

        Returns:
            SHA-256 hash representing the complete subtree.
        """
        serialized = self.content_hash + "".join(
            child.context_hash for child in self.children
        )

        return sha256(serialized.encode("utf-8")).hexdigest()

    @property
    def path(self) -> tuple[int, ...]:
        """Returns the structural path of the node within the AST.

        Returns:
            Tuple containing the indices required to reach this node from
            the document root.
        """
        if self.parent is None:
            return ()

        index = self.parent.children.index(self)
        return (*self.parent.path, index)

    @classmethod
    def from_content(
        cls,
        content: Any,
    ) -> Self:
        """Creates a node from serialized content.

        Args:
            content: Serialized semantic content.

        Returns:
            Deserialized node.
        """
        return cls()

    def add_child(self, child: Node) -> None:
        """Adds a child node.

        Args:
            child: Node to attach.
        """
        child.parent = self
        self.children.append(child)

    def remove_child(self, child: Node) -> None:
        """Removes a child node.

        Args:
            child: Child node to remove.

        Raises:
            ValueError: If the node is not a child of this node.
        """
        self.children.remove(child)
        child.parent = None

    def walk(self) -> Iterator[Node]:
        """Traverses the subtree in depth-first order.

        Yields:
            Each node of the subtree, starting from this node.
        """
        yield self

        for child in self.children:
            yield from child.walk()

    def __iter__(self) -> Iterator[Node]:
        """Iterates over the subtree."""
        return self.walk()

    def __eq__(self, other: object) -> bool:
        """Returns whether two nodes are semantically equal."""

        if not isinstance(other, Node):
            return NotImplemented

        return hash(self) == hash(other)


    def __hash__(self) -> int:
        """Returns the hash of the subtree."""

        return hash(self.context_hash)