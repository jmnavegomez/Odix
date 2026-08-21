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

from odix.exceptions import OdixError

from ..lexer.token import Token
from ..lexer.token_type import TokenType


class ParserError(OdixError):
    """Base exception for parser errors."""

    def __init__(
        self,
        message: str,
        token: Token,
        expected_token: Token | None = None,
        expected_token_type: TokenType | None = None,
    ) -> None:
        self.message = message
        self.token = token
        self.expected_token = expected_token
        self.expected_token_type = expected_token_type

        super().__init__(message)
