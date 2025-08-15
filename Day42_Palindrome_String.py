def palindrome_String():
    str=input("Enter String:").replace(" ","").lower()
    rev_str=str[::-1]
    print(f"Reverse of given String:{rev_str}")
    if rev_str == str:
        print(f"The given string is a palindrome : {rev_str}")
    else:
        print("The given string is not a palindrome")
palindrome_String()