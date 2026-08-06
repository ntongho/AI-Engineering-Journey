# Parent: Vehicle

# Method: start()

# Child: Car

# Override:
# start()

# Parent prints: Vehicle started.

# Child prints: Car engine started.



class Vehicle:

    def start(self):
        print("Vehicle started.")



class Car(Vehicle):

    def start(self):
        print("Car engine started.")


car_1 = Car()
car_1.start()