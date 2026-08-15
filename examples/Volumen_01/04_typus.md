# Typus

Typus defines the publication style of an Odix book.

While `book.yml` describes the structure and content of the publication, Typus defines how that publication is rendered as a document.

A Typus configuration is provided to Odix through a YAML file.

## Basic usage

A Typus configuration is passed to the `build` command with the `--typus` option:

```
odix build book.yml --typus typus.yml
```

The same book can therefore be built using different Typus configurations without modifying its `book.yml` or its Principia.

## Document configuration

The main document properties are defined under the `document` section.

```yaml
document:
  document_class: book
  page_size: a5paper
  orientation: portrait
  font_size: 11pt
  font: helvetica
  language: spanish
```

These properties control the fundamental characteristics of the generated document.

### Document class

The `document_class` property specifies the LaTeX document class:

```yaml
document:
  document_class: book
```

### Page size

The `page_size` property defines the size of the publication:

```yaml
document:
  page_size: a5paper
```

### Orientation

The document can use portrait or landscape orientation:

```yaml
document:
  orientation: portrait
```

### Typography

The `font` and `font_size` properties define the document typography:

```yaml
document:
  font: helvetica
  font_size: 11pt
```

### Language

The `language` property defines the document language:

```yaml
document:
  language: spanish
```

## Margins

Page margins are defined through the `margins` section:

```yaml
document:
  margins:
    top: 2cm
    bottom: 1.5cm
    left: 1.5cm
    right: 1.5cm
```

Each margin is specified independently.

## Page layout

Typus also provides options related to the layout of the publication:

```yaml
document:
  twoside: true
  chapters_start_on_odd_page: true
```

`twoside` enables two-sided document layout.

`chapters_start_on_odd_page` controls whether chapters begin on odd pages.

## Line spacing

The line spacing can be configured with:

```yaml
document:
  line_spacing: 1.25
```

## Table of contents and page numbering

Typus can configure the table of contents and page numbering:

```yaml
document:
  table_of_contents: true
  page_numbering: true
  page_numbering_position: top
```

These options control the corresponding elements of the generated publication.

## LaTeX packages

Additional LaTeX packages can be specified in the configuration:

```yaml
document:
  packages:
    - inputenc
    - fontenc
    - graphicx
    - amsmath
    - xcolor
    - setspace
    - titlesec
    - tcolorbox
    - colortbl
```

The packages are included in the generated LaTeX preamble.

## Complete example

A Typus configuration can therefore look like this:

```yaml
document:
  document_class: book
  page_size: a5paper
  orientation: portrait

  margins:
    top: 2cm
    bottom: 1.5cm
    left: 1.5cm
    right: 1.5cm

  font: helvetica
  font_size: 11pt
  line_spacing: 1.25

  twoside: true
  chapters_start_on_odd_page: true

  table_of_contents: true
  page_numbering: true
  page_numbering_position: top

  language: spanish

  packages:
    - inputenc
    - fontenc
    - graphicx
    - amsmath
    - xcolor
    - setspace
    - titlesec
    - tcolorbox
    - colortbl
```

Typus keeps publication style separate from book structure. This allows the content of an Odix book to remain independent from the specific document configuration used to publish it.

::pagebreak
::