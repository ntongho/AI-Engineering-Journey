# Ask the user to enter a note.

# Save it to: note.txt

# using write mode.


note = input("Please enter note ")

with open("note.txt", "w") as file:
    file.write(note)