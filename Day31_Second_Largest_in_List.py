n=[5,76,34,89,23,16,19,56]
my_list=list(set(n))
my_list.sort()
if len(my_list)<2:
    print("The list doesnot contain second largest number")
else:
    second_largest=my_list[-2]
    print(f"The second largest number is :{second_largest}")