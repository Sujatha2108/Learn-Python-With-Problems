import ast
def flatten(nested_list):
    flat_list = []
    stack = nested_list[::-1]   

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])   
        else:
            flat_list.append(item)

    return flat_list
user_input = input("Enter a nested list: ")


nested = ast.literal_eval(user_input)
print("Input:", nested)
print("Flattened:", flatten(nested))
