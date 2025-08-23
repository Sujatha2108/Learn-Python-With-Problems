import ast
def sort_dict_by_values(d, reverse=False):
    """
    Sort dictionary by values.
    reverse=False -> ascending
    reverse=True  -> descending
    """
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))
dict1 = ast.literal_eval(input("Enter Dictionary (e.g. {'a': 10, 'b': 2, 'c': 15}): "))
order = input("Sort order? (asc/desc): ").strip().lower()
if order == "desc":
    sorted_dict = sort_dict_by_values(dict1, reverse=True)
else:
    sorted_dict = sort_dict_by_values(dict1, reverse=False)

print(f"The Sorted Dictionary: {sorted_dict}")
