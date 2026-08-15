# Mathematics

Mathematical expressions can be included in a Principium using the mathematical syntax provided by Odix.

Odix supports both inline mathematical expressions and displayed mathematical blocks.

## Inline mathematics

An inline mathematical expression is enclosed between `$` symbols:

```text
$E = mc^2$
````

The expression is included as part of the surrounding text.

For example:

```text
The energy-mass relationship is given by $E = mc^2$.
```

Inline mathematics is useful when the mathematical expression is part of a sentence.

## Mathematical blocks

A mathematical expression can also be displayed as an independent block using the `::math` directive:

```text
::math
E = mc^2
::
```

The expression is rendered as a separate mathematical element in the published document.

For example:

```text
The energy-mass relationship is:

::math
E = mc^2
::
```

This is useful for equations that require their own space in the document.

## LaTeX expressions

Odix uses LaTeX as the mathematical representation of the generated publication.

This means that mathematical expressions can use standard LaTeX notation.

For example:

```text
::math
\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
::
```

More complex expressions can be written in the same way:

```text
::math
\int_0^1 x^2 \, dx = \frac{1}{3}
::
```

Odix preserves the mathematical expression when generating the LaTeX document.

## Mathematical content in a book

Mathematical expressions can be used in any Principium.

For example:

```text
# Quadratic equations

The solutions of a quadratic equation are given by:

::math
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
::
```

This allows technical and scientific content to be written directly alongside the mathematical expressions it requires.

## Summary

Odix provides two ways of writing mathematics:

+ inline expressions using `$...$`;
+ mathematical blocks using the `::math` directive.

Inline mathematics is intended for expressions that form part of a sentence, while mathematical blocks are intended for standalone expressions.

Mathematical expressions use LaTeX notation and are included directly in the generated LaTeX document.

::pagebreak
::