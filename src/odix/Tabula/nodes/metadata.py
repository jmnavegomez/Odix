from __future__ import annotations

from typing import Any


class Metadata:
    """Stores the metadata associated with a document.

    Metadata are loaded from the document configuration (e.g.
    ``principia.yml``) and stored as key-value pairs.
    """

    def __init__(self, **kwargs: Any) -> None:
        """Initializes the document metadata.

        Args:
            **kwargs: Metadata fields loaded from the document
                configuration.
        """
        self._data = kwargs

    def get(self, key: str, default: Any = None) -> Any:
        """Returns the value associated with a metadata key.

        Args:
            key: Metadata key.
            default: Value returned if the key does not exist.

        Returns:
            Metadata value or ``default`` if the key is not present.
        """
        return self._data.get(key, default)

    def content(self) -> tuple[Any, ...]:
        """Returns the semantic content of the metadata.

        The metadata are sorted by key to ensure a deterministic hash,
        independently of the order in which they were loaded.

        Returns:
            Tuple containing the metadata values.
        """
        return tuple(
            self._data[key]
            for key in sorted(self._data)
        )

    def __getitem__(self, key: str) -> Any:
        """Returns the value associated with a metadata key.

        Args:
            key: Metadata key.

        Returns:
            Metadata value.

        Raises:
            KeyError: If the key does not exist.
        """
        return self._data[key]

    def __contains__(self, key: str) -> bool:
        """Checks whether a metadata key exists.

        Args:
            key: Metadata key.

        Returns:
            ``True`` if the key exists, ``False`` otherwise.
        """
        return key in self._data

    def __setitem__(self, key: str, value: Any) -> None:
        """Sets the value associated with a metadata key.

        Args:
            key: Metadata key.
            value: Metadata value.
        """
        self._data[key] = value

    def __len__(self) -> int:
        """Returns the number of metadata fields.

        Returns:
            Number of metadata fields.
        """
        return len(self._data)

    def __iter__(self):
        """Returns an iterator over the metadata keys.

        Returns:
            Iterator over the metadata keys.
        """
        return iter(self._data)

    def items(self):
        """Returns the metadata items.

        Returns:
            Dictionary items view.
        """
        return self._data.items()

    def keys(self):
        """Returns the metadata items.
        
        Returns:
            Dictionary keys view.
        """
        return self._data.keys()

    def values(self):
        """Returns the metadata items.
        
        Returns:
            Dictionary values view.
        """
        return self._data.values()