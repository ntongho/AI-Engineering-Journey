# Requirements:
# Create a list of 5 numbers.
# Convert it into an iterator using iter().
# Use next() to retrieve each number.
# Observe what happens after the iterator is exhausted.



numbers = [1,2,3,4,5]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))