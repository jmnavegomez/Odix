# Tuplas

## Introducción

Las listas permiten almacenar varios valores relacionados y modificar su contenido cuando es necesario. Sin embargo, hay situaciones en las que los datos no deben cambiar una vez creados.

Por ejemplo, las coordenadas de un punto, los meses del año o los días de la semana son datos que permanecen constantes durante la ejecución de un programa.

Para representar este tipo de información, Python dispone de las **tuplas** (`tuple`), una colección ordenada cuyos elementos no pueden modificarse una vez creada.

## Uso

Las tuplas se representan mediante paréntesis (`()`), separando sus elementos mediante comas.

```python
coordenadas = (10, 20)
```

Al igual que las listas, pueden contener valores del mismo tipo o de tipos diferentes.

```python
persona = ("Ana", 30, True)
```

Los elementos de una tupla también se acceden mediante índices, comenzando por `0`.

```python
dias = ("Lunes", "Martes", "Miércoles")

print(dias[0])
print(dias[1])
print(dias[2])
```

Sin embargo, una vez creada la tupla, sus elementos no pueden modificarse.

```python
dias = ("Lunes", "Martes", "Miércoles")

dias[0] = "Domingo"   # Error
```

## Ejemplo

El siguiente programa almacena las coordenadas de un punto utilizando una tupla.

```python
punto = (12, 8)

print(punto[0])
print(punto[1])
```

Las tuplas son especialmente útiles cuando un conjunto de datos representa una única entidad y no debe modificarse durante la ejecución del programa.

## Conclusión

Las tuplas permiten agrupar varios valores relacionados de forma ordenada, igual que las listas. Su principal diferencia es que su contenido no puede modificarse una vez creado, lo que ayuda a proteger datos que deben permanecer constantes.

Elegir entre una lista y una tupla depende de si los datos deben cambiar durante la ejecución del programa.

En el siguiente capítulo conocerás los **conjuntos**, una colección diseñada para almacenar elementos sin repetirlos.

::pagebreak
::