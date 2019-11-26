import urllib.request
from bs4 import BeautifulSoup
import re
import ssl
import datetime

context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context

# 클리닝 함수
def clean_text(text):
    text = text.replace("\n", "")
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', cleaned_text)
    return cleaned_text

# 시작날짜 설정
#URL = 'http://media.daum.net/ranking/popular?include=society,politics,culture,economic,foreign,digital&regDate=201807'
mainURL = 'http://media.daum.net/ranking/popular?'
popular = ['society']
myDatetimeStr = '20191001'
myDatetime = datetime.datetime.strptime(myDatetimeStr, '%Y%m%d')
data = []
for i in range(1,365):
    i+=1
    for j in popular:
        URL = mainURL+'&include='+j+'&regDate='+myDatetime.strftime('%Y%m%d')
        print(URL)

        source_code_from_URL = urllib.request.urlopen(URL, context=context)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
        list_news = soup.find('ul', attrs={'class':'list_news2'})
        list_news_li = list_news.find_all('li')
        #기사 썸네일 리스트
        for item in list_news_li:
            link_txt = item.find('a', attrs={'class':'link_txt'})
            subject = clean_text(link_txt.find(text=True))
            #print(subject)

            link_thumb = item.find('a', attrs={'class':'link_thumb'})
            if link_thumb != None:
                linkUrl = link_thumb['href']
                #print(linkUrl)
                source_code_from_URL = urllib.request.urlopen(linkUrl, context=context)
                soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
                article_view = soup.find('div', attrs={'class':'article_view'})
                article_view_text = article_view.find_all(text=True)
               #print(article_view_text)
                article_view_text_plain = ''
                for i in article_view_text:
                    article_view_text_plain += clean_text(i)
                data.append([myDatetime.strftime('%Y%m%d'), j, subject, article_view_text_plain])
    nextDate =  myDatetime + datetime.timedelta(days=1)
    if nextDate.strftime('%d') == '01':
        with open(myDatetime.strftime('%Y%m')+'article.csv', 'w', encoding='UTF8') as file:    # article.csv 파일을 쓰기 모드로 열기
            file.write('date,popular,subject,article\n')                  # 컬럼 이름 추가
            for k in data:                                              # data를 반복하면서
                file.write('{0},{1},{2},{3}\n'.format(k[0], k[1], k[2], k[3]))
        del data[:]
    myDatetime += datetime.timedelta(days=1)
