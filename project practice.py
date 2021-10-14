
#Final Project 안예림

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import time


#제목 / 저자 / 평점 / 네티즌 리뷰 수
#(추가) 책 페이지 수 / 책 정보(소개글) / 저자소개 / 목차

a=urlopen("http://www.yes24.com/24/Category/BestSeller")
soup=BeautifulSoup(a.read(),"html.parser")

tr_list = soup.select('ol > li')
temp_list=[]

for tr in tr_list :
    copy = tr.find('p',{'class':'copy'}).find('a').text
    title = tr.find_all('p')[2].text.strip('[도서]')
    auth = tr.find('p',{'class':'aupu'}).find_all('a')[0].text
    review = tr.find_all('p')[5].text.strip('회원리뷰 (').strip(')').strip()
    price = tr.find('p',{'class':'price'}).text

    

    temp_list.append([copy,title,auth,review,price])

for item in temp_list:
  print(item)
