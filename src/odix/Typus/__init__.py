"""
Typus
=====

Applies styles to a publication.

Public API
==========

Typus
    Loads and applies a publication style.
"""

from .document_style import DocumentStyle
from .margins import Margins
from .typus import Typus

__all__ = [
    "DocumentStyle",
    "Margins",
    "Typus",
]