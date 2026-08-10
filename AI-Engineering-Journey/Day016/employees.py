# Parent:
# Employee

# Method:
# work()

# Children:
# Manager
# Developer
# Designer

# Each overrides:
# work()

# Example outputs:
# Manager is managing the team.
# Developer is writing Python code.
# Designer is creating UI designs.

# Create a list containing all three.
# Loop through them.

# Call:
# employee.work()





class Employee:

    def work(self):
        pass

class Manager(Employee):

    def work(self):
       print("Manager is managing the team.")




class Developer(Employee):

    def work(self):
        print("Developer is writing Python code.")



class Designer(Employee):

    def work(self):
        print("Designer is creating UI designs.")


employees = [Manager(), Developer(), Designer()]

for employee in employees:
    employee.work()