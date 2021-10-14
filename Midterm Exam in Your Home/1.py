#Midterm Exam in your home_1_안예림

#정수 n을 입력받는다.
n=int(input("정수를 입력 :"))

#X가 3으로 나누어 떨어지면, 3으로 나눈다.
def divide_3(n):
    n=n//3
    return n

#X가 2로 나누어 떨어지면, 2로 나눈다.
def divide_2(n):
    n=n//2
    return n

#1을 뺀다.
def minus_1(n):
    n=n-1
    return n

#횟수의 최솟값을 구하기 위해 n-1의 값이 3의 제곱수인 경우, 3으로 나누는 것이 횟수를 더 줄일 수 있다.
#n을 2로 나눌 때보다 더 적은 횟수로 할 수 있기 때문에 제곱수인지 아닌지 판별한다.
def decide_3(n,square):
    d3=n-1
    while d3%3==0:
        d3=d3//3
        if d3==1:
            square=True
            break
        elif d3==2:
            square=False
            break
    else:
        square=False
    return square
            

result=False
square=True
cnt=0

#정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
while not result:
    if n%3==0:
        n=divide_3(n)
        print("3 divide : %d\n" %n)
        cnt+=1
    elif n%2==0:
        square=decide_3(n,square)
        if square:
            n=minus_1(n)
            print("1 minuse :%d\n" %n)
            cnt+=1
        else:
            n=divide_2(n)
            print("2 divide : %d\n" %n)
            cnt+=1
    else:
        n=minus_1(n)
        print("1 minuse :%d\n" %n)
        cnt+=1
    if n==1:
        result=True

#연산을 사용하는 횟수의 최소값을 출력 하시오.      
print("연산을 사용하는 횟수의 최솟값 : ",cnt)
