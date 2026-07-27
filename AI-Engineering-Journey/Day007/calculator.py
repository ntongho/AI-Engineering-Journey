def add(a,b):
    result = a + b
    return result



def multiply(a,b):
    result = a * b
    return result


number_1 = int(input("Input first number: "))
number_2 = int(input("Input second number: "))

print("Addition: ")
print(number_1," + ",number_2," =", add(number_1,number_2))

print("Multiplication: ")
print(number_1," * ",number_2," =", multiply(number_1,number_2))