# Use Python's math module.
# Ask the user for a radius.
# Calculate:
# Circumference
# Area
# Use: math.pi

import math
def circle_calculator():
    radius = int(input("Please enter a value for radius "))
    circumference = round((2 * math.pi * radius),2)
    area = round( math.pi * (radius ** 2),2)
    print(" Circumference: ", circumference,"\n Area: ", area )

if __name__ == "__main__":
    circle_calculator()