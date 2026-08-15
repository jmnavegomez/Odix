# Building a book

Once a book has been configured, Odix can generate its publication source using the `build` command.

The `build` command is the main entry point for the publication workflow.

## Basic usage

From the directory containing the book configuration, run:

```
odix build book.yml --typus typus.yml
```

The command receives two configuration files.

The `book.yml` file defines the structure and metadata of the book.

The `typus.yml` file defines how the book should be published, including properties such as page size, margins, typography and document settings.

The `--typus` option specifies the Typus configuration to use.

## Output

When the build completes successfully, Odix generates a LaTeX document containing the complete book.

The generated file can then be compiled with a LaTeX distribution to produce the final PDF.

The publication workflow is therefore:

```
book.yml + typus.yml
↓
odix build
↓
LaTeX
↓
PDF

```

## Project structure

A minimal Odix project can be organised as follows:

```
my-book/
├── book.yml
├── typus.yml
├── introduction.md
└── ...
```

From the `my-book` directory, the book can be built with:

```

odix build book.yml --typus typus.yml

```

The paths passed to `build` can also point to files in different locations. This makes it possible to keep the book source and the publication style separately when required.

## The build process

The `build` command brings together the different components of Odix.

The book configuration is first loaded into the internal representation of the publication. The Principia are then parsed and compiled, while Typus provides the document style used by Impressio.

The result is a complete LaTeX document ready for compilation.

In simplified form:

```
Principia
    ↓
Tabula
    ↓
Ordinatio + Typus
    ↓
Impressio
    ↓
LaTeX
```

The `build` command therefore does not directly generate the final PDF. It generates the LaTeX source from which the PDF can subsequently be compiled.

::pagebreak
::