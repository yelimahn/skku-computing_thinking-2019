#level test 1번_안예림
'''
perfect=[6,28,496,8128]
    
num=int(input("Please input the number:"))

if num<6:
    print("There is no result.")
elif num>=6 and num<28:
    print("The result is ", perfect[0])
elif num>=28 and num<496:
    print("The result is ", perfect[0], perfect[1])
elif num>=496 and num<8128:
    print("The result is ", perfect[0], perfect[1], perfect[2])
elif num>=8128:
    print("The result is ", perfect[0], perfect[1], perfect[2], perfect[3])
'''
#답

def perfect_number(n):

    results_list=[]

    while n!=1:
        n_counter=n-1
        results=0

        while n_counter !=0:
            if n%n_counter==0:
                results=results+n_counter
            n_counter=n_counter-1

        if n==results:
            results_list.append(n)

        n=n-1

    results_list.sort()
    return results_list

n=int(input("Please input the number :"))
results=perfect_number(n)
print("The result is", results)



