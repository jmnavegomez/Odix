# Números

## Introducción

Los números están presentes en la mayoría de los programas. Se utilizan para realizar cálculos, contar elementos, medir tiempos, representar precios o almacenar cualquier otra cantidad numérica.

Python dispone de distintos tipos de datos para representar números. Los más utilizados son los **enteros** (`int`) y los **decimales** (`float`).

Los enteros representan números sin parte decimal.

```python
edad = 30
temperatura = -5
```

Los decimales representan números con parte fraccionaria.

```python
altura = 1.75
precio = 12.95
```

## Uso

Los números permiten realizar operaciones matemáticas de forma sencilla.

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Además de las operaciones básicas, Python incorpora otros operadores muy útiles.

```python
print(10 // 3)   # División entera
print(10 % 3)    # Resto
print(2 ** 3)    # Potencia
```

Las operaciones pueden combinarse para construir expresiones más complejas.

```python
resultado = (5 + 3) * 2
```

Python respeta la precedencia habitual de los operadores matemáticos, aunque el uso de paréntesis mejora la claridad del código y evita errores.

Una característica interesante de Python es que los números enteros no tienen un tamaño máximo fijo. A diferencia de otros lenguajes, donde un entero suele ocupar un número determinado de bits, Python aumenta automáticamente el espacio necesario para almacenar valores cada vez mayores. En la práctica, el único límite es la memoria disponible del sistema.

## Ejemplo

El siguiente ejemplo calcula el importe total de una compra.

```python
precio = 19.95
cantidad = 3

total = precio * cantidad

print(total)
```

También es posible combinar varias operaciones en una misma expresión.

```python
nota1 = 8
nota2 = 7
nota3 = 9

media = (nota1 + nota2 + nota3) / 3

print(media)
```

## Conclusión

Los números permiten representar cantidades y realizar cálculos dentro de un programa. Python distingue principalmente entre números enteros (`int`) y números decimales (`float`), proporcionando operadores que permiten construir desde operaciones sencillas hasta expresiones matemáticas más complejas.

En el siguiente capítulo descubrirás otro tipo de dato fundamental: las cadenas de texto, utilizadas para representar información escrita.

::pagebreak
::