# Ejemplo 04: Análisis de sentimiento simple (keyword counting)

## Objetivo: Contar cuántas veces aparecen palabras positivas o negativas en textos.

Diccionario (hardcodeado en reducer):

Positivas: bueno, excelente, feliz, amor
Negativas: malo, triste, odio

El texto de ejemplo está en un archivo llamado _texto.txt_ y fue generado por un LLM
para fines de demostración y pruebas con Hadoop Streaming. 
Contiene 5001 palabras exactas, con las palabras clave distribuidas naturalmente en el discurso.

🔍 Frecuencia de palabras clave:
| Palabra | Frecuencia |  | Porcentaje |
|:--:|:--:|:--:|:--:|
| excelente    |    20 | █████████████████████████ | (20.4%) |
| amor         |    19 | ███████████████████████░░ | (19.4%) |
| bueno        |    17 | █████████████████████░░░░ | (17.3%) |
| malo         |    15 | ██████████████████░░░░░░░ | (15.3%) |
| odio         |    12 | ███████████████░░░░░░░░░░ | (12.2%) |
| feliz        |    10 | ████████████░░░░░░░░░░░░░ | (10.2%) |
| triste       |     5 | ██████░░░░░░░░░░░░░░░░░░░ | (5.1%) |

------------------------------

✅ Total de palabras clave encontradas: 98

📊 Total de palabras en el texto: 2,614


# Mapper (mapper.py)

1. Normaliza a minúsculas: text = line.lower()
    * → "Feliz" y "feliz" se cuentan igual.
2. Extrae solo palabras válidas (sin puntuación, sin números):
    ```python
    words = re.findall(r'\b[a-zñáéíóúü]+\b', text)
    ```
    * \b → límite de palabra (evita que "amoroso" coincida con "amor").
    * [a-zñáéíóúü]+ → solo letras (incluye tildes y ñ).
    * re.findall() → devuelve lista de palabras limpias.
3. Cuenta todas las palabras en la línea con Counter(words).
    * → counts = {'hoy':1, 'me':1, 'siento':1, 'feliz':1, ...}
4. Filtra solo las palabras clave (KEYWORDS) y emite solo si aparecen ≥1 vez

# Reducer (reducer.py)

* Lee todas las líneas emitidas por todos los mappers (ya agrupadas por palabra clave).
* Usa defaultdict(int) para acumular conteos sin comprobar si la clave existe.
* Para cada línea:
    * Separa en palabra y conteo_local.
    * Acumula: total[palabra] += conteo_local.
* Al final, imprime ordenado por frecuencia descendente (de mayor a menor).