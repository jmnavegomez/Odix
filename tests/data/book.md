# Introducción

En programación orientada a objetos (POO) las clases se componen principalmente de atributos y métodos. Los atributos son variables asociadas a una clase o a una instancia que almacenan información sobre su estado o sus características.

Los atributos de instancia suelen inicializarse en el método especial `__init__`, aunque también pueden añadirse posteriormente mediante asignación. `__init__` es el método especial encargado de inicializar una instancia recién creada, mientras que la creación del objeto corresponde a `__new__`.

Hay dos tipos principales de atributos: atributos de instancia y atributos de clase. Los de instancia son propios de cada objeto y normalmente obtienen su valor durante la instanciación. Por su parte, los atributos de clase son los que comparten todos los objetos y que pertenecen a la clase.

# Uso de los atributos

La definición de los atributos de instancia y de clase se realiza de forma diferente. Para los atributos de instancia se accede al propio objeto, habitualmente mediante `self`, continuado por un punto y el nombre del atributo y asignando un valor. Mientras que para los atributos de clase basta con nombrar el atributo y asignarle un valor.

Una vez que tienen un valor asignado se pueden modificar accediendo a la propiedad y asignando el nuevo valor de la forma: `objeto.atributo = valor_asignado`.

Tanto las clases como las instancias disponen del atributo especial `__dict__`, que almacena sus atributos en forma de diccionario. Python utiliza estos diccionarios durante la búsqueda de atributos.

Python busca primero un atributo en el `__dict__` de la instancia. Si no lo encuentra, continúa la búsqueda en el `__dict__` de la clase y, posteriormente, en las clases padre si existen.

El shadowing consiste en crear un atributo de instancia con el mismo nombre que un atributo de clase. De este modo, al acceder al atributo desde esa instancia, Python utiliza el atributo de instancia y oculta el de clase.