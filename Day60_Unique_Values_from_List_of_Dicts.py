import ast

def extract_unique_values(list_of_dicts):
    return {value for d in list_of_dicts for value in d.values()}
list_of_dicts = ast.literal_eval(
    input("Enter List of Dictionaries (e.g. [{'a': 1, 'b': 2}, {'a': 2, 'b': 4}, {'a': 1, 'b': 6}]): ")
)

unique_values = extract_unique_values(list_of_dicts)
print(f"Unique Values: {unique_values}")
