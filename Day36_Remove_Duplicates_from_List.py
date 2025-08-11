list1=[1,4,5,6,7,1,7,6,5,2,3]
unique_list=[]
for item in list1:
    if item not in unique_list:
        unique_list.append(item)
print(f"The list without duplicates :{unique_list}")
 
