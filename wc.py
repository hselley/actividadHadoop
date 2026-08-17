#!/usr/bin/env python3
""" Count words """
import sys 
from functools import reduce

print(reduce(lambda x, _:x+1, sys.stdin, 0))