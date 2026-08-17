#!/usr/bin/env python3
""" Print word to lines """
import sys 

for line in sys.stdin:
    for word in line.split():
        print(word)