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

class FibsList:
    def __init__(self, fabs):
        self.fabs = fabs
    def __iter__(self):
        return self.fabs

fabs = Fibs()
for f in fabs:
    print(f)
    if f > 100:
        break

# 会接着上面的迭代结果继续迭代
# 因为这两个for循环用的同一个迭代对象
fabsList = FibsList(fabs)
for f in fabsList:
    print(f)
    if f > 1000:
        break
