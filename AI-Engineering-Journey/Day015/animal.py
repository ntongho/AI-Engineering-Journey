# Create: animal.py

# Requirements:
# Create a parent class Animal
# Attribute: name
# Method: eat()

# Create a child class Dog
# Additional method: bark()
# Create one object and demonstrate both methods.



class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print (f"{self.name} is  eating")


class Dog(Animal):

    def bark(self):
        print (f"{self.name} is  barking")


dog_1 = Dog("Bull Dog")

dog_1.eat()
dog_1.bark()