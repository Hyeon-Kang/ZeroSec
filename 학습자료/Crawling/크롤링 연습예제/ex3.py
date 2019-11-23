#-*- coding : utf-8
import requests
from bs4 import BeautifulSoup

#Text를 html에 저장합니다.
html = requests.get("http://www.naver.com").text
#BeautifulSoup을 이용해 html을 read합니다.
soup = BeautifulSoup(html, 'html.parser')

#가져오고 싶은 Text 부분을 선택해서 가져옵니다.
#실시간 검색어는 이 부분에 있기 때문에 가져온 Data를 for문으로 출력 해 줍니다.
keywords = soup.select('.ah_roll_area .ah_k')

for i, keyword in enumerate(keywords, 1):
    print("{}위 {}".format(i,keyword.get_text()))
