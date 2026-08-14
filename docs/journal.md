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


## 30/07/2026

Continuación del desarrollo del núcleo de Tabula y de la gramática de Principia.

Ampliación progresiva del lexer y del parser para soportar los distintos elementos del lenguaje enriquecido de Odix.

Implementación y pruebas de nuevas estructuras del AST y de las reglas correspondientes del parser.

## 31/07/2026

Desarrollo de las directivas de Odix para incorporar elementos que no pueden expresarse únicamente mediante Markdown convencional.

Implementación de directivas para matemáticas, saltos de página, imágenes, captions, notas, referencias y bibliografía.

Definición de la sintaxis de citas y referencias dentro de Principia.

## 01/08/2026

Desarrollo del Scriptorium como compilador del AST de Tabula.

Implementación de `MarkupVisitor` y de la generación de marcado LaTeX a partir de los nodos de Tabula.

Integración progresiva de los distintos nodos del AST con su representación LaTeX.

## 02/08/2026

Continuación de la generación de documentos LaTeX.

Implementación de elementos matemáticos inline y de bloques matemáticos.

Revisión de la representación de código, tablas, citas, imágenes y otros elementos del documento.

## 03/08/2026

Definición de Typus como componente responsable de la identidad visual de la publicación.

Implementación de la configuración del documento mediante YAML.

Definición de márgenes, tamaño de página, orientación, tipografía, interlineado, paquetes y otras propiedades de publicación.

Creación de la configuración Typus por defecto para el desarrollo del sistema.

## 04/08/2026

Desarrollo de Ordinatio para representar la estructura editorial de un libro.

Definición de `Book`, `Chapter` y `Principium`.

Implementación del cargador YAML para construir un libro a partir de `book.yml`.

Separación entre la estructura editorial del libro y el contenido individual de los Principia.

## 05/08/2026

Desarrollo de Impressio como componente encargado de publicar el libro.

Integración de Ordinatio y Typus con el proceso de generación de LaTeX.

Implementación de la generación del preámbulo y del documento completo.

Primeras publicaciones completas de libros mediante el flujo de Odix.

## 06/08/2026

Integración de metadatos en la configuración de la publicación.

Definición de los metadatos del libro:

- título;
- subtítulo;
- autor;
- fecha;
- edición.

Implementación de una página inicial específica para los metadatos de la publicación.

## 07/08/2026

Integración de imágenes en la publicación.

Definición de la representación de las figuras y de sus elementos asociados.

Revisión de captions y labels para figuras, tablas y bloques matemáticos.

## 08/08/2026

Desarrollo de la bibliografía del libro.

Definición de la configuración bibliográfica dentro de `book.yml`.

El libro puede especificar el archivo `.bib` y el estilo bibliográfico.

Integración de las referencias y citas con la generación de LaTeX mediante:

```text
\bibliographystyle{...}
\bibliography{...}
```

y las correspondientes citas mediante `\cite{...}`.

Comprobación del proceso completo de compilación LaTeX + BibTeX.

## 09/08/2026

Revisión de la estructura final de publicación y de los ejemplos.

Preparación de un libro completo de ejemplo para validar el flujo editorial de Odix.

La colección de ejemplo `Desarrollo Real Python` pasa a utilizar la configuración de libro mediante `book.yml`, incluyendo metadatos, bibliografía y capítulos.

## 10/08/2026

Revisión del formato de publicación del libro.

Ajustes de tamaño de página, márgenes, tipografía, interlineado y estructura de capítulos.

Preparación de una primera versión extensa del libro de ejemplo y revisión visual del PDF generado.

## 11/08/2026

Revisión de la arquitectura de publicación y del funcionamiento de Odix como herramienta editorial.

Definición de la colección de libros y de la estrategia de escritura mediante píldoras independientes.

Continuación del desarrollo de los contenidos de `Desarrollo Real Python`.

## 12/08/2026

Revisión final del formato del libro.

Comprobación visual del PDF generado a partir de las píldoras de contenido.

Revisión de imágenes, captions, labels, matemáticas y estructura editorial.

El flujo de generación produce documentos LaTeX y PDF con el formato esperado.

## 13/08/2026

Preparación de la limpieza del paquete para su primera publicación.

Revisión de la arquitectura del proyecto y eliminación de componentes que todavía no aportan funcionalidad real.

Se decide mantener únicamente el backend de publicación que actualmente está implementado: LaTeX.

Revisión de la estructura de tests y corrección de los tests que habían quedado asociados a versiones anteriores de la arquitectura.

## 14/08/2026

Finalización de la limpieza del paquete para la versión `0.1.0`.

Revisión y actualización de los tests del sistema.

Se reorganizan los tests de Ordinatio para reflejar la estructura actual de `Book`, `Chapter` y `Principium`.

Eliminación de tests que dependían de configuraciones antiguas del proyecto.

Resultado de la limpieza:

```text
94 tests passed
```

Revisión de los componentes de publicación y eliminación de renderers vacíos que habían sido creados como una abstracción para futuros backends.

La publicación actual queda centrada en LaTeX mediante Impressio.

## 14/08/2026 — CLI

Implementación de la interfaz de línea de comandos de Odix.

El comando principal queda definido como:

```text
odix
```

con el subcomando:

```text
odix build
```

El comando `build` recibe el archivo `book.yml` y la configuración Typus mediante:

```text
odix build book.yml --typus typus.yml
```

Primera prueba satisfactoria del CLI utilizando el libro de ejemplo.

El comando genera correctamente el documento LaTeX.

## 14/08/2026 — Preparación de la primera distribución

Revisión del `pyproject.toml` para preparar la distribución de Odix.

Definición de la versión inicial:

```text
0.1.0
```

Configuración del sistema de build mediante Hatchling.

Definición del entry point del CLI:

```text
odix = odix.cli:main
```

Configuración de Ruff y Black para mantener unas reglas de calidad y formato consistentes.

Revisión del README y adaptación de su contenido al estado real de Odix `0.1.0`.

Preparación de la licencia GPLv3 y de la documentación inicial del proyecto.

## 14/08/2026 — Revisión de la documentación

Revisión de `README.md`, `PHILOSOPHY.md` y la documentación contenida en `docs/`.

Se mantiene el journal como registro histórico de la evolución del proyecto.

Revisión de la arquitectura del parser y confirmación de que la documentación sigue siendo coherente con la implementación actual.

Revisión del roadmap y actualización progresiva de los hitos completados.

## 14/08/2026 — Estado del proyecto

Odix alcanza su primer estado funcional completo como herramienta de publicación técnica.

El flujo actualmente implementado permite:

```text
Principia
    ↓
Lexer
    ↓
Parser
    ↓
Tabula
    ↓
Scriptorium
    ↓
Ordinatio
    ↓
Typus
    ↓
Impressio
    ↓
LaTeX
    ↓
PDF
```

El sistema permite estructurar un libro mediante `book.yml`, definir su estilo mediante Typus y generar un documento LaTeX completo con metadatos, imágenes, matemáticas, citas y bibliografía.

La primera versión del CLI permite ejecutar este proceso desde la línea de comandos.

El proyecto queda preparado para la siguiente fase: construir y revisar el paquete distribuible, publicar el repositorio en GitHub y preparar la primera publicación de Odix en PyPI.
