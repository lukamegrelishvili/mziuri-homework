class Animal:
    def eat(self):
        pass

    def talk(self):
        pass

    def walk(self):
        pass


class Cat(Animal):
    def eat(self):
        return "Cat eats a milk"

    def talk(self):
        return "Cat says miaww"

    def walk(self):
        return "Cat can run 20km/h"


class Dog(Animal):
    def eat(self):
        return "Dog eats a bone"

    def talk(self):
        return "Dog says Aww"

    def walk(self):
        return "Dog can run 40km/h"



animals = (Cat(), Dog())

for animal in animals:
    print(animal.eat())
    print(animal.talk())
    print(animal.walk())
