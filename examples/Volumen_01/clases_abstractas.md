# Clases abstractas

## Introducción

Una clase abstracta es una clase que sirve como base para otras clases y que no está pensada para ser instanciada directamente. En Python las clases abstractas se implementan mediante las Abstract Base Class (ABC) proporcionadas por el módulo `abc`.

Una clase representa un concepto mediante sus propiedades y sus métodos. La abstracción consiste en quedarse con las características esenciales de un objeto y ocultar los detalles que no importan. En el proceso de abstracción se identifican las propiedades y métodos esenciales.

Cuando varias clases comparten comportamiento o representan variaciones de un mismo concepto, es habitual crear una clase padre de la que todas hereden las propiedades y métodos de esta.

Este enfoque permite modularizar y reutilizar el código dando como resultado un código más mantenible y flexible. Por lo tanto la herencia es una herramienta muy útil cuando existe una relación clara entre las clases.

Sin embargo, la herencia por sí sola no hace que las clases hijas implementen determinados métodos o propiedades. Es posible no definir alguno y que el error aparezca mucho más adelante durante la ejecución. Para evitar este problema existen las Abstract Base Class (ABC).

## Uso de las ABC

Una clase abstracta es una clase que sirve como base para otras clases y que puede obligar a sus clases derivadas a implementar determinados métodos o propiedades. En Python este comportamiento se implementa heredando de `ABC`. En el caso de no definir lo que la clase base indica que debe ser definido, se manda un mensaje de error y se para la ejecución del programa.

Dicho en otras palabras, la clase base obliga a sus hijas a seguir una guía que marca esa clase base. Es una garantía de que todas las clases derivadas implementan la interfaz definida por la clase abstracta. Así se puede asegurar que cada vez que se defina una clase hija de una de éstas clases todas sigan un patrón común.

Una vez definidas las clases hijas, se pueden crear funciones y métodos que reciban cualquier objeto de la clase base. Eso permite incluir todos los hijos de la clase base como entrada en esas funciones.

En caso de olvidarse de incluir alguna de las propiedades o métodos lanzará una excepción (TypeError) que impide crear el objeto, evitando que el programa continúe con una implementación incompleta. De este modo se garantiza que todas las clases derivadas implementan la interfaz definida por la clase abstracta, evitando implementaciones incompletas y errores difíciles de detectar durante la ejecución.

## Ejemplo

Para crear una clase abstracta basta con heredar de ABC, una clase incluida en el módulo abc de Python. 

Vamos con un ejemplo mecánico: Definimos una clase `Pieza` que representa en abstracto a cualquier pieza. La clase `Pieza` define la interfaz común que deberán implementar todas las piezas concretas.

Así se marcan las propiedades que deben tener las piezas con su tamaño y la herramienta que se usa y también el método de ensamblaje:

::pagebreak
::

```python

from abc import ABC, abstractmethod

class Pieza(ABC):

    @property
    @abstractmethod
    def tamaño(self):
        pass

    @property
    @abstractmethod
    def herramienta(self):
        pass

    @abstractmethod
    def ensamblar(self):
        pass
```

Definimos dos clases hijas nuevas de la clase `Pieza`: Las clases TuercaM8 y TornilloM8:

::pagebreak
::

```python
class TuercaM8(Pieza):

    @property
    def tamaño(self):
        return "M8"

    @property
    def herramienta(self):
        return "Llave inglesa de 13 mm"

    def ensamblar(self):
        print("Apretar a 50 N·m")
```

```python
class TornilloM8(Pieza):

    @property
    def tamaño(self):
        return "M8"

    @property
    def herramienta(self):
        return "Llave Allen"

    def ensamblar(self):
        print("Apretar con llave Allen")
```

Estas clases están completas porque definen todo lo que la clase base marca. Una clase incompleta sería:

::pagebreak
::

```python
class Remache(Pieza):

    @property
    def tamaño(self):
        return "4 mm"
```

A la que le faltan la propiedad herramienta y el método ensamblar. Para comprobar el funcionamiento se puede ejecutar:

```python
remache = Remache()
```

Lo cual lanzaría un error:

```bash
TypeError:
Can't instantiate abstract class Remache
with abstract methods herramienta, ensamblar
```

Como se puede ver, en caso de no cumplir las condiciones de la clase padre, no se puede seguir con el desarrollo.

Por otro lado, para usar en una función las clases no es necesario usar cada clase por separado como en este ejemplo:

```python
def montar(tuerca: TuercaM8):
    ...
```

Se puede hacer directamente una llamada a la clase base:

```python
def montar(pieza: Pieza):
    pieza.ensamblar()
```

Una vez que todas las clases cumplen la interfaz definida por la clase abstracta, pueden utilizarse indistintamente allí donde se espere un objeto del tipo Pieza. Este comportamiento se estudiará con detalle en la píldora dedicada al polimorfismo.

## Conclusión

Las clases abstractas no están pensadas para ser instanciadas directamente, sino para servir de base a otras clases.

Las ABC permiten definir unas pautas en el diseño. Convierten las decisiones de diseño en reglas que el propio lenguaje hace cumplir, reduciendo errores y facilitando el mantenimiento del código.

::pagebreak
::