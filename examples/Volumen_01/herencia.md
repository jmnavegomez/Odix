# Herencia

## Introducción

Uno de los conceptos más importantes de la programación orientada a objetos (POO) es la herencia. La herencia es un mecanismo de la programación orientada a objetos que permite que una clase derive de otra, heredando sus atributos y métodos y pudiendo ampliarlos o modificarlos.

La clase padre es la clase inicial que define los atributos y métodos comunes que tienen todas las clases hijas. La clase hija puede reutilizar los atributos y métodos heredados, añadir nuevos y sobrescribir aquellos métodos cuyo comportamiento necesite especializar.

Una clase hija representa un caso más específico de la clase padre. Mantiene todas las características generales de ésta y añade únicamente el comportamiento o los datos que la diferencian.

La función `super()` permite acceder a los métodos de la clase padre desde la clase hija. Se utiliza habitualmente para reutilizar parte de su implementación, por ejemplo llamando al constructor de la clase padre antes de inicializar los nuevos atributos de la clase hija.

Las principales ventajas de la herencia son la reutilización de código, la reducción de duplicidades, la mejora del mantenimiento y la posibilidad de crear especializaciones a partir de una misma clase base.

## Uso de la herencia

La herencia en Python es sencilla y se realiza creando la clase padre y una vez creada, añadiéndola entre paréntesis justo después del nombre de la clase: `class Nombre_hija(Nombre_padre):`.

Toda clase hija también puede utilizarse allí donde se espere un objeto de la clase padre. Con un ejemplo, una llave allen es un tipo de herramienta, un destornillador es otra herramienta. Se le puede decir a una función que la entrada son llaves allen o destornilladores, pero eso obligaría a tener una función por cada una. Si la función requiere de una herramienta, se le puede pasar un objeto tipo herramienta a la función, permitiendo utilizar ambas clases para la función con un único bloque de código.

## Ejemplo

La clase `Herramienta` contendrá el comportamiento común, mientras que `Allen` y `Destornillador` representarán dos especializaciones diferentes.

::pagebreak
::

```python
class Herramienta:

    tipo = "herramienta"
    
    def __init__(self, size:float) -> None:
        self.size = size

    def ensamblar(self) -> None:
        pass
```

Definimos dos clases hijas nuevas de la clase Herramienta: Las clases Allen y Destornillador:

```python
class Allen(Herramienta):

    def __init__(self, size:float, length:float) -> None:
        super().__init__(size)
        self.length = length

    def ensamblar(self) -> None:
        print("Apretar con llave Allen")
```

```python
class Destornillador(Herramienta):

    def __init__(self, size:float, punta:str) -> None:
        super().__init__(size)
        self.punta = punta

    def ensamblar(self):
        print("Apretar con llave Destornillador")
```

Ahora, al iniciar un Destornillador necesitamos:

```python
destornillador_1 = Destornillador(size = 8.0, punta = "Estrella")
```

Gracias a la herencia, tanto la clase `Allen` como `Destornillador` reutilizan el atributo `size` definido en `Herramienta`, añadiendo únicamente los atributos que las diferencian (`length` y `punta`, respectivamente). De este modo se evita duplicar código y se obtiene una estructura más modular y fácil de mantener.

## Conclusión

La herencia permite reutilizar código común entre varias clases relacionadas, facilitando el mantenimiento y permitiendo crear especializaciones de una misma clase base sin duplicar comportamiento.

::pagebreak
::