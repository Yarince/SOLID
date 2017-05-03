import math


class Rectangle:
    height = None
    width = None

    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle(object):
    diameter = None

    def __init__(self, diameter):
        self.diameter = diameter


class WrongAreaCalculator:
    @staticmethod
    def area(shapes):
        area = 0

        for shape in shapes:
            if isinstance(shapes[0], Rectangle):
                area += shape.width * shape.height
            elif isinstance(shapes[0], Circle):
                area += int(shape.diameter * math.pi)
        return area


print(WrongAreaCalculator.area([Rectangle(10, 20)] * 5))
print(WrongAreaCalculator.area([Circle(10)] * 5))
