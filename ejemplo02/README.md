# Ejemplo 02
## Contar palabras por longitud 

### Objetivo: Contar cuántas palabras de cada longitud existen (ej. 3 letras: 120, 4 letras: 85...).

mapper.py
```python

#!/usr/bin/env python3
import sys

for line in sys.stdin:
    for word in line.strip().split():
        print(f"{len(word)}\t1")
```

✅ reducer.py
python

#!/usr/bin/env python3
import sys

length_counts = {}
for line in sys.stdin:
    length, count = line.strip().split('\t')
    length_counts[length] = length_counts.get(length, 0) + int(count)

for length, count in sorted(length_counts.items()):
    print(f"{length}\t{count}")
Entrada:
"Hola mundo, esto es una prueba"

Salida del mapper (una línea por palabra):

text

4	1
5	1
4	1
2	1
3	1
6	1
Salida del reducer:

text

2	1
3	1
4	2
5	1
6	1
