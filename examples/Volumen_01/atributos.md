# Atributos

## Introducción

En programación orientada a objetos (POO) las clases se componen principalmente de atributos y métodos. Los atributos son variables asociadas a una clase o a una instancia que almacenan información sobre su estado o sus características.

Los atributos de instancia suelen inicializarse en el método especial `__init__`, aunque también pueden añadirse posteriormente mediante asignación. `__init__` es el método especial encargado de inicializar una instancia recién creada, mientras que la creación del objeto corresponde a `__new__`.

Hay dos tipos principales de atributos: atributos de instancia y atributos de clase. Los de instancia son propios de cada objeto y normalmente obtienen su valor durante la instanciación. Por su parte, los atributos de clase son los que comparten todos los objetos y que pertenecen a la clase.

## Uso de los atributos

La definición de los atributos de instancia y de clase se realiza de forma diferente. Para los atributos de instancia se accede al propio objeto, habitualmente mediante `self`, continuado por un punto y el nombre del atributo y asignando un valor. Mientras que para los atributos de clase basta con nombrar el atributo y asignarle un valor.

Una vez que tienen un valor asignado se pueden modificar accediendo a la propiedad y asignando el nuevo valor de la forma: `objeto.atributo = valor_asignado`.

Tanto las clases como las instancias disponen del atributo especial `__dict__`, que almacena sus atributos en forma de diccionario. Python utiliza estos diccionarios durante la búsqueda de atributos.

Python busca primero un atributo en el `__dict__` de la instancia. Si no lo encuentra, continúa la búsqueda en el `__dict__` de la clase y, posteriormente, en las clases padre si existen.

El shadowing consiste en crear un atributo de instancia con el mismo nombre que un atributo de clase. De este modo, al acceder al atributo desde esa instancia, Python utiliza el atributo de instancia y oculta el de clase.

## Ejemplo

El siguiente ejemplo no es parte del código del proyecto. Se ha puesto para entender los conceptos en atributos:

``` python
class Circulo:
    
    pi = 3.141592
    
    def __init__(self, radio: float) -> None:
        self.radio: float = radio
        self.diametro: float = 2*radio

```

En el ejemplo, pi es un atributo de clase y no hace falta asignarle un valor cuando se instancia la clase.

Los atributos de radio y diametro se asignan cuando se instancia un objeto.

``` python
circulo_1 = Circulo(10.0)

print(circulo_1.diametro)

```

En este fragmento el resultado impreso sería `20.0` pues se pide que imprima el valor del atributo diametro de la instancia `circulo_1`.

En caso de seguir con el ejemplo anterior:

``` python
circulo_1.diametro = 15

print(circulo_1.radio)
```

Esto reasigna el atributo diametro con el valor entero `15`. Sin embargo, no modifica el valor de radio, ya que ambos atributos almacenan valores independientes. Si se desea mantener la relación diametro = 2 * radio, debe implementarse explícitamente, por ejemplo mediante una propiedad (`@property`) o actualizando ambos atributos.

Al asignar `circulo_1.pi = 3` no se modifica el atributo de clase, sino que se crea un nuevo atributo de instancia llamado `pi`, que oculta al atributo de clase durante la búsqueda de atributos.


``` python
circulo_1.pi = 3

circulo_2 = Circulo(5.0)

print(circulo_2.pi)
```

En este ejemplo, se imprimiría 3.141592 pues sólo se ha modificado `pi` para el `circulo_1`. Esta situación representa lo que es el shadowing.

## Conclusión

Los atributos de las clases pueden ser de instancia o de clase.

Los atributos de instancia suelen inicializarse mediante el constructor, aunque también pueden crearse posteriormente mediante asignación.

A los de clase se les asigna desde la clase el valor, que puede llamarse desde cualquier objeto de la clase.

Cuando se accede a un atributo desde una instancia, Python busca primero en los atributos propios del objeto y, si no lo encuentra, continúa la búsqueda en la clase. Este mecanismo explica el comportamiento de los atributos de clase y el fenómeno conocido como shadowing.

::pagebreak
::