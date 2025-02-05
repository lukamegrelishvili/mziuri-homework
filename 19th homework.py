class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say_hi(self):
        print(f"Hello my name is {self.name} with color {self.color} and I am an animal")


class Dog(Animal):
    def say_hi(self):
        print(f"Hello my name is {self.name} with color {self.color}and im a dog")

#class Animal
animal = Animal("Milo", "brown")
animal.say_hi()

#class Dog
my_dog = Dog("Buddy", "black")
my_dog.say_hi()
