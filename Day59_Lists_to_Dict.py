import ast

keys = ast.literal_eval(input("Enter list of keys (e.g. ['a','b','c']): "))
values = ast.literal_eval(input("Enter list of values (e.g. [1,2,3]): "))

my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(f"The Resulting Dictionary: {my_dict}")
