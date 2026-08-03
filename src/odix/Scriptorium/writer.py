from __future__ import annotations

from collections.abc import Callable

from .language import Language
from .syntax import SYNTAX


class Writer:
    """Writes markup using a target language."""

    def __init__(
        self,
        language: Language,
    ) -> None:
        """Initializes the writer.

        Args:
            language: Output language.
        """

        self._language = language

        self._command_resolvers: dict[
            str,
            Callable[..., str],
        ] = {
            "Section": self._resolve_section,
        }

    def command(
        self,
        command: str,
        content: str = "",
        **kwargs,
    ) -> str:
        """Formats a markup command.

        Args:
            command: Semantic command name.
            content: Command content.
            **kwargs: Optional command arguments.

        Returns:
            Formatted output.

        Raises:
            ValueError: If the command is unsupported.
        """

        resolver = self._command_resolvers.get(command)

        if resolver is not None:
            command = resolver(**kwargs)

        try:
            syntax = SYNTAX[
                command
            ][
                self._language
            ]

        except KeyError as error:
            raise ValueError(
                f"Unsupported command '{command}' "
                f"for language '{self._language.value}'."
            ) from error

        return (
            syntax.opening
            + content
            + syntax.closing
        )

    @staticmethod
    def _resolve_section(
        *,
        level: int,
    ) -> str:
        """Resolves a section command.

        Args:
            level: Section level.

        Returns:
            Concrete section command.

        Raises:
            ValueError: If the section level is invalid.
        """

        if not 1 <= level <= 6:
            raise ValueError(
                f"Invalid section level ({level})."
            )

        return f"Section{level}"