class Dog:
    def __init__(self,name,breed) -> None:
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")
    
Dog_1 = Dog("Willow","bull dog")

Dog_1.bark()