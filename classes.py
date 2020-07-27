class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
print(point1.x)

print("------------------------------------")


# constructors

# add constructor to Point

# Exercise

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()

print("------------------------------------")


# Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):  # DOg class inherits all methods from Mammal
    def bark(self):  # python dosent like empty class so we just write pass
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.be_annoying()

