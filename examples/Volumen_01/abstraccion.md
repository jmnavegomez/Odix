# Abstracción

## Introducción

La abstracción es uno de los pilares fundamentales de la Programación Orientada a Objetos (POO). Consiste en representar una entidad del problema mediante una clase que recoge únicamente las características y comportamientos relevantes para el contexto, ignorando los detalles que no aportan información útil.

En otras palabras, una abstracción es un modelo simplificado de un objeto real o conceptual.

La abstracción permite construir modelos más sencillos y fáciles de comprender. Al centrarse únicamente en los aspectos importantes de cada entidad, el código resulta más claro, reutilizable y sencillo de mantener.

Además, facilita el diseño de programas complejos, ya que permite dividir un problema en objetos que representan conceptos bien definidos y con responsabilidades concretas.

## Uso de la abstracción

La abstracción comienza identificando las entidades que forman parte del problema que se quiere resolver.

Una vez identificadas, se determina qué información debe almacenar cada una y qué operaciones debe realizar. Esa información se convierte en los atributos de la clase y esas operaciones en sus métodos.

No existe una única abstracción correcta. La forma de modelar una entidad depende del problema que se desea resolver y de la información que resulte relevante en cada caso. Dependiendo del objetivo del programa, una misma entidad puede representarse mediante clases diferentes.

Por ejemplo, una clase Libro puede contener el título, el autor y el ISBN, ya que son características relevantes para una biblioteca. Sin embargo, no es necesario representar el número de fibras del papel o el color exacto de la tinta, porque esa información no resulta útil para ese contexto.

## Ejemplo

En este capítulo no es necesario comprender todos los detalles del código; basta con observar cómo la clase representa las características comunes a todos los nodos del árbol.

En Odix todos los elementos del árbol sintáctico (AST) se representan mediante nodos. Aunque existen distintos tipos de nodos, todos comparten unas características comunes: poseen un identificador, conocen su nodo padre y almacenan sus nodos hijos.

Esta idea se representa mediante la siguiente abstracción:

```python
class Node(ABC):
    def __init__(self, node_id: str) -> None:
        self.id = node_id
        self.parent: Node | None = None
        self.children: list[Node] = []
```

La clase `Node` no representa un párrafo, una tabla o un encabezado concreto. Representa el concepto general de nodo de un árbol sintáctico, definiendo únicamente las características comunes a todos ellos.

Posteriormente, otras clases derivadas heredarán de ella para añadir el comportamiento específico de cada tipo de nodo.

## Conclusión

La abstracción consiste en construir modelos simplificados de las entidades del problema, conservando únicamente la información y el comportamiento necesarios para el contexto. Suele ser el primer paso en el diseño orientado a objetos, ya que permite identificar las clases que formarán parte del programa y definir sus responsabilidades antes de comenzar su implementación.

::pagebreak
::