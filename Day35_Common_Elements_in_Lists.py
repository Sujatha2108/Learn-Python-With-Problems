from collections import Counter
list1=[3,5,6,7,3,2,4]
list2=[3,4,0,2,3,9,8]
c1=Counter(list1)
c2=Counter(list2)
common=list((c1&c2).elements())
print(f"Common Elements in the Lists : {common}")