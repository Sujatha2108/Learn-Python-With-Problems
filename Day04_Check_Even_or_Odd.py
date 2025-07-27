def EvenOrOdd(num):
    if num%2==0:
        print(f"It is a Even number:{num}")
    else:
        print(f"It is a Odd number:{num}")
num=int(input("Enter a number:"))
result=EvenOrOdd(num)
print(result)