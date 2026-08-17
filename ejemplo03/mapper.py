#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) == 2:
        category, price = parts[0], parts[1]
        try:
            price = float(price)
            print(f"{category}\t{price}\t1")
        except ValueError:
            continue  # saltar líneas inválidas