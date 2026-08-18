#!/usr/bin/env python3
import sys
from collections import defaultdict

total = defaultdict(int)
for line in sys.stdin:
    word, count = line.strip().split('\t')
    total[word] += int(count)

for word, count in sorted(total.items(), key=lambda x: -x[1]):
    print(f"{word:<15}{count}")
