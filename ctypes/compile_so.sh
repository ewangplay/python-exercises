#!/bin/sh

gcc -c -fPIC calc.c
gcc -shared calc.o -o calc.so

