import pandas as pd
import ast
def merge_dict(d1,d2):
    df1=pd.DataFrame(d1)
    df2=pd.DataFrame(d2)
    merged=pd.merge(df1,df2,on="id")
    return merged
dict1=ast.literal_eval(input("Enter Dictionary1 : "))
dict2=ast.literal_eval(input("Enter Dictionary2 : "))
merged_dictionaries=merge_dict(dict1,dict2)
print(f"The Merged Dictionaries : ",merged_dictionaries)


import ast

def merge_dict(d1, d2):
    merged = {**d1, **d2}   # Python dictionary unpacking
    return merged

dict1 = ast.literal_eval(input("Enter Dictionary1: "))
dict2 = ast.literal_eval(input("Enter Dictionary2: "))

merged_dictionaries = merge_dict(dict1, dict2)
print(f"The Merged Dictionaries: {merged_dictionaries}")
