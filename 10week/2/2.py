#10week_2_안예림

def admin():
    file=open("members.txt","w")
    name="admin"
    password="1234"
    members={}
    members[name]=(password,0,0)
    password,account,loan=members[name]
    line=name+','+str(password)+','+str(account)+','+str(loan)+'\n'
    file.write(line)
    file.close()
    
def load_mem():
    file=open("members.txt","r")
    members={}
    for line in file:
        name,password,account,loan=line.strip('\n').split(',')
        members[name]=(str(password),int(account),int(loan))
    file.close()
    return members

def store_mem(members,password):
    file=open("members.txt","w")
    names=members.keys()
    members[name]=(0,0,0)
    for name in names:
        password,account,loan=members[name]
        line=name+','+str(password)+','+str(account)+','+str(loan)+'\n'
        file.write(line)
    file.close()
    return members

def register():
    name=input("계정 등록, 사용자 이름 입력 : ")
    members=load_mem()
    while name in members.keys():
        name=input("이름 중복, 사용자 이름 다시 입력 : ")
    password=input("비밀번호 입력 :")
    return store_mem(members,password)

def login():
    name=input("로그인, 이름 입력 : ")
    password=input("비밀번호 입력 :")
    members=load_mem()
    if name in members.keys():
        if members[name][0]!=password:
            print("비밀번호가 틀렸습니다.")
        else:
            return members
    else:
        print("없는 계정입니다.")
    
def begin():
    print("성균 은행")
    print("1. 계정 등록 \n2.계정 로그인\n")
    first=input(">>>0을 누르면 종료됩니다<<<")
    if first=='0':
        print("종료")
        import sys
        exit()
    elif first=='1':
        members=register()
        members=login()
    elif first=='2':
        members=login()
    main(members)

def statement(members):
    global state
    if len(state)>5:
        for i in range(len(state)-5):
            del state[0]
    elif len(state)==0:
        print("입출금 내역 혹은 대출 및 상환 내역이 없습니다.")
    print(state)
    main(members)

def deposit(members):
    global state
    print(account)
    print(members)
    money=int(input("계좌에 입금할 금액 : "))
    name=list(members.keys())
    name=name[0]
    file=open("members.txt","w")
    account+=money
    state.append("입금 : +%d원" %money)
    print("잔액 :",account)
    line=name+','+str(password)+','+str(account)+','+str(loan)+'\n'
    file.write(line)
    file.close()
    main(members)

def withdraw(members):
    global state
    print("잔액 :",account)
    money=int(input("계좌에서 출금할 금액 : "))
    account-=money
    file=open("members.txt","w")
    line=name+','+str(password)+','+str(account)+','+str(loan)+'\n'
    file.close()
    state.append("출금 : -%d원" %money)
    main(members)
    
def borrow(members):
    global state
    print("현재 잔액 :",account)
    print("현재 잔액의 50% 이하에 해당하는 금액을 대출할 수 있습니다.")
    global cash
    print("은행의 현금 보유액 :",cash)
    print("대출 시작")
    while True:
        m1=int(input("1000원>>"))
        m5=int(input("5000원>>"))
        m10=int(input("10000원>>"))
        m50=int(input("50000원>>"))
        if m1>cash['1000'] or m5>cash['5000'] or m10>cash['10000'] or m50>cash['50000']:
            print("은행 권종 부족, 다시 입력")
        else:
            mm=m1*1000+m5*5000+m10*10000+m50*50000
            if (mm*2)<account:
                yesno=input("총 %d원을 대출하시겠습니까? (y/n)" %mm)
                if yesno=='y' or yesno=='Y':
                    break
            else:
                print("잔액 부족, 다시 입력")
    cash['1000']-=m1
    cash['5000']-=m5
    cash['10000']-=m10
    cash['50000']-=m50
    state.append("대출 : -%d원" %mm)
    main(members)
    
def repay(members):
    global state
    print("대출 잔액 :",loan)
    global cash
    print("대출 상환 시작")
    while True:
        m1=int(input("1000원>>"))
        m5=int(input("5000원>>"))
        m10=int(input("10000원>>"))
        m50=int(input("50000원>>"))
        mm=m1*1000+m5*5000+m10*10000+m50*50000
        yesno=input("총 %d원을 대출하시겠습니까? (y/n)" %mm)
        if yesno=='y' or yesno=='Y':
                    break
    cash['1000']+=m1
    cash['5000']+=m5
    cash['10000']+=m10
    cash['50000']+=m50
    state.append("대출 상환 : +%d원" %mm)
    main(members)

def main(members):
    print("\n[메인화면]\n>>>0을 누르면 로그아웃되고 초기화면으로 돌아갑니다<<<")
    print("%s님 안녕하세요!"%members)
    bank=input("1. 은행 이용 내역\n2. 계좌 입금\n3. 계좌 출금\n4. 대출하기\n5. 대출 상환하기\n")
    if bank=='0':
        print("로그아웃")
        begin()
    elif bank=='1':
        statement(members)
    elif bank=='2':
        deposit(members)
    elif bank=='3':
        withdraw(members)
    elif bank=='4':
        borrow(members)
    elif bank=='5':
        repay(members)
    
cash={'1000':20,'5000':3,'10000':20,'50000':4}
state=[]
admin()
begin()
    
