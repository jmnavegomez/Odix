# Book configuration

The `book.yml` file defines the structure of an Odix book.

It contains the information needed to identify the publication, define its bibliography and organise its chapters and Principia.

A book configuration can contain three main sections:

- `metadata`
- `bibliography`
- `chapters`

## Metadata

The `metadata` section contains information about the publication.

```yaml
metadata:
  title: "My Technical Book"
  subtitle: "An Introduction"
  author: "Author Name"
  date: "2026"
  edition: "1st edition"
```

The available metadata fields are:

* `title`: the title of the book.
* `subtitle`: the subtitle of the book.
* `author`: the author of the book.
* `date`: the publication date or year.
* `edition`: the edition of the publication.

These values are used by the publication process when generating the book.

## Bibliography

A book can define a bibliography using a BibTeX file.

```yaml
bibliography:
  file: "references.bib"
  style: "plain"
```

The `file` field specifies the BibTeX file containing the references.

The `style` field specifies the bibliography style that will be used when generating the LaTeX document.

For example, a project can contain:

```text
my-book/
├── book.yml
├── typus.yml
├── references.bib
└── ...
```

References can then be cited from the Principia using the corresponding citation syntax.

## Chapters

The `chapters` section defines the structure of the book.

Each chapter has a title and a list of Principia:

```yaml
chapters:
  - title: Introduction
    principia:
      - introduction.md

  - title: Fundamentals
    principia:
      - variables.md
      - data_types.md
      - functions.md
```

The order of the chapters in `book.yml` determines their order in the published book.

The same applies to the Principia inside each chapter.

## A complete example

A complete `book.yml` can therefore look like this:

```yaml
metadata:
  title: "My Technical Book"
  subtitle: "An Introduction"
  author: "Author Name"
  date: "2026"
  edition: "1st edition"

bibliography:
  file: "references.bib"
  style: "plain"

chapters:
  - title: Introduction
    principia:
      - introduction.md

  - title: Fundamentals
    principia:
      - variables.md
      - data_types.md

  - title: Advanced topics
    principia:
      - advanced.md
```

The `book.yml` file describes **what the book contains and how it is organised**.

It does not define the visual appearance of the publication. That responsibility belongs to Typus.

::pagebreak
::