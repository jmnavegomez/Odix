# Cadenas de texto

## Introducción

Los programas no solo trabajan con números. También necesitan representar información escrita, como nombres, direcciones, mensajes, contraseñas o el contenido de un archivo.

Para almacenar este tipo de información, Python utiliza las **cadenas de texto** (`str`). Una cadena es una secuencia de caracteres que puede contener letras, números, símbolos o espacios.

Las cadenas se delimitan mediante comillas simples (`'`) o dobles (`"`), siendo ambas equivalentes en Python.

```python
nombre = "Ana"
mensaje = '¡Hola, mundo!'
```

## Uso

Las cadenas pueden almacenarse en variables y utilizarse como cualquier otro tipo de dato.

```python
ciudad = "Madrid"
```

También es posible combinar varias cadenas mediante el operador de concatenación (`+`).

```python
nombre = "Ana"
apellido = "García"

nombre_completo = nombre + " " + apellido
```

El operador de multiplicación (`*`) permite repetir una cadena un número determinado de veces.

```python
separador = "-" * 20
```

Python distingue entre mayúsculas y minúsculas, por lo que dos cadenas que solo se diferencian en el uso de estas letras se consideran distintas.

```python
usuario = "ana"
administrador = "Ana"
```

## Ejemplo

El siguiente programa crea un mensaje de bienvenida utilizando varias cadenas de texto.

```python
nombre = "Ana"

mensaje = "Bienvenida, " + nombre + "."

print(mensaje)
```

También es posible repetir una cadena para generar un separador.

```python
print("=" * 30)
print("Fin del programa")
print("=" * 30)
```

## Conclusión

Las cadenas de texto permiten representar información escrita dentro de un programa. Gracias a ellas es posible almacenar, mostrar y combinar texto de forma sencilla.

En el siguiente capítulo conocerás los **valores lógicos** (`bool`), un tipo de dato utilizado para representar situaciones que solo pueden tener dos posibles estados: verdadero o falso.

::pagebreak
::