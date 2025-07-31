def ArmstrongNum():
    num=int(input("Enter a Number:"))
    temp=num
    s=0
    r=0
    while(num!=0):
        r=num%10
        s=s+(r*r*r)
        num=num//10
    if temp==s:
        print(f"It is Armstrong Number:{s}")
    else:
        print("It is not a Armstrong Number")
ArmstrongNum()