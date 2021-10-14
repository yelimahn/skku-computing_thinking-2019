#5th Practice_1_안예림

def check(a):
    global m
    #음량의 범위는 0 미만이면 안되고 최대는 M이다.
    if a<=m and a>=0:
        return True
    else:
        return False
    
def choice(a,i):
    global l
    global n
    big=a+l[i]
    small=a-l[i]
    volume=[]
    if check(big):
        volume.append(big)
    if check(small):
        volume.append(small)
    i+=1
    while not i==n:
        add=volume
        volume=[]
        for j in range(len(add)):
            big=add[j]+l[i]
            small=add[j]-l[i]
            if check(big):
                volume.append(big)
            if check(small):
                volume.append(small)
        i+=1
    return volume

def max_select(a,b):
    if a>b:
        return a
    else:
        return b

l=[]
n=int(input("NCT가 노래할 곡 수 : "))#곡 수 : N
a=int(input("초기음량 : "))#초기 음량 : A
m=int(input("최대음량 : "))#최대 음량 : M
for i in range(n):
    vol=int(input("볼륨 하나씩 입력 :"))#각 노래가 시작 하기 전 가능한 볼륨의 차이
    l.append(vol)

i=0
last=choice(a,i)
max_vol=0
for x in range(0,len(last)):
    max_vol=max_select(max_vol,last[x])

print("NCT의 마지막 곡 음량 중 최댓값 : ",max_vol)

