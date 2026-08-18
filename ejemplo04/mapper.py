#!/usr/bin/env python3
import sys
import re
from collections import Counter

KEYWORDS = ['bueno', 'excelente', 'feliz', 'amor', 'malo', 'triste', 'odio']

for line in sys.stdin:
    text = line.lower()
    words = re.findall(r'\b[a-zñáéíóúü]+\b', text)
    counts = Counter(words)
    
    # Emitir solo las palabras clave con su conteo
    for kw in KEYWORDS:
        if counts[kw] > 0:
            print(f"{kw}\t{counts[kw]}")
