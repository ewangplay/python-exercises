class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

r = Rectangle()
r.size = 10,20
print(r.size)
print(r.width, r.height)
r.width = 50
r.height = 60
print(r.size)
