# Create:
# def countdown(n):

# It should use yield.
# Example:
# 5
# 4
# 3
# 2
# 1

# Then:
# for number in countdown(5):
#     print(number)



def countdown(n):
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

for number in countdown(5):
    print(number)
   