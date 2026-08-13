# Booleanos

## Introducción

En muchas situaciones, un programa necesita responder a preguntas cuya respuesta solo puede tener dos posibilidades: **sí** o **no**.

Por ejemplo:

+ ¿El usuario ha iniciado sesión?
+ ¿La contraseña es correcta?
+ ¿El pedido ha sido enviado?
+ ¿El número es mayor que cero?

Para representar este tipo de información, Python utiliza el tipo de dato **booleano** (`bool`), cuyos únicos valores posibles son `True` (verdadero) y `False` (falso).

## Uso

Los valores booleanos pueden asignarse a una variable como cualquier otro tipo de dato.

```python
es_mayor_de_edad = True
sesion_iniciada = False
```

También pueden obtenerse como resultado de una comparación.

```python
edad = 20

es_adulto = edad >= 18
```

En este ejemplo, la comparación produce el valor `True`, que queda almacenado en la variable `es_adulto`.

Los valores booleanos suelen utilizarse para controlar el comportamiento de un programa, permitiendo tomar decisiones o repetir acciones, como veremos en capítulos posteriores.

## Ejemplo

El siguiente programa comprueba si una persona es mayor de edad.

```python
edad = 20

es_adulto = edad >= 18

print(es_adulto)
```

También es posible asignar directamente un valor booleano.

```python
modo_oscuro = True

print(modo_oscuro)
```

## Conclusión

Los booleanos permiten representar información que solo puede adoptar dos estados: verdadero o falso. Son fundamentales para expresar condiciones y controlar el comportamiento de un programa.

En el siguiente capítulo descubrirás las **listas**, un tipo de dato que permite almacenar varios valores en una única variable.

::pagebreak
::
