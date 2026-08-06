# Create: person.py

# Parent: Person

# Attributes:name

# Method: introduce()

# Child: Student

# Additional attribute: course

# Additional method: study()

# Use super() inside the constructor.


class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello {self.name}")



class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course} ")

student_1 = Student("Benjamin","Computer science")

student_1.study()
student_1.introduce()