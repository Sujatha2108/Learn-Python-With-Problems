def remove_spaces(s):
    removed_string=s.replace(" ","")
    return removed_string
string1=input("Enter a String:")
result=remove_spaces(string1)
print(f"The string after removing all spaces : {result}")
