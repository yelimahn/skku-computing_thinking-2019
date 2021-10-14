import numpy as np
import sys

#Numpy를 사용하여 학생들의 성적을 관리하는 프로그램
print("학생 성적 관리 프로그램")
stu_num=int(input("학생 수 :"))

a=np.random.randint(0,101,(stu_num,4))


def score_print():
    global stu_num
    global a

    #총 몇 명이 있는지 알려주고,
    print("\n1번부터 %d번까지 총 %d명의 학생이 있습니다." %(stu_num,stu_num))
    order=int(input("학생의 번호 :"))
    
    #범위를 넘어서는 값을 입력할 경우 다시 입력하라고 합니다.
    while not (order<=stu_num and order>0):
        order=int(input("학생의 번호 :"))
        
    #해당 학생의 네 과목 점수와 평균이 출력
    print("==%d번 학생의 점수==" %order)
    print("국어 : ",a[order-1,0])
    print("수학 : ",a[order-1,1])
    print("영어 : ",a[order-1,2])
    print("한국사 : ",a[order-1,3])
    
    ave=0
    for i in range(4):
        ave+=a[order-1][i]
    ave=ave/4
    print(">>평균 : ",ave)


def score_revise():
    global stu_num
    global a

    #학생의 번호를 입력하면 해당 학생의 네 과목 점수를 수정할 수
    print("\n1번부터 %d번까지 총 %d명의 학생이 있습니다." %(stu_num,stu_num))
    order=int(input("학생의 번호 :"))
    while not (order<=stu_num and order>0):
        order=int(input("학생의 번호 :"))

    score=[]
    print("==%d번 학생의 점수 수정==" %order)
    #범위를 넘어서는 값을 입력할 경우 다시 입력하라고
    korean=int(input("국어 :"))
    while not (korean>=-1 and korean<=100):
        korean=int(input("국어 :"))
    math=int(input("수학 :"))
    while not (math>=-1 and math<=100):
        math=int(input("수학 :"))
    english=int(input("영어 :"))
    while not (english>=-1 and english<=100):
        english=int(input("영어 :"))
    history=int(input("한국사 :"))
    while not (history>=-1 and history<=100):
        history=int(input("한국사 :"))
    score.append(korean)
    score.append(math)
    score.append(english)
    score.append(history)

    #단, -1이 입력되면 이전의 점수가 유지됩니다. 
    for i in range(4):
        if score[i]!=-1:
            a[order-1,i]=score[i]

  
def average():
    global stu_num
    global a
    
    #과목별 평균과 분산을 계산
    print("\n==과목별 평균과 분산==")
    sub=["국어","수학","영어","한국사"]
    for i in range(4):
        ave=0
        ave2=0
        for j in range(stu_num):
            ave+=a[j][i]
            ave2+=a[j][i]*a[j][i]
        ave=ave/stu_num
        ave2=ave2/stu_num
        print(sub[i],"평균 : %.2f" %ave)
        print(sub[i],"분산 : %.2f"%(ave2-ave*ave))
    
def stu_ave():
    global stu_num
    global a
    print("\n학생의 번호를 각각 입력, 0을 입력하면 종료")
    stud=[]
    #학생의 번호를 입력하고 마지막에 0이 들어오면 입력한 학생의 평균과 분산을 계산
    while True:
        order=int(input("학생의 번호 :"))
        if order==0:
            break
        else:
            stud.append(order)
    print(stud)
    sub=["국어","수학","영어","한국사"]
    for i in range(4):
        ave=0
        ave2=0
        for j in stud:
            ave+=a[j-1][i]
            ave2+=a[j-1][i]*a[j-1][i]
        ave=ave/len(stud)
        ave2=ave2/len(stud)
        print(sub[i],"평균 : %.2f" %ave)
        print(sub[i],"분산 : %.2f" %(ave2-ave*ave))
    
def menu():
    print("\n====MENU====\n")
    print("1. 학생의 점수 출력")
    print("2. 학생의 점수 수정")
    print("3. 평균, 분산 계산")
    print("4. 학생별 평균, 분산 계산")
    print("0. 종료")
    num=int(input(">>"))

    #0이 입력되면 종료됩니다.
    if num==0:
        print("종료됩니다.")
        sys.exit()
    elif num==1:
        #학생 점수 출력
        score_print()
    elif num==2:
        #학생 점수 수정
        score_revise()
    elif num==3:
        #전체 평균, 분산
        average()
    elif num==4:
        #학생 평균, 분산
        stu_ave()
    else:
        print("다시 입력!")
    menu()

menu()

    
