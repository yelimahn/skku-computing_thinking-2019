#Midterm Exam in Your Home_2_안예림

#각 돌은 순서대로 1~N까지 번호가 붙어 있으며,2차원 배열을 선언
n=int(input("돌의 개수 >> "))
d=[[0 for clo in range(2)] for row in range(n)]

#각 돌에는 점수가 적혀있다.
for i in range(n):
    d[i][0]=int(input("돌의 쓰여질 점수 >> "))

#돌을 밟을 때마다 돌에 쓰여진 점수를 누적해서 더해야 되고,
#돌의 합이 최대가 되도록 징검다리를 건너고 싶다.
score=0


def finish_n(i,d,score):
    global n
    #5. 마지막 N번째 돌은 꼭 밟아야 한다.
    #마지막 돌을 밟으면서 규칙을 어기지 않게 하는 조건
    if i==n-3:
        score+=d[n-1][0]
        d[n-1][1]=1
        print(d)
        return score
    elif i==n-2:
        score+=d[n-1][0]
        d[n-1][1]=1
        print(d)
        return score
    else:
        return 0


def next_stone(i,d,score):
    finish=finish_n(i,d,score)
    if finish!=0:
        return finish

    #3. 단, 연속된 세 개의 돌을 밟으면 안된다.
    if d[i][1]==1 and d[i-1][1]==1:
        score+=d[i+2][0]
        d[i+2][1]=1
        return next_stone(i+2,d,score)#밟는 돌로 넘어가서 다시 실행
    
    #1. 돌은 한번에 하나씩만 밟아야 하며, 작은 번호에서 높은 번호의 순서로 밟아야 한다.
    #2. i번째 돌을 밟은 상태라면, 다음번에는 i+1번째 돌이나 i+2번째의 돌을 밟을 수 있다.
    else:
        if d[i+1][0]>d[i+2][0]:
            score+=d[i+1][0]
            d[i+1][1]=1
            return next_stone(i+1,d,score)#밟는 돌로 넘어가서 다시 실행
        else:
            score+=d[i+2][0]
            d[i+2][1]=1
            return next_stone(i+2,d,score)#밟는 돌로 넘어가서 다시 실행


#D[i] 배열을 i번째 돌을 밟았을 때의 점수의 최대 누적 값으로 정의할 수 있다.
#단, 1,2번 돌에서는 그 최댓값이 무의미할 수 있기 때문에
#(예를 들어 0번:11,1번:29인데 1번을 밟았을 때 가질 수 있는 최댓값은 40이지만 총 최댓값으로 판단했을 경우에는 1번인 29만 밟는 것이 더 큰 결과값을 가질 수 있는 경우)
#그 경우를 고려하여 먼저 정리하였다.
        
def first_stone1(dd1):
    score1=0
    i=0
        
    score1+=dd1[0][0]#0번 돌 선택: 0,1 둘다 선택 or 0만 선택
    dd1[0][1]=1

    #0번 시작의 결과의 최댓값
    result1=next_stone(i,dd1,score1)
    return result1


def first_stone2(dd2):
    global n
    for j in range(n):
        dd2[j][1]=0
    
    score2=0
    i=1
    
    score2+=dd2[1][0]#0번 선택 안하고 1번 돌 선택
    dd2[1][1]=1

    #1번시작의 결과의 최댓값
    result2=next_stone(i,dd2,score2)
    return result2

#0번으로 시작하는 것이 최대인지,1번으로 시작이 최대인지 판별
def max_select(a,b):
    if a>b:
        return a
    else:
        return b


a=first_stone1(d)
b=first_stone2(d)
score=max_select(a,b)
print("돌의 누적 최댓값 : ",score)
