
class Bird():
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Ahhh~~~")
            self.hungry = False
        else:
            print("No, tranks!")

class SongBird(Bird):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound
    def sing(self):
        print(self.sound)
    
b1 = Bird()
b1.eat()
b1.eat()

b2 = SongBird("gagaga~~~")
b2.sing()
b2.eat()
