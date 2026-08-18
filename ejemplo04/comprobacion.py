#!/usr/bin/env python3
"""
Calcula la frecuencia de palabras clave en un texto.
Uso:
    python word_frequency.py texto.txt
    cat texto.txt | python word_frequency.py
"""

import sys
import re
from collections import Counter

# Lista de palabras clave (solo base, sin mayúsculas)
KEYWORDS = ['bueno', 'excelente', 'feliz', 'amor', 'malo', 'triste', 'odio']

def count_keyword_frequencies(text):
    """
    Cuenta frecuencias de KEYWORDS en el texto.
    - Ignora mayúsculas/minúsculas
    - Coincidencia con palabras completas (no subcadenas)
    - Ignora puntuación adyacente (ej. 'amor.' → 'amor')
    """
    # Convertir texto a minúsculas para búsquedas case-insensitive
    text_lower = text.lower()
    
    # Extraer solo palabras alfanuméricas (separadas por límites de palabra)
    # \b asegura coincidencia con palabra completa (ej. 'amor' no coincide en 'amoroso')
    words = re.findall(r'\b[a-zñáéíóúü]+(?:_[a-zñáéíóúü]+)?\b', text_lower)
    
    # Contar todas las palabras
    all_counts = Counter(words)
    
    # Filtrar solo las palabras clave
    freqs = {kw: all_counts.get(kw, 0) for kw in KEYWORDS}
    
    return freqs

def main():
    # Leer entrada (archivo o stdin)
    if len(sys.argv) > 1:
        # Si se pasa un archivo como argumento
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                text = f.read()
        except UnicodeDecodeError:
            print(f"⚠️ Advertencia: intentando con 'latin-1' (archivo {filename})", file=sys.stderr)
            with open(filename, 'r', encoding='latin-1') as f:
                text = f.read()
    else:
        # Leer desde stdin (para tuberías: cat file.txt | python word_frequency.py)
        text = sys.stdin.read()

    # Contar frecuencias
    freqs = count_keyword_frequencies(text)

    # Calcular total para porcentajes
    total_found = sum(freqs.values())
    
    # Imprimir resultados ordenados por frecuencia (descendente)
    print("🔍 Frecuencia de palabras clave:")
    print("-" * 30)
    
    if total_found == 0:
        print("⚠️  No se encontraron ninguna de las palabras clave.")
    else:
        for word, count in sorted(freqs.items(), key=lambda x: -x[1]):
            pct = (count / total_found) * 100 if total_found > 0 else 0
            # Barra visual proporcional (máximo 30 caracteres)
            bar_len = int((count / max(freqs.values())) * 25) if max(freqs.values()) > 0 else 0
            bar = "█" * bar_len + "░" * (25 - bar_len)
            print(f"{word:12} | {count:5} | {bar} ({pct:.1f}%)")

    # Imprimir resumen
    print("-" * 30)
    print(f"✅ Total de palabras clave encontradas: {total_found}")
    
    # Opcional: mostrar total de palabras en el texto (para contexto)
    words_total = len(re.findall(r'\b\w+\b', text.lower()))
    print(f"📊 Total de palabras en el texto: {words_total:,}")

if __name__ == "__main__":
    main()
