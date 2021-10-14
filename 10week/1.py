import sys

n=int(input("회의의 수 :"))
list=[]
for i in range(n):
    start=int(input("%d번째 회의의 시작 시간 :" %(i+1)))
    finish=int(input("끝나는 시간 :"))
    list.append([start,finish])

s=sorted(list, key=lambda x:x[0])
max_num=[]
for i in range(n):
    cnt=1
    a=s[i][1]
    for j in range(n-i-1):
        if a==s[j+i+1][0]:
            cnt+=1
            a=s[j+i+1][1]
    max_num.append(cnt)

max_find=sorted(max_num, key=lambda x:x,reverse=True)
print("\n회의의 최대 개수 : ",max_find[0])
