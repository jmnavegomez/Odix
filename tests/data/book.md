| Categoría              | Métodos habituales                                                                   |
| Construcción           | `__new__`, `__init__`, `__del__`                                                     |
| Representación         | `__str__`, `__repr__`, `__format__`, `__bytes__`                                     |
| Comparación            | `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`                           |
| Operadores aritméticos | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__` |
| Operadores lógicos     | `__and__`, `__or__`, `__xor__`, `__invert__`                                         |
| Conversión de tipos    | `__int__`, `__float__`, `__bool__`, `__complex__`, `__index__`                       |
| Colecciones            | `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`               |
| Iteración              | `__iter__`, `__next__`, `__reversed__`                                               |
| Objetos invocables     | `__call__`                                                                           |
| Gestión de atributos   | `__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`                      |
| Gestores de contexto   | `__enter__`, `__exit__`                                                              |
| Copias                 | `__copy__`, `__deepcopy__`                                                           |
| Hash                   | `__hash__`                                                                           |

## Anexo II: Relación entre operaciones de Python y métodos especiales


| Operación en Python   | Método especial invocado             |
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

Comparaciones:

| Operación | Método especial |
| `a == b`  | `a.__eq__(b)`   |
| `a != b`  | `a.__ne__(b)`   |
| `a < b`   | `a.__lt__(b)`   |
| `a <= b`  | `a.__le__(b)`   |
| `a > b`   | `a.__gt__(b)`   |
| `a >= b`  | `a.__ge__(b)`   |

Operadores aritméticos:

| Operación | Método especial     |
| `a + b`   | `a.__add__(b)`      |
| `a - b`   | `a.__sub__(b)`      |
| `a * b`   | `a.__mul__(b)`      |
| `a / b`   | `a.__truediv__(b)`  |
| `a // b`  | `a.__floordiv__(b)` |
| `a % b`   | `a.__mod__(b)`      |
| `a ** b`  | `a.__pow__(b)`      |

Operaciones bit a bit:

| Operación | Método especial   |
| `a & b`   | `a.__and__(b)`    |
| `a \| b`  | `a.__or__(b)`     |
| `a ^ b`   | `a.__xor__(b)`    |
| `~a`      | `a.__invert__()`  |
| `a << b`  | `a.__lshift__(b)` |
| `a >> b`  | `a.__rshift__(b)` |

Gestión de atributos:

| Operación                     | Método especial                  |
| `obj.atributo` (si no existe) | `obj.__getattr__(nombre)`        |
| `obj.atributo`                | `obj.__getattribute__(nombre)`   |
| `obj.atributo = valor`        | `obj.__setattr__(nombre, valor)` |
| `del obj.atributo`            | `obj.__delattr__(nombre)`        |


::pagebreak
::

# Atributos

## Introducción

En programación orientada a objetos (POO) las clases se componen principalmente de atributos y métodos. Los atributos son variables asociadas a una clase o a una instancia que almacenan información sobre su estado o sus características.

Los atributos de instancia suelen inicializarse en el método especial `__init__`, aunque también pueden añadirse posteriormente mediante asignación. `__init__` es el método especial encargado de inicializar una instancia recién creada, mientras que la creación del objeto corresponde a `__new__`.

+ Personalizar la representación textual de un objeto.
+ Comparar objetos entre sí.
+ Sobrecargar operadores como `+`, `-` o `*`.
+ Hacer que un objeto sea iterable.
+ Permitir que pueda utilizarse con `len()`.
+ Convertir un objeto en una función invocable.
+ Gestionar el acceso a atributos.
+ Implementar gestores de contexto (`with`).
