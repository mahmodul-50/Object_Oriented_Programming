from abc import ABC, abstractmethod

# abc = Abstract Base Classes
# It is a built-in Python module (no install needed) that helps to create abstract classes.


class Shape(ABC):
    @abstractmethod
    # Why @abstractmethod?
    # Every child class must implement this method.
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius


shapes = [Rectangle(10, 5), Circle(7)]

for shape in shapes:
    print("Area:", shape.area())
