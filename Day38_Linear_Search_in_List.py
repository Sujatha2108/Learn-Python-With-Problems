def linear_search(my_list,key):
    for i in range(len(my_list)):
        if my_list[i]==key:
            return i
    return -1
list1=[3,5,7,8,9,2,6]
target=8
result=linear_search(list1,target)
if result!=-1:
    print(f"The Element {target} at index {result} ")
else:
    print("The Element not found")