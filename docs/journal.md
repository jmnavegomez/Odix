## 16/07/2026

Creación de la estructura principal de la colección de libros Desarrollo Real Python.

Consolidación de la estructura del proyecto de software libre.

Definido el procedimiento de compilación de los libros.

Siguiente objetivo: redactar el manifiesto y establecer los primeros hitos del roadmap.

## 17/07/2026

Redacción de PHILOSOPHIAE.md, que recoge la filosofía del proyecto y sustituye al manifiesto tradicional.

Redacción del README.md con las principales características del software, instrucciones de instalación, licencia y demás información del proyecto.

Cambio del nombre del proyecto de PyBook a Principia.

El nombre fue elegido por ser la palabra que identifica la obra *Philosophiæ Naturalis Principia Mathematica*, conocida simplemente como los *Principia*.

Además de hacer referencia a las ideas y los principios, el proyecto adopta la terminología latina tradicional de las distintas fases de creación de un libro.

## 18/07/2026

Búsqueda del nombre Principia en PyPI y en github. El nombre está cogido lo que lleva a cambiar el nombre del proyecto sin modificar la filosofía.

Replanteamiento de la utilidad del proyecto y el objetivo de su creación.

El objetivo de creación del proyecto es mostrar cómo hacer un proyecto desde cero mediante la colección de libros.

Es un proyecto que busca cubrir una necesidad que tengo en este momento para realizar la edición de forma personalizada.

## 20/07/2026

Selección del nombre Odix (Odisea del Codex) como nombre para el proyecto. Se puede cambiar en caso de estar cogido ya.

Cambios en la filosofía y comienzo con la escritura del pyproject.toml.

Toma de decisiones sobre Tabula(AST) y el markdown para ser analizado por el Parser, Lexer y Tabula.

## 21/07/2026

Establecer los hitos del roadmap.

## 22/07/2026

Movidos Lexer, Parser y clases AST a Tabula para que represente todo el proceso semántico previo a pasar al Scriptorium.

Investigación sobre arquitectura de Pandoc y de los compiladores.

Decisión de poner conceptualmente Scriptorium en la parte superior del proyecto como el que orquesta los procesos pero en el mismo nivel que el resto de herramientas a nivel arquitectura de software porque es más sencillo de implementar a nivel software.

## 23/07/2026

Escritura del script con la clase base nodes.py para la generación de Tabula.

Decisión de usar un número identificador con un número con puntos por cada nivel que avanza (Título:id = 1, Párrafo del Título:id = 1.1) y empleo del Hash como elemento de búsqueda y de análisis de textos iguales.

Determinar el Hash para contenido y contexto.

Hacer píldoras sobre los distintos temas para explicar posteriormente.