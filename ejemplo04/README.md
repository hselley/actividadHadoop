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
