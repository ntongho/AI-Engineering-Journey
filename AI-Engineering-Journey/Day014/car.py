# Create a class:Car

# Attributes:
# brand
# model

# Class Variable:
# wheels = 4

# Method: display()

# Print:
# Brand: Toyota
# Model: Corolla
# Wheels: 4


class Car:

    wheels = 4
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nWheels: {Car.wheels}"

car1 = Car("Toyota","Corolla")
print(car1.display())