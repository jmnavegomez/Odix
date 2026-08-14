# Odix Roadmap

## 0. Research

Understand the publishing ecosystem before implementing the compiler.

- [x] Markdown analysis
- [x] LaTeX analysis
- [x] Compiler structure and performance
- [x] Pandoc architecture study
- [x] Existing technical publishing systems
- [x] AST design patterns
- [ ] LaTeX publishing requirements
- [ ] EPUB and HTML publishing requirements

### Deliverable

A research document summarizing the publishing ecosystem,
design alternatives, architectural decisions and the rationale
behind the Odix compiler.



## I. Foundations

Establish the philosophical and technical foundations of the project.

- [x] Project philosophy
- [x] Repository structure
- [x] Build pipeline
- [x] Development environment
- [x] Coding standards (Ruff, formatting, typing)
- [ ] Contribution guidelines



## II. Language Definition

Define the language used to express a Principia.

- [ ] Establish the concepts
- [ ] LaTeX feature analysis
- [ ] Enriched Markdown specification
- [ ] Metadata format (`principia.yml`)
- [ ] Bibliography model
- [ ] Cross-reference model
- [ ] Error reporting strategy

### Deliverable

A complete specification document describing the Principia language and its semantics.



## III. Tabula Core

Design and implement the central representation of the book.

- [ ] Tabula node hierarchy
- [ ] Document model
- [ ] Metadata model
- [ ] Section and chapter model
- [ ] Figure and table model
- [ ] Equation model
- [ ] Citation model
- [ ] Serialization and debugging utilities

### Deliverable

A stable `Tabula` API independent from any renderer.



## IV. Principia Analysis

Transform a Principia into a validated Tabula.

- [x] Lexer
- [x] Parser
- [x] Tabula generation
- [ ] Semantic validation
- [ ] Reference resolution
- [ ] Diagnostics and error messages
- [x] Validation tests

### Deliverable

`principia -> tabula`



## V. Scriptorium

Compile the Tabula into a Codex representation.

- [ ] Codex intermediate model
- [ ] Structural transformations
- [ ] Numbering system
- [ ] Table of contents generation
- [ ] Index preparation
- [ ] Bibliography preparation
- [ ] Incremental build support

### Deliverable

`tabula -> codex`



## VI. Typus

Apply the visual identity of the book.

- [ ] Theme system
- [ ] Typography configuration
- [ ] Page layout model
- [ ] Code block styling
- [ ] Figure and table styling
- [ ] Admonitions and callouts
- [ ] Default theme

### Deliverable

A fully styled Codex ready for publication.



## VII. Impressio

Publish the final work.

- [ ] LaTeX backend
- [ ] PDF backend
- [ ] HTML backend
- [ ] EPUB backend
- [ ] Asset management
- [ ] Output directory structure
- [ ] Publication metadata
- [ ] Reproducible build verification

### Deliverable

`codex -> LaTeX/pdf/html/epub`



## VIII. First Book

Validate the complete workflow with a real project.

- [ ] Create example templates
- [ ] Create a personalized theme
- [ ] Write the first Principia
- [ ] Generate LaTeX
- [ ] Generate PDF
- [ ] Generate HTML
- [ ] Generate EPUB
- [ ] Review the editorial workflow

### Deliverable

The first complete book published with Odix.



## IX. Stabilization

Prepare the project for external users.

- [x] Unit tests
- [ ] Integration tests
- [ ] Golden-file rendering tests
- [x] Performance benchmarks
- [x] Documentation
- [ ] Tutorials and examples
- [ ] CI/CD pipeline
- [x] PyPI packaging
- [ ] Versioning strategy
- [ ] Release v0.1.0
- [ ] Release v1.0.0



## Compiler Pipeline

Principia → Tabula → Scriptorium → Codex → Typus → Impressio → LaTeX / PDF / HTML / EPUB



## Success Criteria for v0.1.0

- Parse a non-trivial Principia
- Generate a valid Tabula



## Release Roadmap

| Version | Main milestone               |
| v0.1.0  | Principia → Tabula           |
| v0.2.0  | Tabula → Codex               |
| v0.3.0  | Codex → Styled Codex (Typus) |
| v0.4.0  | PDF backend                  |
| v0.5.0  | HTML backend                 |
| v0.6.0  | EPUB backend                 |
| v0.7.0  | Themes & plugin system       |
| v0.8.0  | Performance & extensibility  |
| v0.9.0  | Feature complete             |
| v1.0.0  | Stable production release    |



## Long-term Vision

- Plugin system
- Multi-language books
- Advanced bibliography support
- Interactive HTML editions
- Print-ready publishing workflow
- Collaborative editorial features
- Digital preservation tooling



> May every Principia become a worthy Codex.


