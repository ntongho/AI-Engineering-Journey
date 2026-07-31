# The calculator should:

# Ask for two numbers.
# Ask which operation: +,-,*,/
# Perform the calculation.

# Handle:
# Invalid numbers
# Division by zero
# Invalid operation
# The calculator should never crash because of user input.



def simple_calculator(num_1,operator,num_2):
       try: 
        if operator == "+":
            c = num_1 + num_2
            return c

        elif operator == "-":
                c = num_1 - num_2
                return c

        elif operator == "*":
                c = num_1 * num_2
                return c

        elif operator == "/":
                c = num_1 / num_2
                return c
        else:
              return "Invalid operator"
       except ZeroDivisionError:
             return "cannot divide by zero"

try:

    num_1, num_2 = map(int, input("Enter two number to perform calculation "  ).split())
    operator = input("Enter operator ")

    print(simple_calculator(num_1,operator,num_2))
except ValueError:
       print("invalid input")