# Citations and bibliography

Odix supports bibliographic references using BibTeX.

A book can define a bibliography in its `book.yml` configuration and individual references can then be cited from any Principium.

## Bibliography configuration

The bibliography is configured in `book.yml`:

```yaml
bibliography:
  file: "references.bib"
  style: "plain"
```

The `file` property specifies the BibTeX file containing the bibliographic references.

The `style` property specifies the bibliography style used by the LaTeX publication.

For example, a project can contain:

```text
my-book/
├── book.yml
├── typus.yml
├── references.bib
├── introduction.md
└── ...
```

## BibTeX references

The `references.bib` file contains the bibliographic entries.

For example:

```bibtex
@article{smith2022,
    author  = {Smith, John},
    title   = {An Example of a Scientific Article},
    journal = {Journal of Examples},
    year    = {2022},
    volume  = {10},
    number  = {2},
    pages   = {1--10}
}
```

The value `smith2022` is the citation key of the reference.

## Citing a reference

A reference can be cited from a Principium using its citation key:

```text
This result was previously described in the literature ··smith2022··.
```

The citation key must correspond to an entry in the BibTeX file.

When Odix generates the LaTeX document, the citation is converted into the corresponding LaTeX citation command.

For example:

```latex
\cite{smith2022}
```

## Multiple citations

Multiple references can be cited independently in the same Principium:

```text
Several studies have investigated this problem ··smith2022·· and
··jones2024··.
```

Each citation key must correspond to an entry in the bibliography.

## Bibliography in the published document

When a bibliography is configured, Odix adds the required bibliography commands to the generated LaTeX document.

For example:

```latex
\bibliographystyle{plain}
\bibliography{references}
```

The references are then resolved by the LaTeX and BibTeX compilation process.

The final bibliography is therefore generated from the BibTeX file rather than being written directly inside the Principia.

## Summary

Odix separates bibliographic information from the book content.

The `book.yml` file specifies:

+ the BibTeX file;
+ the bibliography style.

The `.bib` file contains the bibliographic references.

Principia contain citations using their corresponding citation keys.

The publication process connects these elements and generates the bibliography in the final document.

::pagebreak
::