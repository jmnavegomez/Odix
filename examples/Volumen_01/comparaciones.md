# Operadores de comparación

## Introducción

En muchas ocasiones no basta con almacenar información o realizar cálculos. Un programa también necesita **comparar valores** para saber si una determinada condición se cumple.

Por ejemplo:

+ ¿Es una persona mayor de edad?
+ ¿La contraseña introducida coincide con la esperada?
+ ¿Dos números son iguales?
+ ¿Un producto cuesta más que otro?

Para responder a estas preguntas, Python dispone de los **operadores de comparación**, que comparan dos valores y producen un resultado booleano: `True` o `False`.

## Uso

Los operadores de comparación más utilizados son:

::pagebreak
::

| Operador | Comparación       |
| `==`     | Igual que         |
| `!=`     | Distinto de       |
| `>`      | Mayor que         |
| `<`      | Menor que         |
| `>=`     | Mayor o igual que |
| `<=`     | Menor o igual que |

El resultado de una comparación siempre es un valor booleano.

```python
edad = 20

print(edad >= 18)
```

También es posible almacenar el resultado de una comparación en una variable.

```python
precio = 12.50

es_caro = precio > 10

print(es_caro)
```

Es importante no confundir el operador de asignación (`=`), utilizado para almacenar un valor en una variable, con el operador de comparación (`==`), que comprueba si dos valores son iguales.

```python
edad = 18      # Asigna el valor 18 a la variable
edad == 18     # Comprueba si edad es igual a 18
```

## Ejemplo

El siguiente programa comprueba si un alumno ha aprobado un examen.

```python
nota = 7.5

aprobado = nota >= 5

print(aprobado)
```

También es posible comparar cadenas de texto.

```python
usuario = "Ana"

print(usuario == "Ana")
```

## Conclusión

Los operadores de comparación permiten comprobar la relación entre dos valores y obtener un resultado booleano. Son la base para que un programa pueda tomar decisiones en función de la información que procesa.

En el siguiente capítulo aprenderás los **operadores lógicos**, que permiten combinar varias condiciones para construir expresiones más complejas.

::pagebreak
::
