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

"""
Odix
=====

Open-source publishing system for creating technical books from Markdown.

Public API
==========

Principia
    Represents a publication and its metadata.

Tabula
    Builds the abstract syntax tree (AST).

Typus
    Applies styles to a Principia.

Impressio
    Renders the final publication.

build
    High-level build function.
"""

from impressio import Impressio
from ordinatio import Ordinatio
from typus import Typus
from scriptorium.compiler import Compiler
from tabula import Tabula

__all__ = [
    "Impressio",
    "Ordinatio",
    "Typus",
    "Compiler",
    "Tabula",
]
