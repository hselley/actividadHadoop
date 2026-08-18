#!/usr/bin/env python3
import sys

counts = {'pos': 0, 'neg': 0}

for line in sys.stdin:
    label, cnt = line.strip().split('\t')
    counts[label] += int(cnt)

print(f"positivas\t{counts['pos']}")
print(f"negativas\t{counts['neg']}")
