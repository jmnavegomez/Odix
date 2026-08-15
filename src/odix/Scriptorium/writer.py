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
            syntax = SYNTAX[command][self._language]

        except KeyError as error:
            raise ValueError(
                f"Unsupported command '{command}' "
                f"for language '{self._language.value}'."
            ) from error

        return syntax.opening + content + syntax.closing

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
            raise ValueError(f"Invalid section level ({level}).")

        return f"Section{level}"

    def command_table(
        self,
        content: str = "",
        **kwargs,
    ) -> str:
        """Resolves a table command.

        Args:
            columns: Number of table columns.

        Returns:
            Concrete table command.
        """

        try:
            syntax = SYNTAX["Table"][self._language]

        except KeyError as error:
            raise ValueError(f"for language '{self._language.value}'.") from error

        opening = syntax.opening

        structure = kwargs.get("structure")

        if structure is not None:
            opening = opening.replace(
                "{{structure}}",
                structure,
            )

        caption = kwargs.get("caption", "")
        label = kwargs.get("label", "")

        closing = syntax.closing

        closing = closing.replace(
            "{caption}",
            caption,
        ).replace(
            "{label}",
            label,
        )

        return opening + content + closing

    def command_mathblock(
        self,
        content: str = "",
        **kwargs,
    ) -> str:
        """Resolves a table command.

        Args:
            columns: Number of table columns.

        Returns:
            Concrete table command.
        """

        try:
            syntax = SYNTAX["MathBlock"][self._language]

        except KeyError as error:
            raise ValueError(f"for language '{self._language.value}'.") from error

        opening = syntax.opening

        label = kwargs.get("label", "")

        closing = syntax.closing

        closing = closing.replace(
            "{label}",
            label,
        )

        return opening + content + closing

    def command_figure(
        self,
        content: str = "",
    ) -> str:
        """Resolves a figure command.

        Args:
            content: content of the figure.

        Returns:
            Concrete figure command.
        """

        try:
            syntax = SYNTAX["Figure"][self._language]

        except KeyError as error:
            raise ValueError(f"for language '{self._language.value}'.") from error

        opening = syntax.opening

        return opening + content + syntax.closing
