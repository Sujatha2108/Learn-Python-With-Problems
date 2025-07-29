n=int(input("Enter a number:"))
num=n
rev=0
remainder=0
while(n!=0):
    remainder=n%10
    rev=rev*10+remainder
    n=n//10
if num==rev:
    print(f"It is a palindrome Number:{rev}")
else:
    print("It is not a palindrome")
