numbers = [5, 12, 17, 20, 25, 30, 33, 40]

big_numbers = filter(lambda number: number > 20, numbers)

print(list(big_numbers))