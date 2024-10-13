import math

class Shape:
    def area(self):
        raise NotImplementedError("Derived classes oeride this method")

class Rectangle(Shape):
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius:int):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi
