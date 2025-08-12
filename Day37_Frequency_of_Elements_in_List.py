from collections import Counter
my_list=[1,3,2,4,1,4,2,3,8,0,8,9,6,7,0]
frequency=Counter(my_list)
print(f"The frequency of the elements in list : {dict(frequency)}")
