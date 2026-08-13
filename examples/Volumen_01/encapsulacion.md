# Encapsulación

## Introducción

La encapsulación consiste en diseñar una clase de forma que el acceso y la modificación de su estado se realicen a través de una interfaz pública controlada, ocultando por convención los detalles de implementación interna.

En Python, la encapsulación suele implementarse mediante propiedades y otros métodos públicos que controlan el acceso y la modificación del estado interno del objeto, mientras que los atributos internos se consideran detalles de implementación.

## Uso de la encapsulación

Para implementar la encapsulación, Python se apoya principalmente en convenciones de nomenclatura y en propiedades (`property`) que permiten controlar el acceso al estado interno del objeto. En muchos lenguajes de programación, la encapsulación impide acceder directamente a los atributos privados o protegidos, obligando a utilizar métodos públicos, habitualmente denominados ·setters· y ·getters·, para modificar o consultar su valor.

La convención para atributos protegidos es el uso de guión bajo (`_`) y para privados doble guión bajo (`__`) antecediendo el nombre del atributo. Estas convenciones no impiden el poder modificar el valor asignado al atributo pero en Python se sigue la filosofía: ·"We're all consenting adults here"·.

La palabra clave `@property` permite exponer un método como si fuera un atributo. Si además se define un método decorado con `@atributo.setter`, la asignación sobre dicho atributo ejecutará automáticamente ese método. 

La encapsulación ofrece varias ventajas:

- Permite validar los datos antes de modificar el estado interno.
- Reduce el acoplamiento ocultando los detalles de implementación.
- Facilita modificar la implementación interna sin afectar al código que utiliza la clase.

## Ejemplo

Para el ejemplo de encapsulación se empleará un ejemplo con la clase `Circulo`:

::pagebreak
::

```python
class Circulo:

    def __init__(self, radio:float):
        self.__radio:float = radio

    @property
    def radio(self) -> float:
        return self.__radio

    @radio.setter
    def radio(self, nuevo_radio:float) -> None:
        if nuevo_radio > 0.0:
            self.__radio = nuevo_radio

    @property
    def diametro(self) -> float:
        return self.__radio * 2

    
```

En este ejemplo `__radio` es un atributo privado. La propiedad radio permite consultar su valor y el método decorado con `@radio.setter` controla su modificación, validando que el nuevo radio sea mayor que cero.

Para invocar cada uno se puede ejecutar:

```python
circulo_1 = Circulo(5.0)

print(circulo_1.radio)

circulo_1.radio = 4.0

print(circulo_1.diametro)
```

En el primer print se consulta la propiedad lo que lleva a obtener el valor del radio (`5.0` en este punto). En el segundo print se obtiene el valor del diámetro que es calculado en base al radio. Sin embargo, este diámetro ya no es el doble de `5.0`, sino que es `8.0` ya que se invocó el setter justo antes del print para modificar el radio a `4.0`.

## Conclusión

La encapsulación en Python es más un convenio que una característica intrínseca del lenguaje. No existe la ocultación de atributos como tal pero se pueden usar convenciones para poder usar propiedades y métodos ·setter· como en otros lenguajes de programación.

Esto permite validar, transformar o calcular valores antes de modificar el estado interno del objeto, además de mantener una interfaz pública estable aunque cambie la implementación interna de la clase.

::pagebreak
::