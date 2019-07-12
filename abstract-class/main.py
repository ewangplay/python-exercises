#!/usr/local/bin/python3

from abc import ABC,abstractmethod

class Animal(ABC):
    # 这是装饰器表示这是一个抽象方法，在子类中必须实现
    @abstractmethod
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print("Miao ~~~")
    def run(self):
        print("Cat running...")
    
# 抽象类不能被实例化
# n = Animal()
# n.talk()

cat = Cat()
print("Is cat a Cat Class:", isinstance(cat, Cat))
print("Is cat a Animal Class:", isinstance(cat, Animal))
cat.talk()
cat.run()
