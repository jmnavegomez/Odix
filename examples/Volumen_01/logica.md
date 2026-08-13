# Operadores lógicos

## Introducción

En ocasiones, una única comparación no es suficiente para tomar una decisión. Un programa puede necesitar comprobar que se cumplen varias condiciones al mismo tiempo o que basta con que se cumpla una de ellas.

Por ejemplo:

* ¿Es mayor de edad **y** tiene entrada?
* ¿Es administrador **o** moderador?
* ¿El usuario **no** ha iniciado sesión?

Para resolver estas situaciones, Python dispone de los **operadores lógicos**, que permiten combinar o modificar valores booleanos.

## Uso

Los operadores lógicos más utilizados son:

::pagebreak
::

| **Operador** | **Significado**                                         |
| `and`    | Todas las condiciones deben ser verdaderas.         |
| `or`     | Basta con una de las condiciones verdadera.         |
| `not`    | Invierte el valor lógico de una condición.          |

Los operadores lógicos trabajan con valores booleanos (`True` y `False`) y producen también un resultado booleano.

```python
es_adulto = True
tiene_entrada = False

print(es_adulto and tiene_entrada)
print(es_adulto or tiene_entrada)
print(not tiene_entrada)
```

## Ejemplo

El siguiente programa comprueba distintas condiciones para permitir el acceso a un evento.

```python
edad = 20
tiene_entrada = True
esta_en_lista = False

puede_entrar = edad >= 18 and tiene_entrada

print(puede_entrar)

acceso_especial = tiene_entrada or esta_en_lista

print(acceso_especial)

print(not esta_en_lista)
```

En este ejemplo:

+ `and` exige que ambas condiciones sean verdaderas.
+ `or` devuelve `True` si al menos una condición es verdadera.
+ `not` invierte el valor lógico de una condición.

## Conclusión

Los operadores lógicos permiten combinar o modificar condiciones para construir expresiones más complejas. Gracias a ellos, un programa puede comprobar simultáneamente varios requisitos o invertir el resultado de una condición.

En el siguiente capítulo descubrirás cómo convertir valores entre los distintos tipos de datos de Python, una herramienta fundamental para trabajar con información de diferente naturaleza.

::pagebreak
::