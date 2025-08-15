numbers = [3, 5, 7, 8, 9, 2, 6]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")
