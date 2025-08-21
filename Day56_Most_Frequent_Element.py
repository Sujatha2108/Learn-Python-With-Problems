from collections import Counter
import ast
def most_frequent(lst):
    freq = Counter(lst)
    most_common = freq.most_common(1)[0]
    return most_common
list1=ast.literal_eval(input("enter a list:"))
result=most_frequent(list1)
print("Most frequent element:",result)