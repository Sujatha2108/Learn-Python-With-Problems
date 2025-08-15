def binary_search(my_list,key):
    low=0
    high=len(my_list)-1
    while low<=high:
        mid=(low+high)//2
        if my_list[mid]==key:
            return mid
        elif my_list[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
list1=[1,2,3,4,5,6,7,8,9]
target=8
result=binary_search(list1,target)
if result!=-1:
    print(f"The Element {target} at index {result} ")
else:
    print("The Element not found")