from abc import ABCMeta, abstractmethod


# Wrong impl
class RectangleWrong(metaclass=ABCMeta):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self):
        return self.height * self.width


class SquareWrong(RectangleWrong):
    def __init__(self, width):
        super().__init__(width, width)
        RectangleWrong.register(SquareWrong)
        self.width = width

    def area(self):
        return self.width * self.width


# Right impl
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self): return None


class SquareRight(Shape):
    def __init__(self, width):
        Shape.register(SquareRight)
        self.width = width

    def area(self):
        return self.width * self.width


class RectangleRight(Shape):
    def __init__(self, width, height):
        Shape.register(RectangleRight)
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
