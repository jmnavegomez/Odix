# Métodos

## Introducción

Los métodos son funciones definidas dentro de una clase que describen el comportamiento de sus objetos o de la propia clase. Los métodos de instancia se invocan normalmente desde un objeto previamente instanciado.

La diferencia clave entre funciones y métodos es que los métodos reciben automáticamente una referencia a la instancia (`self`) o a la clase (`cls`), lo que les permite acceder a sus atributos si lo necesitan.

El parámetro `self` representa la instancia sobre la que se está ejecutando el método. Gracias a él es posible acceder a los atributos y métodos del propio objeto.

Hay tres tipos de métodos: de instancia, de clase y estáticos. Los métodos de instancia acceden a los atributos y métodos de la instancia mediante `self`. Por su parte los métodos de clase llaman a los atributos de clase mediante el parámetro `cls`. Finalmente, los métodos estáticos no emplean atributos de la clase, simplemente implementan una operación que utiliza únicamente los parámetros recibidos. En este último caso el método suele estar relacionado con la clase.

Estos métodos no poseen modificadores de acceso `public`, `private` o `protected`. En su lugar utiliza convenciones. Para los métodos públicos se escribe directamente el nombre del método. Los protegidos se representan con `_` pero no afecta a la visibilidad, sólo al nombre y es una convención que se ha quedado para indicar que es protegido. Los métodos privados usan el doble guion bajo (`__`). Python modifica internamente su nombre (name mangling), lo que evita colisiones con métodos de clases base durante la herencia y dificulta su acceso accidental.

## Uso de los métodos

Para invocar un método se escribe: `nombre_objeto.metodo(argumentos)`. Los métodos pueden modificar el estado del objeto asignando nuevos valores a sus atributos de instancia. También pueden modificar atributos de clase cuando sea necesario.

Son importantes las buenas prácticas a la hora de programar los métodos:

- Utilizar nombres que describan acciones (`guardar()`, `calcular()`, `abrir()`).
- Cada método debería tener una única responsabilidad.
- Evitar métodos excesivamente largos.
- Los métodos públicos forman parte de la interfaz de la clase y deberían mantenerse estables.
- Reservar los métodos con `_` para detalles internos de implementación.
- Utilizar `@staticmethod` únicamente cuando la función no necesite acceder ni a la instancia ni a la clase.
- Utilizar `@classmethod` cuando la operación afecte a la clase o actúe como constructor alternativo.

## Ejemplo

Para los ejemplos, se va a usar el ejemplo empleado en el apartado de atributos pero añadiendo un método área:

::pagebreak
::

``` python
class Circulo:
    
    pi = 3.141592
    
    def __init__(self, radio: float) -> None:
        self.radio: float = radio
        self.diametro: float = 2*radio

    def area(self):
        return self.pi * (self.radio**2)

    @classmethod
    def obtener_pi(cls):
        return cls.pi

    @staticmethod
    def suma_areas(area1: float, area2: float) -> float:
        return area1 + area2
```

Como se puede ver en el ejemplo, area depende del atributo de clase pi y del atributo de instancia radio. El método de clase devuelve pi, que es un atributo de clase. Por último, la clase estática suma_areas devuelve la suma de dos áreas que no se encuentran en ninguno de los atributos de la clase.


## Conclusión

Los métodos son funciones propias de las clases que pueden usar los atributos para hacer modificaciones internas u obtener una respuesta en base a los atributos.

Pueden ser de instancia, de clase y estáticos y siguen una convención concreta para métodos públicos, privados y protegidos. En Python no existe un mecanismo estricto de control de acceso como en otros lenguajes. La visibilidad de los métodos se basa principalmente en convenciones de nomenclatura.

Es recomendable seguir buenas prácticas para evitar confusiones y duplicidades.

::pagebreak
::
