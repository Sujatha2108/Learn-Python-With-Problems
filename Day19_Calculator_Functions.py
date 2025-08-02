def Calculator_functions(a, b):
    Addition = a + b
    Subtraction = a - b
    Multiplication = a * b
    Division = a / b
    Modulo = a % b   
    return Addition, Subtraction, Multiplication, Division, Modulo  
a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))
add, sub, mul, div, mod = Calculator_functions(a, b)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
print(f"Modulo: {mod}")
