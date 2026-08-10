# Parent:
# Animal

# Method:
# speak()

# Children:
# Dog
# Cat
# Cow

# Each overrides speak().
# Store all three in a list.
# Loop through the list.

# Call:
# animal.speak()





class Animal:
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print("woof" )
    

    
class Cat(Animal):

    def speak(self):
        print("meow")



class Cow(Animal):

    def speak(self):
        print("moo")


animals = [Dog(),Cat(),Cow()]

for animal in animals:
    animal.speak()






