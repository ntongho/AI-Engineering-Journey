# Ask the user for a journal entry.

# Append it to: journal.txt

# Each new entry should appear on a new line.


journal_input = input("Please make a Journal Entry ")

with open("journal.txt","a") as file:
    file.write("\n"+journal_input)