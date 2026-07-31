# Arquitectura del Parser de Tabula

## Objetivo

El parser transforma la secuencia de tokens producida por el lexer en un Árbol de Sintaxis Abstracta (AST) de Tabula.

Su responsabilidad es exclusivamente interpretar la estructura semántica del documento y construir los nodos correspondientes del AST.

No realiza tareas relacionadas con la representación visual, el estilo o la generación de documentos.

---

# Filosofía

El parser se ha diseñado siguiendo un enfoque de **parser recursivo descendente (recursive descent parser)**.

Cada regla del lenguaje se implementa mediante una función independiente.

Cada función tiene una única responsabilidad:

* consumir los tokens correspondientes;
* construir un nodo del AST;
* devolver dicho nodo.

No existen clases para las reglas del parser, ya que las reglas no mantienen estado propio.

Todo el estado del análisis reside en la clase `Parser`.

---

# Separación entre Parser y reglas

La clase `Parser` contiene únicamente la infraestructura necesaria para recorrer la secuencia de tokens.

Entre sus responsabilidades se encuentran:

* almacenar la lista de tokens;
* mantener la posición actual;
* avanzar por los tokens;
* comprobar el token actual;
* consumir tokens esperados;
* iniciar el proceso de análisis.

Las reglas del lenguaje se implementan fuera de `Parser`.

Esta separación permite que la clase permanezca pequeña y que cada regla pueda evolucionar de forma independiente.

---

# Organización de las reglas

Las reglas se agrupan dentro del directorio:

```text
parser/
└── rules/
```

Actualmente existen dos niveles de análisis:

* bloques;
* elementos inline.

Cada nivel dispone de un *dispatcher* encargado de decidir qué regla ejecutar.

Conceptualmente:

```text
parse_block()
```

decide qué bloque comienza en la posición actual.

Mientras que:

```text
parse_inline()
```

decide qué elemento inline comienza en la posición actual.

---

# Dispatchers

Los archivos:

```text
blocks.py
inline.py
```

no construyen nodos del AST.

Su única responsabilidad consiste en seleccionar la regla adecuada en función del token actual.

Por ejemplo:

```text
HASH
```

se delega en:

```text
parse_section()
```

mientras que:

```text
TEXT
```

se delega en:

```text
parse_text()
```

Esta separación mantiene los *dispatchers* extremadamente sencillos y facilita añadir nuevas reglas sin modificar las existentes.

---

# Constructores del AST

Cada nodo concreto del AST dispone de una función responsable de construirlo.

Ejemplos:

```text
Paragraph  ← parse_paragraph()

Section    ← parse_section()

Text       ← parse_text()

Bold       ← parse_bold()

Image      ← parse_image()
```

Existe una correspondencia prácticamente uno a uno entre los nodos del AST y las funciones del parser.

Esta simetría simplifica tanto el mantenimiento como la ampliación del lenguaje.

---

# Separación entre bloques e inline

El parser sigue exactamente la misma jerarquía definida por el AST.

```text
Document
│
└── Block
    │
    └── Inline
```

Por tanto, el proceso de análisis también se organiza en niveles:

```text
Document
    ↓

parse_block()

    ↓

parse_paragraph()

    ↓

parse_inline()

    ↓

parse_text()
```

Cada nivel únicamente conoce el inmediatamente inferior.

Un bloque nunca crea directamente nodos inline.

Por ejemplo, `parse_paragraph()` no construye nodos `Text`.

En su lugar delega esta responsabilidad en `parse_inline()`.

Esta decisión mantiene una clara separación de responsabilidades y evita el acoplamiento entre niveles del árbol.

---

# Funciones frente a clases

Las reglas del parser se implementan mediante funciones y no mediante clases.

Las razones son:

* no mantienen estado;
* reciben toda la información necesaria mediante la instancia de `Parser`;
* resultan más sencillas de leer;
* facilitan la extensión del parser mediante nuevas reglas.

De este modo, la inteligencia del parser reside en la colaboración entre la clase `Parser` y un conjunto de funciones especializadas.

---

# Evolución incremental

El parser se desarrollará de forma incremental.

Cada nueva regla añadirá una única característica al lenguaje.

Por ejemplo:

1. párrafos con texto;
2. encabezados;
3. texto en negrita;
4. cursiva;
5. código inline;
6. enlaces;
7. imágenes;
8. tablas;
9. bloques matemáticos.

Cada paso dispondrá de sus propios tests antes de continuar con la siguiente funcionalidad.

---

# Responsabilidades

La distribución de responsabilidades queda resumida de la siguiente forma:

| Componente       | Responsabilidad                                           |
| ---------------- | --------------------------------------------------------- |
| `Lexer`          | Transformar caracteres en tokens.                         |
| `Parser`         | Gestionar el recorrido de los tokens.                     |
| `parse_block()`  | Seleccionar la regla de bloque adecuada.                  |
| `parse_inline()` | Seleccionar la regla inline adecuada.                     |
| `parse_*()`      | Construir un nodo concreto del AST.                       |
| `Node`           | Gestionar la estructura del árbol y el cálculo de hashes. |

---

# Evolución futura

A medida que el número de reglas aumente, se prevé reorganizar el directorio `rules` para separar explícitamente los *dispatchers* de las reglas de construcción del AST.

La organización prevista será similar a:

```text
rules/
│
├── dispatchers/
│   ├── blocks.py
│   └── inline.py
│
├── blocks/
│   ├── headings.py
│   ├── paragraphs.py
│   ├── tables.py
│   └── ...
│
└── inline/
    ├── text.py
    ├── emphasis.py
    ├── links.py
    └── ...
```

Esta reorganización será únicamente estructural y no modificará el comportamiento del parser.

