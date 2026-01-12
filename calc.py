# Version 3: Added multiplication
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

print("2 + 2 =", add(2, 2))
print("5 - 3 =", subtract(5, 3))
print("10 * 2 =", multiply(10, 5))

def divide(a, b):
    if b == 0:
        return "Error! Division by zerooooooo"
    return a / b

print("10 / 2 =", divide(10, 2))