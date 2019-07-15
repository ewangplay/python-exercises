#!/usr/local/bin/python3

class A:
    def Hello(self):
        print("Hi, I'm from A")

class B(A):
    def Hello(self):
        print("Hi, I'm from B")

a = A()
a.Hello()
b = B()
b.Hello()

