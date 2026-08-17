#!/usr/bin/env python3
import sys
from functools import reduce

def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt,0) + 1
    return acc

dictionary = reduce(make_counts, sys.stdin, {})
items = dictionary.items()

for item in items:
    for x in item:
        print(x)