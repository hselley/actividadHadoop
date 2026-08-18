# Ejemplo 03

## Objetivo: Dado un CSV de ventas (categoría, precio), calcular el promedio de precio por categoría.

Ej. entrada:

ropa,50

alimentos,10

ropa,70

alimentos,20


# Mapper (mapper.py)

* Lee cada línea del archivo (una línea = un registro: categoría,precio).
* Separa en dos partes con .split(',').
* Valida que haya exactamente 2 campos (len(parts) == 2).
* Intenta convertir el segundo campo a float.
* Si éxito: emite 3 campos separados por tabulador:
* Si fallo (ej. "ropa,abc"): salta la línea (continue).

# Reducer (reducer.py)

* Lee todas las líneas que Hadoop le envía (ya agrupadas por categoría).
* Para cada línea:
    * Separa en 3 partes: categoría, precio, 1.
    * Acumula:
    total[cat] += precio → suma de todos los precios de esa categoría.
    * count[cat] += 1 → número de registros de esa categoría.
* Al final, calcula:
promedio = total[cat] / count[cat]
* Imprime cada categoría con su promedio, ordenada alfabéticamente.