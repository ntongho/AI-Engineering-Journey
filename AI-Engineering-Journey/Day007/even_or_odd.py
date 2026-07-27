def is_even(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


user_input = int(input("Enter number to check "))
is_even(user_input)