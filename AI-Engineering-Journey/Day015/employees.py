# Create: employees.py

# Parent class: Employee

# Attributes:
# name
# salary

# Method:
# display_info()

# Child classes:

# => Manager

# Extra attribute:
# department

# Override:
# display_info()
# Include department.

# => Developer

# Extra attribute:
# programming_language

# Override:
# display_info()
# Include language.
# Use super() where appropriate.

# Create at least one Manager and one Developer.
# Display their information.






class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def display_info(self):
        return f"Name: {self.name}\n Salary:{self.salary}"





class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name,salary)
        self.department = department

    def display_info(self):
        return f"Name: {self.name}\n Salary:{self.salary}\n Department:{self.department}"




class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name,salary)
        self.programming_language = programming_language

    def display_info(self):
        return f"Name: {self.name}\nSalary:{self.salary}\nLanguage:{self.programming_language}"

manager_1 = Manager("Mr.Hat", "$1000","Operations")
developer_1 = Developer("Mr.B", "$900", "Python")

print(developer_1.display_info())


