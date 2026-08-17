# Create:

# def count_up_to(n):
#     # use yield

# If you call:

# count_up_to(5)

# it should produce:

# 1
# 2
# 3
# 4
# 5

# Use a for loop to consume the generator.



def count_up_to(n):
    for i in range(1, n + 1):
        yield  i

result = count_up_to(5)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
