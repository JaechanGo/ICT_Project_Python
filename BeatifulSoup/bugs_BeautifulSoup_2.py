#-*-coding:utf8*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()
f=open('bugschart1.txt','wt', encoding='utf-8') #파일 쓸 준비
search_day = input("순위 검색할 날짜를 8자리로 입력하세요!!(ex : 20060922~20170702 사이 입력) => ")
url=urlopen("http://music.bugs.co.kr/chart/track/day/total?chartdate=" + search_day, context=context)
soup=BeautifulSoup(url.read(), "html.parser", from_encoding="utf8")
artists=[] #이 날 1위~100위에 등록된 가수들 목록
artistRank=0
titles=[] #이 날 1위~100위에 등록된 제목 목록
titleRank=0
try:
    for link1 in soup.find_all(name="p",attrs={"class":"artist"}):
        try:
            artist=link1.find('a').text
            artists.append(artist)
            artistRank += 1
        except AttributeError as artistError: #가수데이터가 존재하지 않을 경우 a태그가 없음(중간에 간혹 순위가 빠진 경우가 있음).
            artist='N/A'
            artists.append(artist)
            artistRank += 1
    
    for link2 in soup.find_all(name="p",attrs={"class":"title"}):
        try:
            title=link2.find('a').text
            titles.append(title)
            titleRank+=1
            
        except AttributeError as titleError: #곡 데이터가 존재하지 않을 경우 a태그가 없음.
            title='N/A'
            titles.append(title)
            titleRank+=1
            
    for i in range(0,100):
        f.write(str(search_day)+','+str(i+1)+','+str(artists[i])+','+str(titles[i])+'\n')
                
except AttributeError as e: #p태그 자체가 존재하지 않을 경우, 데이터 없는것으로 여기고 다음 루프로 넘어가게 한다.
    print(search_day+"이 날 데이터가 존재하지 않습니다.")
except IndexError as index: #웹페이지 자체 에러로 Top100 곡 갯수가 100개가 안되면 인덱스에러로 표시한다.
    print('인덱스 에러 / '+'아티스트 리스트 길이 : '+str(len(artists))+'/ 곡 리스트 길이 : '+str(len(titles)))
        
f.close()