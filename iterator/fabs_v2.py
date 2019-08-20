'''
Note In formal terms, an object that implements the __iter__ method is iterable, and the object implementing next is the iterator.
'''
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    # 实现这个方法的对象被称为迭代器
    def next(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    # 实现这个方法的对象是可迭代的
    def __iter__(self):
        return self

fabs = Fibs()

for f in fabs:
    print(f)
    if f > 100:
        break
