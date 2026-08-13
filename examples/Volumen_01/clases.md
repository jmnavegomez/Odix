# clases

## Introducción

Las clases son un tipo de elemento versátil usado en el paradigma de programación orientada a objetos (POO por sus siglas, que en inglés serían OOP). Python es un lenguaje multiparadigma. Aunque es posible programar utilizando únicamente funciones, también ofrece un potente modelo de programación orientada a objetos basado en clases.

Una clase es resultado del proceso de abstracción, en el que de uno o varios elementos se extraen los atributos y métodos principales y se agrupan sus atributos y comportamientos en un nuevo tipo de objeto. 

Un ejemplo de tipo integrado es `int`. Aunque habitualmente se piense en él simplemente como el tipo de los números enteros, en realidad `int` es una clase. Cada número entero (`1`, `2`, `3`, ...) es una instancia de dicha clase y dispone de operaciones propias, como la suma, la resta o la multiplicación, implementadas mediante los métodos especiales del tipo.

Como se ha explicado, un objeto es la instancia de una clase. Se pueden crear tantos objetos como se necesiten de una clase para llevar a cabo la ejecución del programa. Cada objeto posee sus propios atributos, mientras que comparte los métodos definidos por la clase. El objeto no añade características a la clase sino que la utiliza como patrón para ser creado y es único.

Las clases se emplean para simplificar y agrupar elementos que tienen un comportamiento similar con operaciones propias y diferentes de las que vienen por defecto para variables existentes. Suelen ser elementos más complejos que las variables básicas y suelen contener internamente como atributos variables u otras clases.

## Uso de las clases

Para definir una clase en Python se emplea la palabra clave `class`, seguida del nombre de la clase y dos puntos (`:`). Como cualquier otro bloque del lenguaje, el contenido de la clase se escribe con un nivel de indentación. Aunque el nombre puede ser el que el programador desee, se recomienda que sea descriptivo y siga la convención **PascalCase**, es decir, comenzando cada palabra por una letra mayúscula. Esta convención permite identificar rápidamente que se trata de una clase y diferenciarla de las funciones y variables, que normalmente se escriben en minúsculas utilizando ·snake_case·.

Dentro de la clase suele definirse, en primer lugar, el constructor. El constructor es un método especial denominado `__init__` que Python ejecuta automáticamente cuando se crea un nuevo objeto. Su función consiste en inicializar el estado del objeto, asignando los valores iniciales de sus atributos a partir de los parámetros recibidos.

Los atributos representan la información que almacena cada objeto. Habitualmente se crean dentro del constructor mediante la sintaxis `self.atributo`, aunque también pueden existir atributos de clase, que son compartidos por todas las instancias y se definen directamente dentro de la clase, fuera de cualquier método.

Además de almacenar información, las clases definen métodos. Los métodos son funciones asociadas a la clase que describen el comportamiento de sus objetos. Al invocarlos, pueden modificar el estado del objeto, consultar información o realizar cualquier otra operación relacionada con él.

Todos los métodos de instancia reciben como primer parámetro una referencia al propio objeto. Por convención, este parámetro recibe el nombre `self`. Aunque podría utilizarse cualquier identificador, el uso de self está completamente estandarizado en Python y debe respetarse. Gracias a este parámetro, un método puede acceder a los atributos y a otros métodos del mismo objeto sin necesidad de recibirlos como argumentos adicionales. En otras palabras, `self` representa el objeto sobre el que se está ejecutando el método.

Una vez definida la clase, es posible crear tantos objetos como sean necesarios. Este proceso recibe el nombre de instanciación y consiste en llamar a la clase como si fuera una función, proporcionando los argumentos que requiera su constructor.

Para acceder a los atributos o invocar un método de un objeto se utiliza el operador punto (`.`). Los atributos se consultan escribiendo `objeto.atributo`, mientras que los métodos se ejecutan mediante `objeto.metodo()`, proporcionando entre paréntesis los argumentos que dicho método necesite.

Por último, una clase puede heredar atributos y métodos de otra clase. Este mecanismo, conocido como **herencia**, permite reutilizar código y especializar comportamientos. En Python, la herencia se indica escribiendo el nombre de la clase padre entre paréntesis tras el nombre de la clase hija, por ejemplo: `class claseHija(clasePadre):`.

## Ejemplo

Esta es la clase Node del proyecto que inspira la colección de libros de Python Real: 

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

Esta es una clase que hereda los atributos y métodos de la clase ABC que se utiliza para clases abstractas. `ABC` es una clase de la biblioteca estándar utilizada para crear clases abstractas. En esta colección se estudiará más adelante con detalle, por lo que, por ahora, basta con saber que `Node` hereda de ella.

En este ejemplo pueden identificarse fácilmente los principales elementos de una clase. La declaración `class Node(ABC):` indica el nombre de la clase y que hereda de `ABC`. El método `__init__` es el constructor, encargado de inicializar los atributos `id`, `parent` y `children`. Finalmente, los métodos `add_child()` y `remove_child()` implementan parte del comportamiento del objeto, permitiendo modificar la estructura del árbol.

::pagebreak
::

Para que quede más claro, el esquema sería:
```text
class Node(ABC)
↑
La clase hereda de ABC

↓

__init__
↑
Constructor

↓

self.id
self.parent
self.children
↑
Atributos

↓

add_child
↑
Método
```

## Conclusión

Las clases permiten definir nuevos tipos de objetos adaptados a las necesidades del programa.

Estas clases se instancian en objetos que son concreciones de la clase y que representan una instancia concreta del tipo definido por la clase.

Tienen una estructura propia que las hace reconocibles, pero el nombre es a elección del programador y se recomienda usar mayúscula en la primera del nombre explicativo.

::pagebreak
::