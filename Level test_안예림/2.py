#level test 2번_안예림
'''
def bubble_sort(originlist):
    for i in range(0,9):
        for j in range(0,9-i):
            if originlist[j]>originlist[j+1]:
                originlist[j],originlist[j+1]=originlist[j+1],originlist[j]
    print(originlist)

import random
originlist=random.sample(range(100),10)
print(originlist)
afterlist=bubble_sort(originlist)
print(afterlist)
'''

#답

def bubble_sort(olist):
    total_length = len(olist)-1

    for i in range(total_length):
        for j in range(total_length - i):
            if olist[j+1] < olist[j]:
                olist[j],olist[j+1]=olist[j+1],olist[j]

    return olist

import random
originlist=random.sample(range(100),10)
print(originlist)
afterlist=bubble_sort(originlist)
print(afterlist)
            
        
