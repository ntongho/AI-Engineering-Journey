# Imagine we're building an AI application that needs to save data.
# Create an abstract class:
# Storage

# with:
# save()
# load()

# Then create:
# FileStorage
# DatabaseStorage

# Each should implement its own version of:
# save()
# load()



from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass



class FileStorage(Storage):

    def save(self):
            print("Saving data to a file.")
    
    def load(self):
            print("Loading data from a file.")

class DatabaseStorage(Storage):

    def save(self):
          print("Saving data to a database.")

    def load(self):
          print("Loading data from a database.")


storage_system = [
     FileStorage(),
     DatabaseStorage()
]

for storage in storage_system:
     storage.save()
     storage.load()