numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


numbers_2 = [3, 10, 15, 22, 27, 30, 41, 50]

big_numbers = [number for number in numbers_2 if number > 20]

print(big_numbers)