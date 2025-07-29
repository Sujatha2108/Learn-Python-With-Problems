n=int(input("Enter a Number:"))
arr=[0,1]
for i in range(2,n):
    fibonacci=arr[i-1]+arr[i-2]
    arr.append(fibonacci)
print(f"fibonacci series:{arr}")