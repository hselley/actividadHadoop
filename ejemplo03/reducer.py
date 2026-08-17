#!/usr/bin/env python3
import sys

total = {}
count = {}

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue
    cat, price_str, cnt_str = parts
    price = float(price_str)
    cnt = int(cnt_str)

    total[cat] = total.get(cat, 0) + price
    count[cat] = count.get(cat, 0) + cnt

for cat in sorted(total):
    avg = total[cat] / count[cat]
    print(f"{cat:<25} {avg:.2f}")
