from __future__ import annotations

from abc import ABC
from typing import Iterator


class Node(ABC):
    """Base class for all Tabula nodes.

    Every element of the AST inherits from this class. A node stores its
    position in the tree, its children and its unique identifier.

    Attributes:
        id: Unique node identifier.
        parent: Parent node. ``None`` if this node is the root.
        children: Child nodes.
    """

    def __init__(self, node_id: str) -> None:
        """Initializes a new node.

        Args:
            node_id: Unique identifier of the node.
        """
        self.id = node_id
        self.parent: Node | None = None
        self.children: list[Node] = []

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