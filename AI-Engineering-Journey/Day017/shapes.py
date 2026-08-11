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
from math import pi as p

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
       area = self.length * self.breadth
       print(area)


class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius


    def area(self):
        area = p * self.radius * self.radius
        print(area)


shapes = [Rectangle(4,3), Circle(4)]

for shape in shapes:
    shape.area()
    