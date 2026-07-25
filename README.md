# Odix

> Every idea deserves a worthy Codex.
>
> Technical publishing with the discipline of software engineering.

An open-source publishing system for creating beautiful technical books from Markdown.

Inspired by centuries of editorial craftsmanship and designed with the discipline of modern software engineering.

Odix is free software because knowledge deserves free tools.

The software belongs to its community.

Every book belongs to its author.

Every book begins as a **Principia**.

A **Principia** is analysed into a **Tabula**.

The **Scriptorium** compiles the **Tabula** into a **Codex**.

**Typus** gives the **Codex** its visual identity.

Finally, **Impressio** publishes the finished work.

```text
Markdown
    │
    ▼
 Tabula
    │
    ▼
Scriptorium
    │
    ▼
 Codex
    │
    ▼
 Typus
    │
    ▼
Impressio
    │
    ▼
PDF • EPUB • HTML
```

## Why Odix?

Modern technical books deserve more than file converters.

Odix treats books as reproducible software artifacts.

Instead of manually formatting documents, authors describe knowledge while Odix takes care of structure, typography and publication.

The result is a deterministic publishing workflow inspired by the traditions of classical bookmaking.

## Features

- Markdown-first authoring
- Beautiful PDF generation through LaTeX
- EPUB and HTML support
- Cross references
- Automatic numbering
- Table of contents
- Bibliography management
- Footnotes
- Extensible architecture
- Deterministic builds
- Open Source
- Semantic document model

## Installation

```bash
pip install odix
```

## Quick Start

```bash
odix build book.md
```

```python
from odix import build

build("book.md")
```

## Documentation

The complete documentation can be found in the `docs/` directory.

- Philosophy
- Manifesto
- Architecture
- Roadmap
- Journal

## License

Odix is released under the GNU General Public License v3.0.

We believe that the tools used to preserve knowledge should remain free for future generations.

Ideas deserve permanence.

Software deserves freedom.

Books deserve craftsmanship.

## Status

Odix is currently under active development.

The architecture is being designed with long-term stability in mind.

Breaking changes are expected until the first stable release.