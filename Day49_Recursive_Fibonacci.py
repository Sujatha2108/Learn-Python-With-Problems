def recursive_fibnacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        seq=recursive_fibnacci(n-1)
        seq.append(seq[-1]+seq[-2])
        return seq
num=int(input("Enter a number :"))
fib=recursive_fibnacci(num)
print(f"fibonacci series:{fib}")