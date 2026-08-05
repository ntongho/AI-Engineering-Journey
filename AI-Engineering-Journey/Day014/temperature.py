class Temperature:
    def __init__(self):
        pass

    @staticmethod
    def celsius_to_fahrenheit(c):
       return (c * 9/5) + 32

print(Temperature.celsius_to_fahrenheit(4))