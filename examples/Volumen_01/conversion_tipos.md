# Conversión de tipos

## Introducción

Hasta ahora hemos trabajado con distintos tipos de datos, como números, cadenas de texto, valores booleanos o colecciones. En muchas ocasiones, un programa necesita transformar un valor de un tipo a otro para poder seguir trabajando con él.

Por ejemplo, un número puede convertirse en una cadena de texto para mostrarlo por pantalla, o un texto que contiene un número puede convertirse en un valor numérico para realizar cálculos.

Para realizar estas transformaciones, Python proporciona varias funciones de conversión de tipos.

## Uso

Las conversiones más habituales se realizan mediante las funciones `int()`, `float()`, `str()` y `bool()`.

```python
numero = int("25")
precio = float("19.95")
texto = str(42)
activo = bool(1)
```

Cada una de estas funciones crea un nuevo valor del tipo indicado a partir del valor original.

No todas las conversiones son posibles. Por ejemplo, intentar convertir un texto que no representa un número producirá un error.

```python
numero = int("Hola")    # Error
```

Por este motivo, es importante asegurarse de que el contenido puede convertirse al tipo deseado.

## Ejemplo

El siguiente programa convierte la edad almacenada como una cadena de texto en un número entero para poder realizar una operación.

```python
edad_texto = "30"

edad = int(edad_texto)

print(edad + 5)
```

También es posible convertir un número en una cadena de texto.

```python
temperatura = 21.5

mensaje = "La temperatura es " + str(temperatura) + " grados."

print(mensaje)
```

## Conclusión

La conversión de tipos permite adaptar la información al formato que necesita un programa en cada momento. Gracias a estas funciones es posible transformar números, textos y valores booleanos para realizar cálculos, mostrar información o combinar datos de diferentes tipos.

Con este capítulo concluye el estudio de los fundamentos de Python. A lo largo de este volumen has aprendido cómo almacenar información, representarla mediante distintos tipos de datos, organizarla en colecciones, realizar operaciones y convertirla entre diferentes formatos.

En el siguiente volumen utilizarás todas estas herramientas para construir programas capaces de tomar decisiones, repetir tareas y organizar el código mediante funciones.

::pagebreak
::