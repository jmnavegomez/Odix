"""
Scriptorium
===========

High-level compilation pipeline for Odix.

Public API
==========

build
    Builds a publication from source files.
"""

from .compiler import build

__all__ = [
    "build",
]