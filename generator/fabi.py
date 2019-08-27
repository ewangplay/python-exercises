#!/usr/local/bin/python3

import sys

def fabi(n):
    a = b = 1
    while True:
        if a > n:
            return 'done'
        yield a
        a, b = b, a+b

f = fabi(100)
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print(e.value)
        sys.exit()
