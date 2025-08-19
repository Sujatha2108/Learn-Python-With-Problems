def recursive_power(n,p):
    if p==0:
        return 1
    return n*recursive_power(n,p-1)
num=int(input("Enter a number : "))
exp=int(input("Enter the power : "))
power=recursive_power(num,exp)
print(f"power of a Number : {power}")