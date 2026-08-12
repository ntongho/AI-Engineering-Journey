# Parent:
# Shape

# Abstract method:
# area()
# Children:

# Rectangle
# Circle

# The rectangle should calculate:
# length × width

# The circle should use:
# math.pi

# The important part is that both provide:
# shape.area()
# but calculate the result differently.
# You're combining abstraction + polymorphism.



from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
       area = self.length * self.breadth
       return area


class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius


    def area(self):
        area = pi * self.radius ** 2
        return area


shapes = [
    Rectangle(4,3), 
    Circle(4)
    ]

for shape in shapes:
    print(shape.area())
    