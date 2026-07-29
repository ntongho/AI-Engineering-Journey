contacts = {
    "Alice": "08012345678",
    "Bob": "08098765432",
    "John": "08011112222"
}

name = input("Input name to do a check ")
if name in contacts:
    print(contacts[name])
else:
    print("Contact not found")