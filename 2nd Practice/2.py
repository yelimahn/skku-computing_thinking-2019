#2st Practice_2_안예림

#(1)   함수1: 정렬이 완료되어도 loop를 끝까지 도는 버블 정렬
def loop1(num):
    length = len(num)
    for i in range(length):
        for j in range(length-1):
            if num[j+1] < num[j]:
                num[j],num[j+1]=num[j+1],num[j]
    return num

#(2)   함수2: 정렬이 완료되면 loop를 멈추는 버블 정렬(재귀 사용 안함)
def loop2(num):
    length = len(num)
    for i in range(length-1):
        for j in range(length-i-1):
            if num[j+1] < num[j]:
                num[j],num[j+1]=num[j+1],num[j]
            else:
                break
        if num[j]<num[j+1]:
            return num

#(3)   함수3: 정렬이 완료되면 loop를 멈추는 버블 정렬(재귀를 사용함)
def loop3(num):
    swap=0
    for i in range(len(num)-1):
        if num[i]>num[i+1]:
            num[i],num[i+1]=num[i+1],num[i]
            swap+=1
    if swap==0:
        return num
    else:
        return loop3(num)

#(4)   리스트에 정렬할 숫자를 입력 받습니다. 숫자가 아니면 다시 입력해야 합니다. n 또는 N이 들어오면 정지합니다.
num=[]
while True:
    num1=input("숫자를 입력 :")
    while not num1.isdigit():
        if num1=='n' or num1=='N':
            break
        num1=input("숫자를 다시 입력 :")
    if num1=='n' or num1=='N':
        break
    num.append(num1)
print(num)

#(5)   실제로 성능이 개선되었는지 알기 위해 time을 사용하여 함수 3개가 각각 실행되는데 걸린 시간을 비교하고 가장 빠른 버블 정렬부터 나열하세요.
import time

start1=time.time()
after1=loop1(num)
print(after1)
end1=time.time()

processTime=end1-start1
print(processTime)

start2=time.time()
after2=loop2(num)
print(after2)
end2=time.time()

processTime=end2-start2
print(processTime)

start3=time.time()
after3=loop3(num)
print(after3)
end3=time.time()

processTime=end3-start3
print(processTime)

print("버블 정렬 빠른 순서대로 나열 : 함수2, 함수1, 함수3")
