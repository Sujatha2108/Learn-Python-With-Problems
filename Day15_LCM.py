def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def find_lcm(a,b):
    gcd=find_gcd(a,b)
    lcm=(a*b)//gcd
    return lcm
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = find_lcm(num1, num2)
print(f"The lcm of {num1} and {num2} is: {lcm}")

 **method-2**
import math

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = math.lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")

