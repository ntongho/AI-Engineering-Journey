
# Parent:
# Shape

# Method:
# area()
# Child classes:

# Rectangle
# Circle
# Each should calculate its own area.
# Rectangle:
# length × width

# Circle:
# Use:
# import math




from math import pi as p

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
            print(self.length * self.breadth )
class Circle(Shape):

   
    def __init__(self,radius):
        self.radius = radius

    def area(self):
            print(p * self.radius * self.radius)
    

shapes = [Rectangle(1,4), Circle(4)]

for shape in shapes:
    shape.area()