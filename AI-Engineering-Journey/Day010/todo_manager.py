# The program should:

# Ask the user for a task.
# Save the task to todo.txt.
# Ask if they want to add another task.
# Keep asking until they type no.
# Display all saved tasks at the end.

# Hint: Combine what you've learned about loops, file handling, and user input.

while True:
    task_input = input("Enter task ")
    with open("todo.txt", "a") as file:
            file.write("\n"+task_input)

    exit_status = input("Do you want to add another task ? ")

    if exit_status.strip().lower() == "no":
            break


with open("todo.txt","r") as file:
       print(file.read())