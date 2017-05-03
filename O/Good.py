# Right implementation
import math
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self): return None


class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.register(Rectangle)
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


class Circle(Shape):
    def __init__(self, diameter):
        Shape.register(Circle)
        self.diameter = diameter

    def area(self):
        return int(self.diameter * math.pi)


class RightAreaCalculator:
    @staticmethod
    def area(shapes):
        area = 0
        for shape in shapes:
            area += shape.area()
        return area


print(RightAreaCalculator.area([Rectangle(10, 20)] * 5))
print(RightAreaCalculator.area([Circle(10)] * 5))
