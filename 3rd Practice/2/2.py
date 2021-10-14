#3rd Practice_2_안예림

import random
import string

def string_lower(stir,find):
    while True:
        for i in range(len(stir)):
            if stri[i]==find:
                return True
        return False

#(1) 자연수 N을 입력 받습니다.
n=int(input("문자열 몇 개 :"))
while not n>=0:
    n=int(input("문자열 몇 개 :"))
print()

#(2) N개만큼의 문자열을 랜덤으로 생성하여 새로운 txt 파일에 씁니다.
t=open("test.txt","w")

#- 모두 영어 소문자로 되어 있음. (대문자, 띄어쓰기, 특수문자 없음.)
stri=string.ascii_lowercase
result=''

#- 1~30자 사이 랜덤 길이
for i in range(n):
    num=random.randrange(1,31)
    for j in range(num):
        result+=random.choice(stri)
    #- 각 문자열 앞에는 1번부터 순번이 붙어 나오며, 엔터로 구분됩니다.
    t.write("%d: %s\n" %(i+1,result))
    result=''
    
t=open("test.txt","r")
test=t.readlines()

#(3) 찾고 싶은 문자를 입력합니다. 문자는 a부터 z까지 영어 소문자 중 하나입니다.
find_str=input("찾을 문자를 입력하세요:")
while not string_lower(stri,find_str):
    find_str=input("찾을 문자를 입력하세요:")

print()
#(4) 2번에서 만든 txt파일을 열고, 각 문자열에서 찾고 싶은 문자가
#가장 처음 나오는 위치를 알려줍니다.
#(가장 처음에 나올 경우 1번째입니다.) 없을 경우 없다고 알려줍니다.
for x in range(n):
    sentence=test[x]
    order=sentence.find(find_str)
    if order==-1:
        print("%d: 문자열 내에 없습니다." %(x+1))
    else:
        if x<10:
            print("%d: %d번째에서 처음으로 발견" %(x+1,order-2))
        else:
            print("%d: %d번째에서 처음으로 발견" %(x+1,order-3))

t.close()

