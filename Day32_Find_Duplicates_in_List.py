my_list = [1, 2, 2, 3, 4, 4, 5]
seen = set()
duplicates = set()

for item in my_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(f"Duplicate elements: {list(duplicates)}")