class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_sides(self):
        return self.__a, self.__b, self.__c

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        sides = sorted([self.__a, self.__b, self.__c])
        return 0.5 * sides[0] * sides[1]

triangle = Triangle(3, 4, 5)
print("sides of triangle:", triangle.get_sides())
print("perimeter:", triangle.perimeter())
print("area:", triangle.area())
