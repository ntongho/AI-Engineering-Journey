
# Ask the user for a filename.

# Read the file.

# If it doesn't exist:

# Display:

# File not found.

# Use:except FileNotFoundError:

try:
    file_name = input("Input a file name with .extension to confirm if it exist \n").strip()
    with open(file_name,"r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")