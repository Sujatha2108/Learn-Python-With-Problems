def countdigits():
    num = int(input("Enter a Number: "))
    count = 0
    n = abs(num)  # Handle negative numbers

    if n == 0:
        count = 1  # Edge case: single-digit 0
    else:
        while n != 0:
            n = n // 10
            count += 1

    print(f"Count of digits: {count}")

countdigits()

