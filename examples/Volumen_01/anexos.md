## Anexo A. Tipos de datos de Python

| **Tipo de dato**  | **Clase**   |
| Número entero | `int`   |
| Decimal       | `float` |
| Cadena        | `str`   |
| Booleano      | `bool`  |
| Lista         | `list`  |
| Tupla         | `tuple` |
| Conjunto      | `set`   |
| Diccionario   | `dict`  |

::pagebreak
::

## Anexo B. Métodos más utilizados

### Listas

| **Método**      | **Descripción**                          |
| `append()`  | Añade un elemento al final.          |
| `insert()`  | Inserta un elemento en una posición. |
| `remove()`  | Elimina un elemento.                 |
| `pop()`     | Elimina y devuelve un elemento.      |
| `sort()`    | Ordena la lista.                     |
| `reverse()` | Invierte el orden.                   |
| `clear()`   | Vacía la lista.                      |
| `index()`   | Devuelve el índice en el que se encuentra el elemento |

### Cadenas

| **Método**      | **Descripción**             |
| `lower()`   | Convierte a minúsculas. |
| `upper()`   | Convierte a mayúsculas. |
| `strip()`   | Elimina espacios.       |
| `replace()` | Sustituye texto.        |
| `split()`   | Divide una cadena.      |
| `join()`    | Une los elementos de una colección.|
| `startswith()`| Comprueba si la cadena comienza por un texto.|
| `endswith()`|  Comprueba si la cadena termina en un texto.|

### Diccionarios

| **Método**     | **Descripción**                       |
| `keys()`   | Devuelve las claves.              |
| `values()` | Devuelve los valores.             |
| `items()`  | Devuelve pares clave-valor.       |
| `get()`    | Obtiene un valor de forma segura. |
| `update()` | Actualiza el diccionario.         |
| `pop()`    | Elimina una clave.                |
| `popitem()`| Elimina y devuelve el último par clave-valor.|

### Conjuntos

| **Método**           | **Descripción**          |
| `add()`          | Añade un elemento.   |
| `remove()`       | Elimina un elemento. |
| `union()`        | Unión de conjuntos.  |
| `intersection()` | Intersección.        |
| `difference()`   | Devuelve la diferencia de los elementos.|

## Anexo C. Operadores

| **Tipo**        | **Operadores**        |
| Aritméticos | `+ - * / // % **` |
| Comparación | `== != > < >= <=` |
| Lógicos     | `and or not`      |

::pagebreak
::

## Anexo D. Conversión de tipos

| **Función**   | **Convierte a**  |
| `int()`   | Entero       |
| `float()` | Decimal      |
| `str()`   | Cadena       |
| `bool()`  | Booleano     |
| `list()`  | Lista        |
| `tuple()` | Tupla        |
| `set()`   | Conjunto     |
| `dict()`  | Diccionario* |
*No todas las conversiones son posibles. La conversión solo puede realizarse cuando el valor original puede representarse mediante el nuevo tipo de dato.

::pagebreak
::

## Anexo E. Precedencia de operadores

Cuando una expresión contiene varios operadores, Python los evalúa siguiendo el siguiente orden de prioridad.

|**Precedencia**|**Operador**|
|1|`()`|
|2|`**`|
|3|`* / // %`|
|4|`+ -`|
|5|`< > ==`|
|6|`not`|
|7|`and`|
|8|`or`|

::pagebreak
::

## Anexo F. Funciones integradas utilizadas en este volumen

| **Función**   | **Descripción**                       |
| `print()` | Muestra información por pantalla. |
| `type()`  | Devuelve el tipo de un valor.     |
| `len()`   | Devuelve el número de elementos.  |
| `int()`   | Convierte a entero.               |
| `float()` | Convierte a decimal.              |
| `str()`   | Convierte a cadena.               |
| `bool()`  | Convierte a booleano.             |

::pagebreak
::

## Anexo G: Relación entre operaciones de Python y métodos especiales

| **Operación en Python**   | **Método especial invocado**             |
| `str(obj)`            | `obj.__str__()`                      |
| `repr(obj)`           | `obj.__repr__()`                     |
| `format(obj)`         | `obj.__format__()`                   |
| `bytes(obj)`          | `obj.__bytes__()`                    |
| `len(obj)`            | `obj.__len__()`                      |
| `bool(obj)`           | `obj.__bool__()`                     |
| `int(obj)`            | `obj.__int__()`                      |
| `float(obj)`          | `obj.__float__()`                    |
| `complex(obj)`        | `obj.__complex__()`                  |
| `hash(obj)`           | `obj.__hash__()`                     |
| `iter(obj)`           | `obj.__iter__()`                     |
| `next(iterador)`      | `iterador.__next__()`                |
| `reversed(obj)`       | `obj.__reversed__()`                 |
| `obj[indice]`         | `obj.__getitem__(indice)`            |
| `obj[indice] = valor` | `obj.__setitem__(indice, valor)`     |
| `del obj[indice]`     | `obj.__delitem__(indice)`            |
| `valor in obj`        | `obj.__contains__(valor)`            |
| `obj()`               | `obj.__call__()`                     |
| `with obj:`           | `obj.__enter__()` y `obj.__exit__()` |

::pagebreak
::

## Anexo H: Comparaciones:

| **Operación** | **Método especial** |
| `a == b`  | `a.__eq__(b)`   |
| `a != b`  | `a.__ne__(b)`   |
| `a < b`   | `a.__lt__(b)`   |
| `a <= b`  | `a.__le__(b)`   |
| `a > b`   | `a.__gt__(b)`   |
| `a >= b`  | `a.__ge__(b)`   |
## Anexo I: Operadores aritméticos:

| **Operación** | **Método especial**     |
| `a + b`   | `a.__add__(b)`      |
| `a - b`   | `a.__sub__(b)`      |
| `a * b`   | `a.__mul__(b)`      |
| `a / b`   | `a.__truediv__(b)`  |
| `a // b`  | `a.__floordiv__(b)` |
| `a % b`   | `a.__mod__(b)`      |
| `a ** b`  | `a.__pow__(b)`      |

::pagebreak
::

## Anexo J: Operaciones bit a bit:

| **Operación** | **Método especial**   |
| `a & b`   | `a.__and__(b)`    |
| `a \| b`  | `a.__or__(b)`     |
| `a ^ b`   | `a.__xor__(b)`    |
| `~a`      | `a.__invert__()`  |
| `a << b`  | `a.__lshift__(b)` |
| `a >> b`  | `a.__rshift__(b)` |

## Anexo K: Gestión de atributos:

| **Operación**                    | **Método especial**                 |
| `obj.atributo` (si no existe) | `obj.__getattr__(nombre)`        |
| `obj.atributo`                | `obj.__getattribute__(nombre)`   |
| `obj.atributo = valor`        | `obj.__setattr__(nombre, valor)` |
| `del obj.atributo`            | `obj.__delattr__(nombre)`        |
