# Ask the user for their age.

# If they enter text instead of a number, display a friendly message instead of crashing.

try:
    age = int(input("Please enter your age"))
    
except ValueError:
    print("Oops you did not enter a valid age")
