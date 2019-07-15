#!/usr/local/bin/python3

try: 
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    value = x / y
    print('x / y is', value)
except: # 有异常发生时执行
    print("Exception ~")
else: # 没有异常发生时执行
    print("It's ok!")
finally: # 不管有没有异常发生，都会执行
    print("bye-bye.")
