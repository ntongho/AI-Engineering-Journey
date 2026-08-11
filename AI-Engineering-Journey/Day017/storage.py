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
            pass
    
        def load(self):
            pass

class DatabaseStorage(Storage):

     def save(self):
          pass

     def load(self):
          pass
    