# Polimorfismo

## Introducción

En programación orientada a objetos (POO) se define polimorfismo como la capacidad de utilizar una misma interfaz para trabajar con objetos de diferentes tipos, es decir, una misma función puede trabajar con objetos de diferentes clases utilizando la misma interfaz, sin necesidad de conocer el tipo concreto del objeto.

En Python el polimorfismo puede conseguirse principalmente de dos formas: mediante herencia o mediante Duck Typing. El polimorfismo mediante herencia emplea la sobreescritura de un método de la clase padre en las clases hijas, haciendo que todos los objetos de ese tipo puedan ser empleados en la misma función. El polimorfismo sin herencia se basa en el **Duck Typing**: "Si camina como un pato y hace cuac como un pato, entonces lo tratamos como un pato.". En este caso no es necesario que exista una relación de herencia entre las clases. Basta con que el objeto implemente el método esperado para que pueda utilizarse.

El polimorfismo permite evitar duplicidades de código y simplificar el uso de los objetos, ya que una misma función puede invocar un método del objeto sin necesidad de conocer la clase a la que pertenece. 

## Uso del polimorfismo

Para emplear el polimorfismo se puede hacer uso de la herencia o no. Para llevar a cabo un polimorfismo mediante herencia, la clase padre tendrá que definir uno o varios métodos que en las clases hijas, especializaciones de la clase padre, sobreescribirán pero manteniendo el mismo nombre del método.

Cuando se quiere realizar polimorfismo sin herencia, basta con incluir el método con las mismas propiedades dentro de una clase ya que después la función no diferencia que un objeto sea de una clase o no, simplemente intenta acceder al método solicitado. Si el objeto lo implementa, la llamada se realiza correctamente; en caso contrario se producirá una excepción (`AttributeError`).

Por lo tanto, para implementar el polimorfismo en Python, es suficiente con el uso de métodos con el mismo nombre y argumentos dentro de distintas clases que luego, al instanciarlas en objetos, podrán ser utilizadas por las funciones independientemente de si son de la misma clase o clase padre que tengan.

## Ejemplo

Para este ejemplo que se presentó en los métodos de la clase, la clase `Herramienta` contendrá el comportamiento común, mientras que `Allen` y `Destornillador` representarán dos especializaciones diferentes.

::pagebreak
::

```python
class Herramienta:

    tipo = "herramienta"
    
    def __init__(self, size:float) -> None:
        self.size = size

    def ensamblar(self) -> None:
        raise NotImplementedError
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

Como se puede ver, `Allen` y `Destornillador` sobrescriben el método ensamblar heredado de `Herramienta`. Si definimos una función ensamble, podemos usar las herramientas llamando al método ensamblar:

```python
def ensamble(tool:Herramienta) -> None:
    tool.ensamblar()
```

Según la herramienta que se ponga usará el método de esa herramienta. Python no necesita comprobar si el objeto es una instancia de `Allen` o `Destornillador`; simplemente intenta acceder al método `ensamblar()`.

Aunque el parámetro se haya anotado como `Herramienta`, esta anotación no impide pasar objetos de otras clases. Los ·type hints· sirven como ayuda para el programador y para las herramientas de análisis estático, pero no modifican el comportamiento del programa en tiempo de ejecución.

Un ejemplo de Duck Typing sería el siguiente:
```python

class Robot:

    def ensamblar(self):
        print("Ensamblando automáticamente")

robot = Robot()

ensamble(robot)
```

Aunque Robot no hereda de `Herramienta`, la función sigue funcionando porque el objeto implementa el método `ensamblar()`.

## Conclusión

El polimorfismo permite emplear objetos de distintas clases en la misma función siempre que implementen la interfaz esperada (normalmente uno o varios métodos con el mismo nombre y comportamiento compatible). Esto evita tener que hacer casos concretos para cada clase que se le pasa al método.

Es un concepto de POO muy empleado que en Python se puede hacer con herencia o sin herencia.

El polimorfismo es uno de los pilares de la programación orientada a objetos, ya que permite escribir funciones más genéricas, reutilizables y fáciles de mantener.

::pagebreak
::