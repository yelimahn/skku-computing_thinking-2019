#level test 4번_안예림
'''
def student_grading(grade_result):
    for i in range(20):
        if grade_result[i]>=95:
            grade='A+'
        elif grade_result[i]>=90:
            grade='A'
        elif grade_result[i]>=85:
            grade='B+'
        elif grade_result[i]>=80:
            grade='B'
        elif grade_result[i]>=75:
            grade='C+'
        else:
            grade='C'
'''

def student_grading(grade_result):
    i=0
    while i<20:
        if grade_result[i]>=95:
            grade_result[i]='A+'
        elif grade_result[i]>=90:
            grade_result[i]='A'
        elif grade_result[i]>=85:
            grade_result[i]='B+'
        elif grade_result[i]>=80:
            grade_result[i]='B'
        elif grade_result[i]>=75:
            grade_result[i]='C+'
        else:
            grade_result[i]='C'

        i=i+1

    ap_count=grade_result.count('A+')
    a_count=grade_result.count('A')
    bp_count=grade_result.count('B+')
    b_count=grade_result.count('B')
    cp_count=grade_result.count('C+')
    c_count=grade_result.count('C')

    print("A+ :", ap_count)
    print("A :", a_count)
    print("B+ :", bp_count)
    print("B :", b_count)
    print("C+ :", cp_count)
    print("C :", c_count)

    class_sum=(ap_count * 4.5)+(a_count * 4)+(bp_count * 3.5)+(b_count *3)+(cp_count *2.5)+(c_count * 2)
    class_average=class_sum/(ap_count + a_count+bp_count+b_count+cp_count+c_count
                             
import random
grade_result=[]
grade_result=random.sample(range(70,101),20)
student_grading(grade_result)
