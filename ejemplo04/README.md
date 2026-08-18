# Ejemplo 04: Análisis de sentimiento simple (keyword counting)

## Objetivo: Contar cuántas veces aparecen palabras positivas o negativas en textos.

Diccionario (hardcodeado en reducer):

Positivas: bueno, excelente, feliz, amor
Negativas: malo, triste, odio

El texto de ejemplo está en un archivo llamado _texto.txt_ y fue generado por un LLM
para fines de demostración y pruebas con Hadoop Streaming. 
Contiene 5001 palabras exactas, con las palabras clave distribuidas naturalmente en el discurso.

📊 Frecuencia aproximada de las palabras clave (para validación):
| Palabra |	Apariciones estimadas |
|:--:|:--:|
| bueno	| 18 |
| excelente	| 21 |
| feliz	| 10 |
| amor	| 20 |
| malo	| 15 |
| triste | 15 |
| odio	| 12 |
| Total	| 111 veces |

