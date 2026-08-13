# Listas

## Introducción

Hasta ahora hemos trabajado con variables capaces de almacenar un único valor. Sin embargo, en muchas ocasiones es necesario trabajar con varios valores relacionados.

Por ejemplo, un programa puede necesitar almacenar las notas de un alumno, los nombres de los participantes de un curso o los productos de un carrito de compra.

Crear una variable para cada dato sería poco práctico. Para resolver este problema, Python dispone de las **listas** (`list`), un tipo de dato que permite almacenar varios valores en una única variable.

Las listas mantienen el orden de los elementos, pueden contener valores del mismo tipo o de tipos diferentes y, además, son modificables.

## Uso

Las listas se representan mediante corchetes (`[]`), separando cada elemento mediante comas.

```python
numeros = [3, 7, 12, 25]
```

También pueden almacenar cadenas de texto.

```python
nombres = ["Ana", "Luis", "Marta"]
```

Incluso es posible combinar distintos tipos de datos en una misma lista.

```python
datos = ["Ana", 30, True]
```

Cada elemento ocupa una posición dentro de la lista, denominada **índice**. En Python, los índices comienzan en `0`.

```python
colores = ["rojo", "verde", "azul"]

print(colores[0])
print(colores[1])
print(colores[2])
```

El número de elementos de una lista puede variar durante la ejecución del programa.

## Ejemplo

El siguiente programa almacena las temperaturas registradas durante una semana y muestra la primera y la última.

```python
temperaturas = [18.5, 20.1, 19.8, 21.3, 22.0, 20.7, 19.4]

print(temperaturas[0])
print(temperaturas[6])
```

Las listas también permiten modificar un elemento indicando su índice.

```python
temperaturas = [18.5, 20.1, 19.8]

temperaturas[1] = 21.0

print(temperaturas)
```

## Conclusión

Las listas permiten agrupar varios valores relacionados en una única variable, manteniendo el orden en el que fueron almacenados. Gracias a ellas, es posible trabajar de forma cómoda con colecciones de datos.

En el siguiente capítulo descubrirás las **tuplas**, una estructura muy similar a las listas, pero diseñada para almacenar datos que no deben modificarse.

::pagebreak
::
