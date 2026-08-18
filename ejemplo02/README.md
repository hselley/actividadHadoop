# Ejemplo 02
## Contar palabras por longitud 

### Objetivo: Contar cuántas palabras de cada longitud existen (ej. 3 letras: 120, 4 letras: 85...).

`mapper.py`
```python

#!/usr/bin/env python3
import sys

for line in sys.stdin:
    for word in line.strip().split():
        print(f"{len(word)}\t1")
```

`reducer.py`
```python

#!/usr/bin/env python3
import sys

length_counts = {}
for line in sys.stdin:
    length, count = line.strip().split('\t')
    length_counts[length] = length_counts.get(length, 0) + int(count)

for length, count in sorted(length_counts.items()):
    print(f"{length}\t{count}")
```

Entrada:

`"Hola mundo, esto es una prueba"`

## Salida del mapper (una línea por palabra):

| Palabra | Frecuencia |
|:-------:|:-------:|
| 4     | 1     |
| 5     | 1     |
| 4     | 1     |
| 2     | 1     |
| 3     | 1     |
| 6     | 1     |


### Salida del reducer:
| Palabra | Frecuencia |
|:-------:|:-------:|
| 2     | 1     |
| 3     | 1     |
| 4     | 2     |
| 5     | 1     |
| 6     | 1     |


# Mapper (mapper.py)

✅ ¿Qué hace?
* Lee líneas del stdin (Hadoop le envía fragmentos del archivo de entrada).
* Por cada línea:
    * line.strip() → elimina espacios/tabs al inicio y final.
    * .split() → divide la línea en palabras (por espacios, tabs, etc.).
* Para cada palabra, calcula su longitud (len(word)) y emite un par:

Ejemplo:

Si la palabra es "Hadoop" (6 letras), imprime:

`6\t1`


## Detalles técnicos clave:
| Aspecto                |Explicación                                                                                                                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Formato de salida**  | `clave\tvalor` → aquí la clave es la **longitud** (un entero como string), y el valor es `1`. Esto es vital: Hadoop Streaming espera que el mapper emita pares `<clave, valor>` separados por tabulador (`\t`). |
| **¿Por qué `\t`?**     | Porque Hadoop usa el **tabulador como delimitador por defecto** entre clave y valor durante la fase de *shuffle & sort*.                                                                                   |
| **¿Por qué `1`?**      | Porque cada palabra "vota" por su longitud: **1 voto por palabra**. Luego, el reducer suma todos los votos por cada longitud (agregación).                                                              |
| **Entrada de stdin**   | Hadoop redirige el contenido del input (ej. archivos en HDFS) al `stdin` del mapper. No necesitas abrir archivos manualmente — el framework se encarga de la entrada.                               |

# Reducer (reducer.py)

### ¿Qué hace?
* Lee todas las líneas que Hadoop le envía desde el mapper (después del shuffle & sort).
* Para cada línea:
    * line.strip().split('\t') → separa en longitud y voto.
    * Suma los votos: length_counts[longitud] += voto.
* Al final, imprime longitud → conteo total, ordenado por longitud (ascendente).