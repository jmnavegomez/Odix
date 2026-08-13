# Programación Orientada a Objetos

## Introducción

En la programación clásica, el paradigma que más se repetía era la programación estructurada. Consistía en escribir código con instrucciones que se ejecutaban una detrás de otra. La Programación Orientada a Objetos (POO) consiste en el uso de Objetos como paradigma central. 

La programación orientada a objetos surgió como una forma de modelar sistemas complejos mediante objetos que representan entidades del problema. En lugar de organizar el programa únicamente como una secuencia de instrucciones, organiza el código alrededor de objetos que encapsulan datos y comportamiento.

Para ello utiliza clases, que definen la estructura y el comportamiento de un tipo de objeto mediante atributos y métodos. Un objeto es una instancia concreta de esa clase cuyos atributos poseen valores determinados.

## Uso de la POO

La POO requiere de la creación de clases. Estas clases contienen variables llamadas atributos que al instanciar los objetos obtienen un valor propio de ese objeto y unos métodos que son funciones que hacen uso de los atributos internos del objeto junto con parámetros que se le pasen.

Una vez se tiene programada la clase, los objetos pueden modificar los atributos y emplear los métodos de la clase para poder realizar acciones, modificaciones o almacenar información.

La POO se compone de varios tipos de elementos:
- las clases
- los atributos
- los métodos

Las clases son el modelo base de los objetos. Los atributos son variables que almacenan el estado de un objeto. Y los métodos son funciones propias de la clase que usan los objetos empleando atributos o no.

En cuanto a las bases de la POO, tiene cuatro pilares:
- La abstracción
- La herencia
- La encapsulación
- El polimirfismo

La herencia es un proceso de especialización de las clases. La abstracción consiste en representar una entidad del problema mediante una clase que recoge únicamente los atributos y métodos relevantes para el contexto. La encapsulación consiste en controlar el acceso al estado interno de un objeto mediante una interfaz pública. Finalmente, el polimorfismo es el poder utilizar una misma interfaz para trabajar con objetos de distintos tipos.

Además de estos pilares, la composición es un mecanismo fundamental muy utilizado para construir objetos complejos reutilizando otros objetos.

## Ejemplo

A lo largo de esta colección se utilizarán fragmentos reales del código de Odix. En este capítulo no es necesario comprender todos los detalles; su propósito es mostrar el aspecto que tiene una clase real. Cada uno de los conceptos empleados se estudiará en los capítulos siguientes.

::pagebreak
::

``` python
class Node(ABC):
    """Base class for all Tabula nodes.

    Every element of the AST inherits from this class. A node stores its
    position in the tree, its children and its unique identifier.

    Attributes:
        id: Unique node identifier.
        parent: Parent node. ``None`` if this node is the root.
        children: Child nodes.
    """

    def __init__(self, node_id: str) -> None:
        """Initializes a new node.

        Args:
            node_id: Unique identifier of the node.
        """
        self.id = node_id
        self.parent: Node | None = None
        self.children: list[Node] = []

    def add_child(self, child: Node) -> None:
        """Adds a child node.

        Args:
            child: Node to attach.
        """
        child.parent = self
        self.children.append(child)

    def remove_child(self, child: Node) -> None:
        """Removes a child node.

        Args:
            child: Child node to remove.

        Raises:
            ValueError: If the node is not a child of this node.
        """
        self.children.remove(child)
        child.parent = None
```

En esta clase aparecen varios de los conceptos de POO y de otros temas. Al final de la colección el lector podrá escribir su propio código con todos los conceptos incluidos en el código de Odix.

## Conclusión

La programación orientada a objetos permite organizar el software mediante clases y objetos que encapsulan datos y comportamiento. A partir de estos conceptos se construyen programas más modulares, reutilizables y fáciles de mantener. En los siguientes capítulos se estudiará cada uno de los elementos fundamentales que forman este paradigma.

::pagebreak
::