# Principia

A `Principium` is the basic unit of content in an Odix book.

A Principium is a Markdown-based source file that contains part of the content of a publication. Principia are grouped into chapters through the `book.yml` configuration.

For example:

```text
my-book/
├── book.yml
├── typus.yml
├── introduction.md
├── variables.md
├── functions.md
└── ...
```

The files containing the content of the book are Principia.

## From Principium to publication

A Principium is not published directly.

Odix parses the source file and converts it into its internal document representation before generating the final publication.

The basic flow is:

```
Principium
↓
Lexer
↓
Parser
↓
Tabula
↓
Scriptorium
↓
LaTeX

```

This process allows Odix to treat the document as a structured publication rather than as a collection of formatted text.

## Writing a Principium

The source syntax of a Principium is based on Markdown.

For example: ` ```markdown`

# Variables

Variables allow a program to associate a name with a value.

```python
name = "Odix"
```

Odix extends this Markdown-based syntax with additional constructs for technical publications.

These extensions allow a Principium to contain elements such as:

- headings;
- paragraphs;
- emphasis;
- lists;
- quotations;
- source code;
- mathematical expressions;
- tables;
- images;
- captions and labels;
- citations;
- bibliography references.

## Principia and chapters

A Principium belongs to a chapter through the `principia` list in `book.yml`.

For example:

```yaml
chapters:
  - title: Python Fundamentals
    principia:
      - variables.md
      - data_types.md
      - functions.md
```

The order of the files determines their order within the chapter.

A Principium can therefore be kept small and focused on a single topic.

This makes it possible to build a larger book by combining independent pieces of content.

## Source files

Principia are ordinary text files and can be edited with any text editor.

They can therefore be version-controlled, reviewed and modified independently from the publication configuration.

The source material remains separate from the final LaTeX document.

## The role of Principia

A Principium describes the **content** of a publication.

`book.yml` describes the **structure** of the book.

Typus describes the **publication style**.

Together, these components allow Odix to separate the different concerns involved in producing a technical book.

The following sections describe the individual elements that can be used inside a Principium.

::pagebreak
::
