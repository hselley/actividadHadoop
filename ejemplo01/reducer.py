#!/usr/bin/env python3
import sys
from functools import reduce

def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt,0) + 1
    return acc

dictionary = reduce(make_counts, map(str.strip, sys.stdin), {})

for word, count in dictionary.items():
    print(f'{word:<30}{count:>20}')
