class Rectangle:
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length


obj1 = Rectangle(1, 5, "blue")
obj2 = Rectangle(3, 3, "green")
obj3 = Rectangle(3, 7, "purple")


print(f"Obj1: Width={obj1.width}, Length={obj1.length}, Color={obj1.color}, Perimeter={obj1.perimeter()}, Area={obj1.area()}")
print(f"Obj2: Width={obj2.width}, Length={obj2.length}, Color={obj2.color}, Perimeter={obj2.perimeter()}, Area={obj2.area()}")
print(f"Obj3: Width={obj3.width}, Length={obj3.length}, Color={obj3.color}, Perimeter={obj3.perimeter()}, Area={obj3.area()}")
