def numberConversion():
    num = int(input("Enter a Decimal Number: "))

    binary = bin(num)      
    octal = oct(num)       
    hexadecimal = hex(num) 

    print(f"Binary: {binary}")
    print(f"Octal: {octal}")
    print(f"Hexadecimal: {hexadecimal}")

numberConversion()
