#!/usr/bin/env python3
import sys

keywords = ['bueno', 'excelente', 'feliz', 'amor', 'malo', 'triste', 'odio']

for line in sys.stdin:
    words = [w.strip('.,!?":;').lower() for w in line.split()]
    for word in words:
        if word in keywords:
            label = 'pos' if word in ['bueno','excelente','feliz','amor'] else 'neg'
            print(f"{label}\t1")
