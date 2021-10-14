#컴퓨팅 사고 및 응용 Final Project
#인공지능융합 2019313464 안예림
#대상 웹페이지 : YES24 베스트셀러 페이지
#http://www.yes24.com/24/Category/BestSeller


#필요한 모듈 추가
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import time


#대상 웹 페이지 크롤링 하는 함수
def book_crawl(total):
  #내용을 넣을 리스트
  temp_list = []
  #항목 지정
  temp_list.append(['순위','제목','부제목','저자','평점','리뷰 수','가격','책 소개'])
  #main함수에서 입력받은 웹페이지에서 list를 만들기 위해 select 함수 사용
  link_list = total.select('ol > li')

  rank = 1 #베스트 셀러 순위

  #link_list 리스트에서 하나씩 꺼내 link에 지정
  for link in link_list:
    #직접 특정 책의 페이지에 다시 들어가야 하므로 url변수에 url 주소 저장
    url = "http://www.yes24.com"
    url += link.find('p',{'class':'copy'}).find('a').attrs["href"]
    #특정 책의 페이지에 들어감
    html = urlopen(url)
    soup = BeautifulSoup(html.read(),"html.parser")

    #탐색 시간을 줄이기 위해 범위 지정
    yes = soup.find('body').find('div',{'id':'yesWrap'})

    #책의 제목
    title = yes.find('div',{'class':'gd_titArea'}).find('h2',{'class':'gd_name'}).text

    #책의 부제목
    subtitle = yes.find('div',{'class':'gd_titArea'}).find('h3',{'class':'gd_nameE'})
    if subtitle!=None: #부제목이 있는 경우
      subtitle = subtitle.text #text로 보여줌
    else: #부제목이 없는 경우
      subtitle = '' #None보다 보기 좋은 ''로 지정

    #저자
    author=''
    #저자가 여러명일 때를 대비해 for문으로 하나씩 꺼내어 temp변수에 넣음
    for i in yes.find('span',{'class':'gd_pubArea'}).find('span',{'class':'gd_auth'}).find_all('a'):
      temp = i.text.strip()
      if temp == '정보 더 보기/감추기': #저자만 넣어야 하므로
        break #그 뒤 정보는 넣지 않음
      else: 
        if author=='': #첫 번째 저자인 경우
          author += temp
        else: #그 외의 경우
          author += ',' + temp #콤마를 함께 넣어줌

    #평점
    score = yes.find('span',{'class':'gd_ratingArea'}).find_all('a')[0].text.strip('리뷰 총점')
    if score=='첫번째 구매리뷰를 남겨주세요.': #평점이 없는 경우
      score = '0.0'

    #회원 리뷰 수
    review = yes.find('span',{'class':'gd_reviewCount'}).find('a').text.strip('회원리뷰(건)')
    if review =='첫번째 구매리뷰를 남겨주세요.': #리뷰가 없는 경우
      review = '0'

    #책의 가격
    price = yes.find('div',{'class':'gd_infoTb'}).find('tr',{'class':'accentRow'}).find('span',{'class':'nor_price'}).text

    #책 소개
    intro = yes.find('div',{'class':'gd_dContLft'}).find('div',{'class':'infoWrap_txtInner'}).find('textarea').text.strip().replace('\n','').replace('\r','')

    #이 모든 것들을 temp_list에 append
    temp_list.append([rank,title,subtitle,author,score,review,price,intro])
    
    #순위를 하나씩 늘려줌
    rank +=1

  #모든 링크를 다 돌고 나서 temp_list 리턴, 함수 밖에서 book_list가 받음
  return temp_list


#이 리스트를 csv파일로 만들어 줍니다
def make_csv(book_list, csv_title):
  #file 변수에서 csv파일 오픈
  file = open(csv_title, 'w', newline='')
  csvfile = csv.writer(file)
  #book_list에서 줄 별로 읽어서 csv파일에 저장
  for row in book_list :
    csvfile.writerow(row)
  #파일 닫기
  file.close()


#사용자가 보는 메인 함수
def main():
  
  #사용자에게 웹페이지 주소 입력 받음
  website=input("웹사이트 주소: ")
  
  #시작 시간을 변수에 넣어줌 start는 정수,  start_time는 문자열로 따로 지정함
  start=time.time()
  start_time=time.strftime("시작시간: %Y년 %m월 %d일 %H시 %M분 %S초",time.localtime(time.time()))
  
  #a=urlopen("http://www.yes24.com/24/Category/BestSeller")
  a=urlopen(website)
  #beautifulsoup을 total변수에서 지정
  total=BeautifulSoup(a.read(),"html.parser")

  #csv 파일 제목을 만들어 줌
  csv_title=time.strftime("%Y%m%d%H%M.csv", time.localtime(time.time()))
  #book_crawl함수의 리턴 값을 book_list에 저장
  book_list=book_crawl(total)

  #csv만들기 함수 연결(내용물이 들어있는 book_list와 csv파일 제목을 넣어줌)
  make_csv(book_list,csv_title)

  #종료시간 측정, 마찬가지로 end와 end_time 따로 지정
  end=time.time()
  end_time=time.strftime("종료시간: %Y년 %m월 %d일 %H시 %M분 %S초",time.localtime(time.time()))

  #종료되었으니 사용자에게 보여줌
  print("'%s' 파일에 크롤링 결과가 저장되었습니다." %csv_title)
  print("소요시간: %d초" %(end-start+0.5)) #float를 int로 바꾸어서 오차가 생기므로 오차를 줄이기 위해
  print(start_time)
  print(end_time)

  #계속할 건지 사용자에게 물어봄
  again=input("계속하시겠습니까? (네/아니오)")
  #네/아니오 이외는 다시 입력받음
  while not (again=='네' or again=='아니오'): 
    again=input("계속하시겠습니까? (네/아니오)")
  if again=='아니오':
    print("안녕히 가십시오")
    return None #종료
  #'네'일 경우 다시 main함수 실행
  main()


#메인 함수 실행
main()
