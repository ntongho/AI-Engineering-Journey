class student:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

student_1 = student("Benjamin","22","Nigeria")
student_2 = student("Joseph","20","Nigeria")

print(student_1.name)
print(student_1.age)
print(student_1.country)
print(" \n")
print(student_2.name)
print(student_2.age)
print(student_2.country)