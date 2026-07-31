# Ask the user for two numbers.

# Divide the first by the second.

# Handle:

# ValueError
# ZeroDivisionError



try:
    num_1, num_2 = map(int, input("input two numbers separated by space ").split())
    division = num_1 / num_2
    print(division)


except ZeroDivisionError:
    print("Cannot divide with zero")

except ValueError:
    print("invalid input")