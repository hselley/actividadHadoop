#!/usr/bin/env python3
import sys

length_counts = {}
for line in sys.stdin:
    length, count = line.strip().split('\t')
    length_counts[length] = length_counts.get(length, 0) + int(count)

for length, count in sorted(length_counts.items()):
    print(f"{length}\t{count}")