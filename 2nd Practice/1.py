#2nd Practice_1_안예림

#우리는 주소록의 이름을 정렬하려고 합니다.

#(1) 주소록의 개수 N을 입력합니다.
n=int(input("주소록의 개수를 입력하세요 :"))

#(3) 입력 받은 이름 중에 영어 대문자, 숫자가 아닌 요소가 있으면 다시 입력해야 합니다.
def secure_ord(a):
    for j in range(len(a)):
        while not ((ord(a[j])>47 and ord(a[j])<58) or (ord(a[j])>64 and ord(a[j])<91)):
            name.remove(a)
            a=input("이름 다시 입력하세요 :")
            name.append(a)

def alp_sort(alp):
    leng=len(alp)-1
    for i in range(leng):
        for j in range(leng-i):
            if alp[j]>alp[j+1]:
                alp[j],alp[j+1]=alp[j+1],alp[j]
    for i in range(leng+1):
        new=chr(alp[i])
        alp.remove(alp[i])
        alp.insert(i,new)
    return alp

def num_sort(num):
    leng=len(num)-1
    for i in range(leng):
        for j in range(leng-i):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return num

#(5) 이름 내부에서 오름차순으로 대문자 먼저 정렬하고 숫자는 그 다음에 정렬됩니다. (ex. D9V3FF → DFFV39)
def a_sort(a):
    alp=[]
    num=[]
    global after
    for i in range(len(a)):
        if ord(a[i])>=65 and ord(a[i])<=90:
            alp.append(ord(a[i]))
        else:
            num.append(a[i])
    alp_sort(alp)
    num_sort(num)
    after=alp+num

name=[]
a=[]
finish=[]
address=''
#(2) N개만큼 이름을 입력합니다. 이름은 영어 대문자 또는 숫자로만 이루어져 있으며, 띄어쓰기는 없습니다. (ex. 3892EWV, D9V3FF, 0192, QAB 등)
for i in range(n):
    a=input("이름을 입력하세요 :")
    name.append(a)
    secure_ord(a)
    a=name[-1]
    a_sort(a)
    for j in after:
        address=address+j
    finish.append(address)
    address=''

#(4) 초기 주소록을 출력합니다.
print("초기 주소록 :",name)

#(6) 이름이 정렬된 주소록을 출력합니다.
print("정렬된 주소록 :",finish)





        


    
    
