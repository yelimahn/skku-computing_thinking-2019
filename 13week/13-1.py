#13week_1_안예림

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

a=urlopen("http://www.op.gg/summoner/champions/userName=Hide%20on%20bush")
soup=BeautifulSoup(a.read(),"html.parser")

#기준 정리 ex. 챔피언, 게임 등
def setting(soup):
  temp_list=[]
  head_list = soup.select('thead > tr')

  for head in head_list :
    rank = head.find('th',{'class':'Rank HeaderCell'}).text
    name = head.find('th',{'class':'Champion HeaderCell'}).text
    game = head.find('th',{'class':'RatioGraph HeaderCell'}).text
    
    gold = head.find('th',{'class':'Gold HeaderCell'}).text
    cs = head.find('th',{'class':'CS HeaderCell'}).text
    max_kill = head.find('th',{'class':'MaxKill HeaderCell'}).text
    max_death = head.find('th',{'class':'MaxDeath HeaderCell'}).text
    give_dam = head.find_all('th',{'class':'Gold HeaderCell'})[1].text
    get_dam = head.find_all('th',{'class':'Gold HeaderCell'})[2].text
    double_k = head.find_all('th',{'class':'Gold HeaderCell'})[3].text
    triple_k = head.find_all('th',{'class':'Gold HeaderCell'})[4].text
    quad_k = head.find_all('th',{'class':'Gold HeaderCell'})[5].text
    penta_k = head.find_all('th',{'class':'Gold HeaderCell'})[6].text

    temp_list.append([rank, name, game, gold, cs, max_kill, max_death, give_dam, get_dam, double_k, triple_k, quad_k, penta_k])

  return hob_Crawl(temp_list,soup)

#내용물을 list에 append시켜줍니다
def hob_Crawl(temp_list,soup):
  tr_list = soup.select('tbody > tr')

  for tr in tr_list :
      rank = tr.find('td',{'class':'Rank Cell'}).text
      name = tr.find('td',{'class':'ChampionName Cell'}).find('a').text
      game = tr.find('td',{'class':'RatioGraph Cell'}).find('span',{'class':'WinRatio'}).text
      '''
      kill = tr.find('td',{'class':'KDA'}).find('span',{'class':'Kill'}).text.strip()
      death = tr.find('td',{'class':'KDA'}).find('span',{'class':'Death'}).text.strip()
      assist = tr.find('td',{'class':'KDA'}).find('span',{'class':'Assist'}).text.strip()
      '''
      gold = tr.find('td',{'class':'Value Cell'}).text.strip()
      cs = tr.find_all('td',{'class':'Value Cell'})[1].text.strip()
      max_kill = tr.find_all('td',{'class':'Value Cell'})[2].text.strip()
      max_death = tr.find_all('td',{'class':'Value Cell'})[3].text.strip()
      give_dam = tr.find_all('td',{'class':'Value Cell'})[4].text.strip()
      get_dam = tr.find_all('td',{'class':'Value Cell'})[5].text.strip()
      double_k = tr.find_all('td',{'class':'Value Cell'})[6].text.strip()
      triple_k = tr.find_all('td',{'class':'Value Cell'})[7].text.strip()
      quad_k = tr.find_all('td',{'class':'Value Cell'})[8].text.strip()
      penta_k = tr.find_all('td',{'class':'Value Cell'})[9].text.strip()

      temp_list.append([rank, name, game, gold, cs, max_kill, max_death, give_dam, get_dam, double_k, triple_k, quad_k, penta_k])

  return temp_list

#이 리스트를 csv파일로 만들어 줍니다
def make_csv(hob_list):
    file = open('Hide on bush.csv', 'w', newline='')
    csvfile = csv.writer(file)
    for row in hob_list :
        csvfile.writerow(row)
    file.close()

#리스트로 정리 실행
hob_list=setting(soup)
'''
for item in hob_list:
  print(item)
'''
#csv 파일로 만들기 실행
make_csv(hob_list)
