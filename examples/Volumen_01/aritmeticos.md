# Operadores aritméticos

## Introducción

Los números permiten representar cantidades, pero su utilidad reside en poder realizar operaciones con ellos.

Python incorpora distintos **operadores aritméticos** que permiten efectuar cálculos de forma sencilla, desde sumas y restas hasta divisiones, potencias y otras operaciones matemáticas.

## Uso

Los operadores aritméticos más utilizados son:

::pagebreak
::

| Operador | Operación       |
| `+`      | Suma            |
| `-`      | Resta           |
| `*`      | Multiplicación  |
| `/`      | División        |
| `//`     | División entera |
| `%`      | Resto (módulo)  |
| `**`     | Potencia        |

Las operaciones pueden combinarse para formar expresiones más complejas.

```python
resultado = (8 + 2) * 5
```

Python sigue las reglas habituales de precedencia matemática, aunque el uso de paréntesis mejora la claridad del código.

## Ejemplo

El siguiente programa calcula las horas, los minutos y los segundos a partir del número total de segundos transcurridos.

::pagebreak
::

```python
segundos = 3675

horas = segundos // 3600
segundos_restantes = segundos % 3600

minutos = segundos_restantes // 60
segundos_finales  = segundos_restantes % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_finales )
```

La salida será:

```text
Horas: 1
Minutos: 1
Segundos: 15
```

En este ejemplo, la **división entera** (`//`) permite obtener el número de horas y minutos completos, mientras que el **operador resto o módulo** (`%`) obtiene los segundos que aún quedan por convertir.

## Conclusión

Los operadores aritméticos permiten realizar cálculos utilizando valores numéricos y construir expresiones cada vez más complejas.

En el siguiente capítulo aprenderás los **operadores de comparación**, que permiten comprobar relaciones entre valores y obtener un resultado lógico.

::pagebreak
::