n=int(input("Enter a number:"))
rev=0
remainder=0
while(n!=0):
    remainder=n%10
    rev=rev*10+remainder
    n=n//10
print(f"Reverse of a given Number is:{rev}")
