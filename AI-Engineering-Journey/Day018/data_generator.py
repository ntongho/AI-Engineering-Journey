# Make a generator that produces:

# "Data record 1"
# "Data record 2"
# "Data record 3"
# ...

# up to whatever number the user provides.

# For example:

# Enter number of records: 5

# Output:

# Data record 1
# Data record 2
# Data record 3
# Data record 4
# Data record 5




def record(n):
    for i in range(1, n + 1):
        yield f"Data record {i}"


user_input = int(input("Enter number of records: "))

for record_item in record(user_input):
    print(record_item)