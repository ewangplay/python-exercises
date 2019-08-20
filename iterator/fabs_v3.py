'''
Note: The iterator protocol is changed a bit in Python3.0. In the new protocol,iterator objects should have a method called __next__ rather than next, and a new built-in function called next may be used to access this method. In other words, next(it) is the equivalent of the pre-3.0 it.next().
'''
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self

fabs = Fibs()
for f in fabs:
    print(f)
    if f > 100:
        break
