# Create a class: LibraryBook

# Attributes:
# title
# author
# _available

# Methods:
# borrow()
# return_book()
# status()

# Rules:
# If available:
# Book borrowed successfully.

# Otherwise:
# Book is already borrowed.
# When returned:
# Book returned successfully.

class LibraryBook:
    def __init__(self, title, author, _available):
        self.title = title
        self.author = author
        self._available = _available

    def borrow(self):
        if self._available:
            self._available = False
            return "Book borrowed successfully."
        
        else:
            return "Book is already borrowed." 

    def return_book(self):
        self._available = True
        return "Book returned successfully."
        


    def status(self):
        if self._available:
            return f"{self.title} available"
        else:   
            return f"{self.title} unavailable"

Book1 = LibraryBook("Intro to chem","JJ Ok",False)

Book2 = LibraryBook("Intro to Bio","JJ Williams",True)

print(Book2.status())
print(Book2.borrow())
print(Book2.borrow())
print(Book1.return_book())