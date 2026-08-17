# Write:

# def generate_records(n):
#     ...

# It should generate:

# Training record 1
# Training record 2
# Training record 3
# ...

# using yield.

# Then:

# records = generate_records(5)


# for record in records:
#     print(record)

# Expected:

# Training record 1
# Training record 2
# Training record 3
# Training record 4
# Training record 5



def generate_records(n):
    for i in range(1, n + 1):
        yield f" Training record {i}"


user_input = int(input("Enter number of records: "))

for record_item in generate_records(user_input):
    print(record_item)