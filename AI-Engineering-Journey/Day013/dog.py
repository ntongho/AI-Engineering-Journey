class Dog:
    def __init__(self,name,breed) -> None:
        self.name = name
        self.breed = breed

    def bark(self):
        print("Buddy says Woof!")
    
Dog_1 = Dog("Willow","bull dog")

Dog_1.bark()