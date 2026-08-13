# Tipos de datos

## Introducción

No toda la información que utiliza un programa es igual. Un número, un texto o una lista de elementos representan conceptos diferentes y permiten realizar operaciones distintas.

Por ejemplo, dos números pueden sumarse, mientras que un texto puede concatenarse con otro. Del mismo modo, una lista puede contener varios elementos, mientras que un número representa un único valor.

Para distinguir cada clase de información, Python utiliza los **tipos de datos**. Cada valor pertenece a un tipo determinado, que define cómo se almacena y qué operaciones pueden realizarse sobre él.

## Uso

En Python, normalmente no es necesario indicar el tipo de una variable. Python determina automáticamente el tipo a partir del valor asignado.

```python
nombre = "Ana"
edad = 30
altura = 1.68
estudiante = True
```

En este ejemplo, Python reconoce que `30` es un número entero, `"Ana"` es un texto y `True` representa un valor lógico.

Aunque todas las variables se crean mediante una asignación, el tipo del valor almacenado es diferente en cada una de ellas.

A lo largo de este libro estudiarás los tipos de datos más utilizados y aprenderás cuándo conviene emplear cada uno de ellos.

## Ejemplo

El siguiente programa utiliza varios tipos de datos diferentes.

```python
nombre = "Ana"
edad = 30
altura = 1.68
estudiante = True

print(nombre)
print(edad)
print(altura)
print(estudiante)
```

Aunque todas las variables se crean de la misma forma, cada una almacena un tipo de información diferente.

## Conclusión

Los tipos de datos permiten representar correctamente la información que utiliza un programa. Cada tipo está diseñado para almacenar una clase concreta de valores y permite realizar un conjunto de operaciones adaptadas a ellos.

En los próximos capítulos estudiarás los principales tipos de datos de Python y aprenderás a utilizarlos en situaciones reales.

::pagebreak
::