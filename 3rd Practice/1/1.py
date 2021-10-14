#3rd Practice_1_안예림

#철근 높이의 합은 항상 N 이상이기 때문에, 소정이에게 철근이 모자라지 않는다. 높이는 모두 자연수이다.
def length_n(n):
    global hap
    global c
    global t
    hap=0
    for i in range(c):
        leng=int(input("%d 번째 철근의 높이:" %(i+1)))
        if leng<=0:
            print("높이는 자연수, 다시 입력")
            leng=int(input("%d 번째 철근의 높이:" %(i+1)))
        t.append(leng)
        hap+=leng
    while not hap>=n:
        print("다시 입력하세요")
        del t[:]
        length_n(n)
    return t

#철근의 높이 내림차순 정렬
def ssort(t):
    tt=[]
    while t !=[]:
        biggest=max(t)
        t.remove(biggest)
        tt.append(biggest)
    return tt


#커터의 높이의 최댓값 찾기(이진탐색)
def find_cut(cut,mid,mid_index):
    global t
    global n
    global c
    rebar=0
    for i in range(c):
        if t[i]>mid:
            rebar=rebar+(t[i]-mid)
        else:
            break
    if rebar==n:
        return mid
    elif rebar>n:
        if len(cut)==1:
            return mid
        else:
            return cut_binary(cut[mid_index:])
    else:
        if len(cut)==1:
            return mid
        else:
            return cut_binary(cut[:mid_index])


#커터의 높이 최댓값 찾기(이진탐색)
def cut_binary(cut):
    mid_index=len(cut)//2
    mid=cut[len(cut)//2]
    result=find_cut(cut,mid,mid_index)
    return result


#철근의 수 C와 소정이가 가져가려고 하는 철근의 길이 N을 입력 받는다.
c=int(input("철근의 수:"))
n=int(input("철근의 길이:"))

#제대로 입력했는지 확인
t=[]
t=length_n(n)
#내림차순 정렬
t=ssort(t)

#커터의 길이의 최댓값을 찾기 위해 커터의 길이가 될 수 있는 최솟값부터 
#철근 길이들의 합까지의 리스트를 만들고 이 중에 최댓값은 무엇일지 이진탐색으로 찾음
cut=[]
for i in range(hap):
    cut.append(i+1)

#적어도 N미터의 철근을 집에 가져가기 위해서 커터에 설정할 수 있는 높이의 최댓값을 출력한다.
cutting=cut_binary(cut)
print("최댓값은",cutting)



