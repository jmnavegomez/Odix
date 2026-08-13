# Variables

## Introducción

Los programas necesitan **recordar información** mientras se ejecutan. Por ejemplo, el nombre de un usuario, el resultado de un cálculo o el número de intentos realizados durante un juego.

Sin una forma de almacenar esa información, el programa tendría que volver a calcularla o solicitarla cada vez que la necesitara. Esto haría que los programas fueran poco prácticos e incluso imposibles de desarrollar.

Para resolver este problema existen las **variables**. Una variable permite asociar un nombre a un valor para poder utilizarlo más adelante dentro del programa.

## Uso

En Python, una variable se crea mediante una **asignación**. Para ello, se escribe el nombre de la variable, seguido del operador de asignación (`=`) y el valor que se desea almacenar.

```python
edad = 30
```

En una asignación, Python evalúa primero la expresión situada a la derecha del operador `=` y, una vez obtenido el resultado, lo asigna a la variable situada a la izquierda. Al asignar el valor de una variable a otra, la nueva variable pasa a contener el mismo valor.

Por ejemplo:

```python
edad = 30
edad_pepe = edad
```

Hace que la variable edad_pepe sea igual a la variable edad. Mientras que:

```python
edad = 30
edad = edad_pepe # Error: edad_pepe todavía no existe.
```

Daría error porque no se ha definido previamente edad_pepe y al intentar asignarle el valor de edad_pepe a edad falta información.

A partir de ese momento, el nombre `edad` representa el valor almacenado y puede utilizarse en cualquier parte del programa.

El nombre de una variable debe ser descriptivo y representar con claridad la información que contiene. Elegir nombres adecuados facilita la lectura y el mantenimiento del código.

```python
nombre = "Ana"
precio_total = 24.95
numero_intentos = 3
```

Además hay dos formas de asignación: directa e indirecta. La asignación directa es darle un valor concreto a la variable. Además de asignar un valor directamente, una variable también puede obtener su valor a partir de una expresión, del resultado de una función, de la entrada del usuario o del valor de otra variable. A esta forma de obtener el valor la llamaremos asignación indirecta.

```python
precio = 12.5
cantidad = 4

total = precio * cantidad
```

## Ejemplo

El siguiente programa almacena el nombre y la edad de una persona y posteriormente muestra esa información por pantalla.

```python
nombre = "Ana"
edad = 30

print(nombre)
print(edad)
```

Las variables también pueden utilizarse para realizar operaciones.

```python
precio = 12.5
cantidad = 4

total = precio * cantidad

print(total)
```

## Conclusión

Las variables permiten almacenar información para reutilizarla durante la ejecución de un programa. Gracias a ellas, es posible recordar valores, realizar cálculos y construir programas que respondan a diferentes situaciones.

En el siguiente capítulo descubrirás que no toda la información es igual. Python puede almacenar números, textos, valores lógicos y otros muchos tipos de datos, cada uno diseñado para representar una clase diferente de información.

::pagebreak
::