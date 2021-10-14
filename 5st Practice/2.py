#5th Practice_2_안예림

import sys
    
class decision:
    tnumbers=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    def __init__(self,name,tnumber,coin):
        self.__name=name
        self.__tnumber=tnumber
        self.__coin=5
        self.__count=0

    def coin(self):
        return self.__coin

    def count(self):
        self.__count+=1
        return self.__count
        
    def results(self):
        if self.__count==3:
            print("1등 당첨! 5점 획득")
            self.__coin+=5
        elif self.__count==2:
            print("2등 당첨! 3점 획득")
            self.__coin+=3
        else:
            print("당첨 실패! 1점 감점")
            self.__coin-=1
        return self.__coin

class Reader:
    @staticmethod
    def get_name():
        return input("이름을 입력하세요 :")

    @staticmethod
    def ox(message):
        response=input(message).lower()
        while not (response=='o' or response=='x'):
            response=input(message).lower()
        return response=='o'

    @staticmethod
    def input_number():
        print("\n1에서 15 사이 정수 3개를 고르시오 : ")
        num=[]
        for i in range(3):
            number=int(input("%d번째 숫자 : " %(i+1)))
            num.append(number)
        print("\n당신이 추측한 로또 번호는 ",num,"입니다.")
        return num



class lottocontroller:
    def __init__(self,name):
        tnumber=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
        coin=5
        self.__player=decision.__init__(self,name,tnumber,coin)
        self.__lotto=get_number.get_number_selection()
    
    def play(self):
        print("\n=====new game=====\n")
        num=Reader.input_number()
        lotto=get_number.get_number_selection()
        player=self.__player
        for i in range(3):
            for j in range(3):
                if num[j]==lotto[i]:
                    decision.count(self)
        coin=decision.results(self)
        print("\n 실제 로또 번호 : ",lotto)
        if coin>=1:
            return 0
        else:
            print("GAME OVER")
            input()
            sys.exit()
                    

class get_number:
        
    def get_number_selection():
        import random
        lotto=random.sample(decision.tnumbers,3)
        return lotto

def main():
    print("Welcome to lotto game\n")
    name=Reader.get_name()
    game=lottocontroller(name)
    while True:
        game.play()
        if not Reader.ox("Play more, "+name+"? (o/x) "):
            break
    print("Bye, "+name+"!")

main()
