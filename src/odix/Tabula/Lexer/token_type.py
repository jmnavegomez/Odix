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

from enum import Enum, auto


class TokenType(Enum):
    """Enumeration of lexical token types."""

    TEXT = auto()
    NEWLINE = auto()

    HASH = auto()
    ASTERISK = auto()
    MIDDLE_DOT = auto()  # ·Nuevo·
    UNDERSCORE = auto()
    BACKTICK = auto()
    DOLLAR = auto()
    COLON = auto()

    GREATER_THAN = auto()
    LESS_THAN = auto()

    HYPHEN = auto()
    PLUS = auto()
    PIPE = auto()
    MODULE = auto()  # %Nuevo%
    AMPERSAND = auto()  # &Nuevo&
    CARET = auto()  # ^Nuevo^
    TILDE = auto()  # ~Nuevo~

    LBRACKET = auto()
    RBRACKET = auto()

    LPAREN = auto()
    RPAREN = auto()

    EXCLAMATION = auto()

    EOF = auto()
