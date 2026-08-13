# Conjuntos

## Introducción

Las listas y las tuplas permiten almacenar colecciones de elementos manteniendo el orden en el que fueron añadidos. Sin embargo, en algunas situaciones el orden no es importante, mientras que evitar elementos repetidos sí lo es.

Por ejemplo, un programa puede necesitar almacenar los idiomas que habla una persona, las etiquetas de un artículo o los permisos asignados a un usuario. En estos casos, un mismo elemento solo debería aparecer una vez.

Para resolver este problema, Python dispone de los **conjuntos** (`set`), una colección de elementos únicos en la que el orden de los elementos no está garantizado.

## Uso

Los conjuntos se representan mediante llaves (`{}`), separando sus elementos mediante comas.

Un conjunto vacío no se crea con `{}`, ya que esa sintaxis corresponde a un diccionario vacío. Para crear un conjunto vacío se utiliza `set()`.

```python
conjunto = set()

idiomas = {"Español", "Inglés", "Francés"}
```

Si un mismo elemento aparece varias veces, el conjunto solo conservará una copia.

```python
numeros = {1, 2, 2, 3, 3, 3}

print(numeros)
```

La salida será:

```text
{1, 2, 3}
```

Al no mantener un orden definido, los conjuntos no permiten acceder a sus elementos mediante índices.

```python
idiomas = {"Español", "Inglés", "Francés"}

print(idiomas[0])   # Error
```

## Ejemplo

El siguiente programa elimina automáticamente los nombres repetidos de una colección.

```python
participantes = {
    "Ana",
    "Luis",
    "Ana",
    "María",
    "Luis"
}

print(participantes)
```

El conjunto contendrá únicamente los nombres diferentes.

## Conclusión

Los conjuntos permiten almacenar colecciones de elementos sin duplicados. Son especialmente útiles cuando lo importante es saber qué elementos existen, cuando lo importante es la presencia de un elemento y no la posición que ocupa.

En el siguiente capítulo descubrirás los **diccionarios**, una colección que permite asociar cada valor a una clave para acceder a la información de una forma más sencilla.

::pagebreak
::