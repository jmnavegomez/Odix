## 16/07/2026

Creación de la estructura principal de la colección de libros Desarrollo Real Python.

Consolidación de la estructura del proyecto de software libre.

Definido el procedimiento de compilación de los libros.

Siguiente objetivo: redactar el manifiesto y establecer los primeros hitos del roadmap.

## 17/07/2026

Redacción de PHILOSOPHIAE.md, que recoge la filosofía del proyecto y sustituye al manifiesto tradicional.

Redacción del README.md con las principales características del software, instrucciones de instalación, licencia y demás información del proyecto.

Cambio del nombre del proyecto de PyBook a Principia.

El nombre fue elegido por ser la palabra que identifica la obra ·Philosophiæ Naturalis Principia Mathematica·, conocida simplemente como los ·Principia·.

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

## 29/07/2026

Definición de la arquitectura base del AST de Tabula.

Creación de la clase abstracta `Node` como núcleo del árbol de sintaxis abstracta, concentrando toda la funcionalidad común de los nodos.

Implementación de un sistema de identificadores incrementales para cada nodo mediante un contador interno de clase.

Decisión de calcular dinámicamente la posición estructural de cada nodo (`path`) en lugar de almacenarla, evitando inconsistencias al modificar el árbol.

Diseño de un sistema de integridad basado en dos hashes:
- `content_hash`, que representa únicamente el contenido semántico del nodo.
- `context_hash`, calculado a partir del `content_hash` propio y de los `context_hash` de sus hijos, formando un árbol de Merkle.

Decisión de que cada nodo defina únicamente su contenido semántico mediante el método abstracto `content()`, dejando el cálculo de hashes completamente implementado en la clase base `Node`.

Definición de la jerarquía principal del AST:
- `Node`
- `Document`
- `Block`
- `Inline`

Separación de los metadatos del árbol sintáctico mediante la creación de la clase `Metadata`, que no hereda de `Node`.

Decisión de almacenar los metadatos como pares clave-valor cargados directamente desde `principia.yml` mediante `**kwargs`, permitiendo una estructura flexible e independiente del esquema concreto del archivo YAML.

Implementación de una interfaz de acceso a metadatos similar a un diccionario (`get`, `__getitem__`, `__setitem__` y `__contains__`).

Comienzo de la implementación de la clase `Document`, definiéndola como nodo raíz del AST y delegando la representación semántica de los metadatos en la clase `Metadata`.

Siguiente objetivo: implementar las clases base `Block` e `Inline` y comenzar la definición de los primeros nodos del AST.