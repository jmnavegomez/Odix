# Diccionarios

## Introducción

Hasta ahora hemos trabajado con colecciones cuyos elementos se identifican por su posición o simplemente por su pertenencia al conjunto. Sin embargo, en muchas ocasiones resulta más útil asociar cada dato a un nombre que describa su significado.

Por ejemplo, al representar una persona es más natural hablar de su nombre, edad o ciudad que del primer, segundo o tercer elemento de una colección.

Para resolver este problema, Python dispone de los **diccionarios** (`dict`), una colección que almacena pares **clave-valor** (·key-value pairs·), permitiendo acceder a cada dato mediante una clave en lugar de un índice.

## Uso

Los diccionarios se representan mediante llaves (`{}`). Cada par clave-valor está formado por una clave y un valor, separados por dos puntos (`:`).

```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}
```

Para acceder a un valor se utiliza su clave.

```python
print(persona["nombre"])
print(persona["edad"])
```

También es posible modificar el valor asociado a una clave existente.

```python
persona["edad"] = 31
```

O añadir un nuevo par clave-valor.

```python
persona["profesion"] = "Ingeniera"
```

Las claves de un diccionario deben ser únicas. Si una misma clave aparece varias veces, solo se conservará la última asignación.

Además de acceder a un valor mediante su clave, también es posible trabajar con el conjunto de claves o con el conjunto de valores de un diccionario. Más adelante aprenderás a obtener las claves mediante `keys()` y los valores mediante `values()`.

## Ejemplo

El siguiente programa almacena información sobre un libro y muestra algunos de sus datos.

```python
libro = {
    "titulo": "Python básico",
    "autor": "Ana García",
    "paginas": 250
}

print(libro["titulo"])
print(libro["paginas"])
```

Modificar un valor resulta tan sencillo como realizar una nueva asignación sobre su clave.

```python
libro["paginas"] = 275

print(libro)
```

## Conclusión

Los diccionarios permiten organizar la información mediante pares clave-valor, facilitando el acceso a cada dato por su nombre en lugar de por su posición. Son especialmente útiles para representar entidades con diferentes características o atributos.

Con este capítulo concluye el estudio de los principales tipos de datos de Python. En los siguientes capítulos aprenderás a utilizarlos para realizar operaciones, tomar decisiones, repetir tareas y organizar mejor tus programas.

::pagebreak
::