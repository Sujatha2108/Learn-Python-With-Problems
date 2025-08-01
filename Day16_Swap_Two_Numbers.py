def swap_Two_Numbers():
    num1=int(input("Enter First Number:"))
    num2=int(input("Enter Second Number:"))
    print("Before Swaping")
    print(f"Number1:{num1} and Number2:{num2}")
    num1,num2=num2,num1
    print("After Swaping")
    print(f"Number1:{num1} and Number2:{num2}")
swap_Two_Numbers()
