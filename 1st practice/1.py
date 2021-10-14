#1st Practice_1_안예림

#하나, 둘, 셋의 가위바위보 입력
fir=input("하나. 가위바위보")
while not (fir=="가위"or fir=="바위"or fir=="보"):
    fir=input("하나. 가위바위보")

sec=input("둘. 가위바위보")
while not (sec=="가위"or sec=="바위"or sec=="보"):
    sec=input("둘. 가위바위보")

thi=input("셋. 가위바위보")
while not (thi=="가위"or thi=="바위"or thi=="보"):
    thi=input("셋. 가위바위보")

#셋 다 비길 경우 
if fir==sec and sec==thi:
    print("셋 다 비겼다!")
if fir!=sec and sec!=thi and fir!=thi:
    print("셋 다 비겼다!")

#그 이외의 경우
if fir=="가위":
    if sec=="가위":
        if thi=="바위":
            print("이긴 사람 : 셋 / 진 사람 : 하나, 둘")
        elif thi=="보":
            print("이긴 사람 : 하나, 둘 / 진 사람 : 셋")
    elif sec=="바위":
        if thi=="가위":
            print("이긴 사람 : 둘 / 진 사람 : 하나, 셋")
        elif thi=="바위":
            print("이긴 사람 : 둘, 셋 / 진 사람 : 하나")
    elif sec=="보":
        if thi=="가위":
            print("이긴 사람 : 하나, 셋 / 진 사람 : 둘")
        elif thi=="보":
            print("이긴 사람 : 하나 / 진 사람 : 둘, 셋")

if fir=="바위":
    if sec=="가위":
        if thi=="가위":
            print("이긴 사람 : 하나 / 진 사람 : 둘, 셋")
        elif thi=="바위":
            print("이긴 사람 : 하나, 셋 / 진 사람 : 둘")
    elif sec=="바위":
        if thi=="가위":
            print("이긴 사람 : 셋 / 진 사람 : 하나, 둘")
        elif thi=="보":
            print("이긴 사람 : 셋 / 진 사람 : 하나, 둘")
    elif sec=="보":
        if thi=="바위":
            print("이긴 사람 : 둘 / 진 사람 : 하나, 셋")
        elif thi=="보":
            print("이긴 사람 : 둘, 셋 / 진 사람 : 하나")

if fir=="보":
    if sec=="가위":
        if thi=="가위":
            print("이긴 사람 : 둘, 셋 / 진 사람 : 하나")
        elif thi=="보":
            print("이긴 사람 : 둘 / 진 사람 : 하나, 셋")
    elif sec=="바위":
        if thi=="바위":
            print("이긴 사람 : 하나 / 진 사람 : 둘, 셋")
        elif thi=="보":
            print("이긴 사람 : 하나, 셋 / 진 사람 : 둘")
    elif sec=="보":
        if thi=="가위":
            print("이긴 사람 : 셋 / 진 사람 : 하나, 둘")
        elif thi=="바위":
            print("이긴 사람 : 하나, 둘 / 진 사람 :셋") 

