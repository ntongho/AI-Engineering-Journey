class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)

book_1 = Book(" Python Basics","John Doe")

book_1.display()