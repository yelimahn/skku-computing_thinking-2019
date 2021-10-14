#1st Practice_4_안예림

num=int(input("2 이상의 자연수 입력 : "))
while not (num>=2):
    num=int(input("2 이상의 자연수 입력 : "))

#입력 받은 수가 소수인지 아닌지 판별하기
def prime_num(n):
    a=2

    while a<n:
        hap=n%a
        a+=1
        if hap==0:
            break

    if n==a:
        print("%d는 소수입니다" %n)
    else:
        print("%d는 소수가 아닙니다" %n)

#입력 받은 자연수까지의 소수를 모두 더한 값을 반환하기
def tail_prime(n):
    return prime_add(n,0)

def prime_add(n,sum):
    if n>1:
        for i in range(2, n+1):
            if n%i==0:
                break
        if n==i:
            return prime_add(n-1, n+sum)
        else:
            return prime_add(n-1,sum)
    else:
        print("입력한 자연수까지의 소수를 모두 더한 값 : ", sum)
        
print()
prime_num(num)
tail_prime(num)



    
