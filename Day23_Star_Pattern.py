def starPattern():
    n=5
    for rows in range(1,n+1):
        for spaces in range(1,n-rows+1):
            print(" ",end="")
        for cols in range(1,2*rows):
            print("*",end="")
        print()
starPattern()
    
def starPattern2():
    n=5
    for rows in range(1,n+1):
        for cols in range(1,rows+1):
            print("*",end=" ")
        print()
starPattern2()

def starPattern1():
    n=5
    for rows in range(1,n+1):
        for cols in range(1,2*rows):
            print("*",end="")
        print()
starPattern1()


def starPattern3():
    n=5
    for rows in range(1,n+1):
        for cols in range(1,n-rows+1):
            print("*",end=" ")
        print()
starPattern3()
    
def starPattern3():
    n=5
    for rows in range(1,n+1):
        for cols in range(1,n-rows+1):
            print("*",end=" ")
        print()
starPattern3()
    