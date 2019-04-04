# -*- coding: utf-8 -*-

from ctypes import *
 
calc = CDLL('./calc.so')
 
res = calc.add(4,5)
print("4 + 5 = " + str(res))

res = calc.multiply(4,5)
print("4 * 5 = " + str(res))
