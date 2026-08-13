# Métodos especiales

## Introducción

Existen determinadas operaciones del lenguaje Python cuyo comportamiento está definido por el propio intérprete. Por ejemplo, cuando se evalúa la expresión `a + b`, Python debe decidir qué operación realizar sobre ambos objetos. Los métodos que permiten definir cómo debe comportarse un objeto cuando participa en estas operaciones reciben el nombre de métodos especiales o ·dunder methods· (de double underscore methods). También se conocen como métodos mágicos (magic methods), aunque el término dunder methods es el más utilizado actualmente.

Los métodos especiales permiten que los objetos personalizados se integren con el propio lenguaje Python. Gracias a ellos, un objeto puede comportarse como una cadena, una lista, un número o cualquier otro tipo compatible con las operaciones del lenguaje.

Gracias a los métodos especiales es posible:

- Personalizar la representación textual de un objeto.
- Comparar objetos entre sí.
- Sobrecargar operadores como `+`, `-` o `*`.
- Hacer que un objeto sea iterable.
- Permitir que pueda utilizarse con `len()`.
- Convertir un objeto en una función invocable.
- Gestionar el acceso a atributos.
- Implementar gestores de contexto (`with`).

En lugar de crear funciones específicas para cada una de estas operaciones, Python utiliza un conjunto estandarizado de métodos especiales que el intérprete invoca automáticamente cuando son necesarios.

## Uso de los dunder methods

Los métodos especiales no suelen llamarse directamente. Cuando se emplean determinadas funciones integradas de Python, como `len()` o `str()`, el intérprete invoca automáticamente el método especial correspondiente.

Algunos métodos especiales son invocados mediante funciones integradas de Python, mientras que otros se ejecutan automáticamente al utilizar operadores o determinadas construcciones del lenguaje:

**No todos los métodos especiales son llamados por una función de Python**. Algunos son invocados por funciones como `len()` o `str()`, mientras que otros son activados automáticamente por el intérprete al utilizar operadores (`+`, `==`, `[]`) o determinadas construcciones del lenguaje (`with`, acceso a atributos, iteración, etc.).

Buenas prácticas a la hora de usar estos métodos son:

- Implementar únicamente los métodos especiales que aporten un comportamiento útil a la clase.
- Mantener el significado esperado de cada operación para evitar comportamientos sorprendentes.
- Preferir funciones del lenguaje (len(), print(), operadores...) en lugar de llamar directamente a los métodos especiales.
- Consultar la documentación oficial cuando se implementen métodos menos habituales, ya que algunos tienen requisitos específicos.

## Ejemplo

Se toma el ejemplo de la clase Allen, que es una llave, y se usará un método especial para aplicar la operación suma con una clase tornillo y esta herramienta. Se definen las clases:

::pagebreak
::

```python
class Herramienta:

    tipo = "herramienta"
    
    def __init__(self, size:float) -> None:
        self.size = size

    def ensamblar(self) -> str:
        raise NotImplementedError

class Pieza:
    tipo = "pieza"

    def __init__(self, size:float) -> None:
        self.size = size

    def ensamblar(self) -> str:
        raise NotImplementedError


class Allen(Herramienta):

    def __init__(self, size:float, length:float) -> None:
        super().__init__(size)
        self.length = length

    def ensamblar(self) -> str:
        return "Apretado con llave Allen"

    def __add__(self,pieza:Pieza) -> str:
        return f"{self.ensamblar()} {pieza.ensamblar()}"

class Tornillo(Pieza):

    def __init__(self, size:float, length:float) -> None:
        super().__init__(size)
        self.length = length

    def ensamblar(self) -> str:
        return "Tornillo"

    
    def __add__(self,hta:Herramienta) -> str:
        return f"{self.ensamblar()} {hta.ensamblar()}"
```

Que después se utilizaría de la siguiente forma:

```python
allen_1 = Allen(8.0, 10.0)

tornillo_1 = Tornillo(8.0, 5.0)

print(allen_1 + tornillo_1)

print(tornillo_1 + allen_1)
```

Al evaluar la expresión `allen_1 + tornillo_1`, Python no realiza la suma directamente, sino que invoca automáticamente el método `allen_1.__add__(tornillo_1)`.

En este ejemplo el resultado depende del orden de los operandos, ya que cada clase implementa su propia versión de `__add__()`. Esto no supone un error, pero sí muestra que la sobrecarga de operadores debe utilizarse con criterio para que el comportamiento de los objetos resulte intuitivo.

## Conclusión

Los métodos especiales permiten integrar las clases personalizadas con el propio funcionamiento del lenguaje Python. Gracias a ellos es posible redefinir cómo se representan los objetos, cómo se comparan, cómo responden a operadores, cómo se recorren o cómo interactúan con funciones integradas como `len()` o `str()`.

Aunque son una herramienta muy potente, conviene implementar únicamente aquellos métodos especiales que aporten un comportamiento claro y coherente, evitando redefinir operaciones de forma que resulten confusas para otros desarrolladores.

::pagebreak
::
