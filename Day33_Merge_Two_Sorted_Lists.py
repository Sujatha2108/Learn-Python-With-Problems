def merge_Two_Sorted_lists(l1,l2):
    return sorted(l1+l2)
list1=[7,9,6,8,19,20]
list2=[59,34,90,87,45,2]
Merged_list=merge_Two_Sorted_lists(list1,list2)
print(f"The Merged list of Two sorted lists is :{Merged_list}")