#1st Practice_2_안예림

print("끝말잇기 시작")
print()

def word_input():
    first=input("word input : ")
    next=input("next word : ")
    compare(first, next)
    
def compare(origin,after):
    if origin[-1]!=after[0]:
        print("실패")
        return 0
    else:
        print("다음")
        origin=after
        after=input("next word gogo: ")
        compare(origin, after)

word_input()



