names = ["Benjamin", "Ada", "Alexander", "Bob", "Christopher"]

# List comprehension #
big_names = [name for name in names if len(name) > 5] 
##


print(big_names)


# filter + lambda
big_names_filtered = filter(lambda name: len(name) > 5, names)

print(list(big_names_filtered))