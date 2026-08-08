
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

class Shape():
    def area(self):
        pass

class Rectangle(Shape):
    def area(self,length,breadth):
        return length * breadth
    
class Circle(Shape):
    def area(self,radius):
        return p * radius * radius
    

circle_1 = Circle()
print(circle_1.area(2))

rect_1 = Rectangle()
print(rect_1.area(2,4))