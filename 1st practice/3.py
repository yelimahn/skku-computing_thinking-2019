#1st Practice_3_안예림

num=int(input("10진수 수 입력 :"))
list=[]

def binary(decimal):
    if decimal==0:
        list.reverse()
        return list
    else:
        remain=decimal%2
        list.append(remain)
        binary(decimal//2)

binary(num)

print("\n10진수 %d은" %num)
print("2진수")
for i in list:
    print(i, end="")
print("입니다.")
