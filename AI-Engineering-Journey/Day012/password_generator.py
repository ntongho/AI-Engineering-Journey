# Requirements:
# Ask the user how many characters the password should have.
# Use: random, string
# Generate a random password containing:
# Letters
# Numbers
# Print the password.

import random
import string

def password_generator(pass_length):
    string_combo = string.ascii_letters + string.digits
    character = "".join(random.choices(string_combo, k = pass_length ))
    return character

pass_length = int(input("Enter the length of password you want "))
print(password_generator(pass_length))