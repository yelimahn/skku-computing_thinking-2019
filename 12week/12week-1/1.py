import numpy as np
import sys
from matplotlib import pyplot as plt

a=np.empty((2,3),dtype='<U11')

a[0][0]="admin"
a[1][0]="1234"

print(a)
i=0

con=np.zeros((3,3),dtype=int)
b=np.full((1,3),0,dtype=int)

def add(b,code):
    money=int(input("입금할 금액 :"))
    b[0][code]+=money
    return b

def consume(name,b,code):
    global con
    print("%s님의 현재 잔액 : %d" %(name,b[0][code]))
    money=int(input("소비할 금액 :"))
    b[0][code]-=money
    i=0
    while con[code][i]!=0:
        i+=1
    con[code][i]=money
    print("%s님의 현재 잔액 : %d" %(name,b[0][code]))
    return b
    
def main(name):
    global a
    global con
    global b
    print("[메인화면] >>>0을 누르면 로그아웃되고 초기화면으로 돌아갑니다<<<")
    print("%s님 환영합니다!" %name)
    print("1. 통장금액 0원 세팅\n2. 계좌입금\n3. 소비\n4. 소비 패턴 보기\n5. 예금이자 이벤트")
    num=int(input(">>>"))

    for x in range(3):
        if a[0][x]==name:
            code=x
            
    if num==1:
        print("초기화 완료")
        print(b)
    elif num==2:
        b=add(b,code)
        
    elif num==3:
        b=consume(name,b,code)
        
    elif num==4:
        plt.plot([1.,2.,3.],con[code])
        plt.show()
        con_sum=con[code][0]+con[code][1]+con[code][2]
        con_sum/=3
        print("소비 평균 :",con_sum)

    elif num==5:
        interest=np.random.randint(0,10,(2,3))
        sum1=(interest[0][0]+interest[0][1]+interest[0][2])/3
        sum2=(interest[1][0]+interest[1][1]+interest[1][2])/3
        if sum1>sum2:
            inter=sum1*0.01
        else:
            inter=sum2*0.01
        b[0][code]+=b[0][code]*inter
        print("예금된 금액에 이자율을 곱한 금액 :",b[0][code])

    elif num==0:
        print("초기화면으로~")
        begin()
    main(name)
        

def register():
    global i
    global a
    global con
    i+=1
    name=input("사용자 이름 :")
    pw=input("비밀번호 :")
    for j in range(3):
        while a[0][j]==name:
            print("이름 중복, 다시 등록")
            name=input("사용자 이름 :")
            pw=input("비밀번호 :")
    a[0][i]=name
    a[1][i]=pw
    print(a)
    return name
    
def login():
    name=input("사용자 이름 :")
    pw=input("비밀번호 :")
    for j in range(3):
        if a[0][j]==name:
            if a[1][j]==pw:
                print("로그인 성공")
                break
            else:
                print("비밀번호가 틀렸습니다.")
        if j==2:
            print("존재하지 않는 계정입니다.")
    return name

        
def begin():
    print("[초기화면] >>>0을 누르면 종료됩니다<<<")
    num=int(input("1. 계정등록\n2. 계정 로그인\n>>>"))
    if num==1:
        name=register()
    elif num==2:
        name=login()
    elif num==0:
        print("종료")
        sys.exit()
    main(name)

begin()
