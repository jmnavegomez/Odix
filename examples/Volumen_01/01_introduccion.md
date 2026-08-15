# Introduction

Odix is an open-source publishing system for technical books.

It allows authors to write their content using a simple Markdown-based syntax and organise it into small, independent Principia. Odix then transforms this source material into a structured document and generates the publication source using the selected publication style.

A book is organised through three main elements:

+ `book.yml` defines the structure and metadata of the book.
+ `Typus` defines the publication style.
+ `Principia` contain the actual content.

The basic workflow is:

```
Principia
    ↓
book.yml
    ↓
Odix
    ↓
LaTeX
    ↓
PDF
```

This guide explains how to create and publish a book with Odix, starting with the `build` command and progressively introducing the different elements available to the author.

The examples in this guide are intended to be practical and can be used as a starting point for creating your own Odix projects.

::pagebreak
::