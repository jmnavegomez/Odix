# Figures

Figures can be included in a Principium using the `::figure` directive.

A figure is defined by its source file:

```text
::figure
img/python.png (path)
::
```

The path is interpreted relative to the Principium containing the directive.

For example, a project can be organised as follows:

```
my-book/
├── book.yml
├── typus.yml
├── introduction.md
├── figures.md
└── img/
└── python.png

```

The figure can then be referenced from `figures.md` with:

```
::figure
img/python.png (path)
::
```

## Figure size

Odix publishes figures using the available width and height of the document while preserving their original aspect ratio.

This allows figures to adapt to the page without being distorted.

The generated LaTeX uses the document dimensions to constrain the figure:

```
\includegraphics[
width=\textwidth,
height=\textheight,
keepaspectratio
]{...}

```

The figure therefore keeps its original proportions while fitting within the available document area.

## Captions

A figure can have a caption.

Captions describe the content of a figure and are included as part of the figure in the published document.

For example:

```
::figure
img/python.png (path)
Python logo (caption)
::
```

The caption is rendered below the figure in the generated publication.

## Labels

A figure can also have a label that can be used to identify it within the document:

```
::figure
img/python.png (path)
Python logo (caption)
fig-python (label)
::
```

The label provides an identifier for the figure and can be used by other document elements that reference it.

## Figures in a book

Figures can be used in any Principium of a book.

For example:

```text
my-book/
├── book.yml
├── typus.yml
├── chapter.md
├── another_chapter.md
└── img/
    ├── python.png
    └── architecture.png
```

Each Principium can reference the figures it needs.

Keeping figures in a separate directory makes the structure of the publication easier to maintain and keeps the source content organised.

## Summary

The `::figure` directive provides the basic mechanism for adding figures to a Principium.

A figure can define:

+ its source file;
+ a caption;
+ a label.

Odix takes care of adapting the figure to the dimensions of the published document while preserving its proportions.

::pagebreak
::