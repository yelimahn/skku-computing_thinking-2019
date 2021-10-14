#level test 3번_안예림
'''
def fac1(n):
    if n==1:
        return 1
    return n*fac1(n-1)

def fac2(n):
    result=1
    for i in range(1, n+1):
        result*=i
    return result
        
def fac3(n):
    result=1
    while n>1:
        result=result*n
        n=n-1
    n=result
    return n
'''

def fac1(n):
    if n>1:
        return fac1(n-1)*n
    else:
        return 1
def fac2(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

def fac3(n):
    result=1
    while n!=0:
        result=result*n
        n=n-1
    return result

n=int(input("Please input 'n' for the factorial:"))

a=fac1(n)
print("The result of fac1 is",a)

a=fac2(n)
print("The result of fac2 is",a)

a=fac3(n)
print("The result of fac3 is",a)
