#!/usr/bin/pyhton

print('년도를 입력하세요. ex) 2019')
yyy = input()
print('시작 월을 입력하세요. ex) 03')
mmm = input()

filename_ = str(yyy)+str(mmm)+'article.csv'
print(filename_)

# 1. csv file 불러오기 ========================================================
import pandas as pd

try :
    csv_data = pd.read_csv(filename_, delimiter=',', encoding='UTF-8')
except:
    print(filename_+' 열기 실패')
    exit(1)


# 추출한 지명 리스트 로드 ====================================================

# 강원도 지명 리스트 준비
KW=[]
file=open('강원도list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        KW.append(line[0:escape])
    else:
        break
file.close()

KW = KW[0].split(' ')
KW.remove('')
print(KW)

# 경기도 지명 리스트 준비
GGD=[]
file=open('경기도list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        GGD.append(line[0:escape])
    else:
        break
file.close()

GGD = GGD[0].split(' ')
GGD.remove('')
print(GGD)

# 경상남도 지명 리스트 준비
GSND=[]
file=open('경상남도list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        GSND.append(line[0:escape])
    else:
        break
file.close()

GSND = GSND[0].split(' ')
GSND.remove('')
print(GSND)


# 경상북도 지명 리스트 준비
GSBD=[]
file=open('경상북도list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        GSBD.append(line[0:escape])
    else:
        break
file.close()

GSBD = GSBD[0].split(' ')
GSBD.remove('')
print(GSBD)


# 광주광역시 지명 리스트 준비
GJ=[]
file=open('광주광역시list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        GJ.append(line[0:escape])
    else:
        break
file.close()

GJ = GJ[0].split(' ')
GJ.remove('')
print(GJ)


# 대구광역시 지명 리스트 준비
DG=[]
file=open('대구광역시list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        DG.append(line[0:escape])
    else:
        break
file.close()

DG = DG[0].split(' ')
DG.remove('')
print(DG)


# 대전광역시 지명 리스트 준비
DJ=[]
file=open('대전광역시list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        DJ.append(line[0:escape])
    else:
        break
file.close()

DJ = DJ[0].split(' ')
DJ.remove('')
print(DJ)

# 부산광역시 지명 리스트 준비
BS=[]
file=open('부산광역시list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        BS.append(line[0:escape])
    else:
        break
file.close()

BS = BS[0].split(' ')
BS.remove('')
print(BS)



# 서울특별시 지명 리스트 준비
SO=[]
file=open('서울특별시list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        SO.append(line[0:escape])
    else:
        break
file.close()

SO = SO[0].split(' ')
SO.remove('')
print(SO)

# 세종특별자치시 지명 리스트 준비
SJ=[]
file=open('세종특별자치시list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        SJ.append(line[0:escape])
    else:
        break
file.close()

SJ = SJ[0].split(' ')
SJ.remove('')
print(SJ)

# 울산광역시 지명 리스트 준비
US=[]
file=open('울산광역시list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        US.append(line[0:escape])
    else:
        break
file.close()

US = US[0].split(' ')
US.remove('')
print(US)


# 인천광역시 지명 리스트 준비
IC=[]
file=open('인천광역시list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        IC.append(line[0:escape])
    else:
        break
file.close()

IC = IC[0].split(' ')
IC.remove('')
print(IC)

# 전라남도지명 리스트 준비
JND=[]
file=open('전라남도list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        JND.append(line[0:escape])
    else:
        break
file.close()

JND = JND[0].split(' ')
JND.remove('')
print(JND)


# 전라북도지명 리스트 준비
JBD=[]
file=open('전라북도list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        JBD.append(line[0:escape])
    else:
        break
file.close()

JBD = JBD[0].split(' ')
JBD.remove('')
print(JBD)

# 충청북도지명 리스트 준비
CB=[]
file=open('충청북도list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        CB.append(line[0:escape])
    else:
        break
file.close()

CB = CB[0].split(' ')
CB.remove('')
print(CB)



# 충청남도지명 리스트 준비
CN=[]
file=open('충청남도list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        CN.append(line[0:escape])
    else:
        break
file.close()

CN = CN[0].split(' ')
CN.remove('')
print(CN)

# 제주특별자치도지명 리스트 준비
JJ=[]
file=open('제주특별자치도list.txt','rt' , encoding='UTF-8')

while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        JJ.append(line[0:escape])
    else:
        break
file.close()

JJ = JJ[0].split(' ')
JJ.remove('')
print(JJ)


# 2. article 컬럼만 추출(원본), sentence(특수문자, stop word 적용) ===========================
article_list = csv_data.article



# 3_1. 특수문자 제거 ======================================================================

# 소문자 변환
# re 라이브러리로 특수문자 제거

# 읽어온 데이터 확인 (json_body)

sentence = []

# 특수문자 제거 라이브러리
import re
for a in range(len(article_list)):
    sentence.append(article_list[a].strip())

for i in range(len(sentence)):
    sentence[i] = sentence[i].lower() # lower() : 모든 문자를 소문자로 변환
    sentence[i] = re.sub("(<br\s*/><br\s*/>)|(\-)|(\/)", ' ', sentence[i]) # 특수문자 제거
    sentence[i] = re.sub("[.;:!\'?,\"()|[\]]", ' ', sentence[i]) # 특수문자 제거



# 3_2. 외부 Stop Word 리스트 불러오기 (stop word ranking 기반) ==============================
# 불용어 처리 - stop_word 리스트 불러오기 & 전처리
stop_words = []
f = open("stop_word.txt", 'r', encoding='UTF-8') # 경로 편집
while True:
    line = f.readline()
    if not line: break
    #print(line) #정상 출력 확인
    stop_words.append(line.rstrip('\n')) # 개행문자 제거 후 추가
f.close()



# 3_3. 불러온 Stop Word 적용   =========================================================
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

result = []
for w in sentence:
    if w not in stop_words:
        result.append(w)


# 연산 절약을 위해 키워드를 통한 필터링 ===============================================
keyw = ['아프리카', '돼지', '야생', '방역', '멧돼지', '발생']
w_list0 = []
w_list1 = []
w_list2 = []
w_list3 = []
w_list4 = []
w_list5 = []
w_list6 = []
w_list7 = []
w_list8 = []

# 아프리카
for i in range(len(sentence)):
    if( sentence[i].find(keyw[0]) >= 0 ):
        w_list0.append(i)
# 돼지
for i in range(len(sentence)):
    if( sentence[i].find(keyw[1]) >= 0 ):
        w_list1.append(i)
# 야생
for i in range(len(sentence)):
    if( sentence[i].find(keyw[2]) >= 0 ):
        w_list2.append(i)
# 방역
for i in range(len(sentence)):
    if( sentence[i].find(keyw[3]) >= 0 ):
        w_list3.append(i)
# 멧돼지
for i in range(len(sentence)):
    if( sentence[i].find(keyw[4]) >= 0 ):
        w_list4.append(i)
# 발생
for i in range(len(sentence)):
    if( sentence[i].find(keyw[5]) >= 0 ):
        w_list5.append(i)


# 아프리카 + 돼지
u_list = list(set(w_list0).intersection(w_list1))








f_article = []    # 선별한 인덱스의 article만 뽑아서 f_article = mydoclist 에 저장 =======
for numm in u_list:
    f_article.append(sentence[numm])
    #print(sentence[numm])
    #print()

# 추출한 명사를 리스트로 만들기
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Kkma, Twitter, Hannanum, Komoran
from konlpy.utils import pprint

mydoclist = f_article

# twitter 와 komoran이 가장 높은 유사도를 보인다.
#kkma = Kkma()
#twitt = Twitter()
#hann = Hannanum()
komo = Komoran()

doc_nouns_list = []

for doc in mydoclist:
    nouns = komo.nouns(doc)
    doc_nouns = ''

    for noun in nouns:
        doc_nouns += noun + ' ' # 추출한 명사를 문장으로 합침

    doc_nouns_list.append(doc_nouns) # doc_nouns_list에 추가



#참조 : https://bab2min.tistory.com/570 ====================================================
#!pip install networkx
import networkx
import re

class RawSentence:
    def __init__(self, textIter):
        if type(textIter) == str: self.textIter = textIter.split('\n')
        else: self.textIter = textIter
        self.rgxSplitter = re.compile('([.!?:](?:["\']|(?![0-9])))')

    def __iter__(self):
        for line in self.textIter:
            ch = self.rgxSplitter.split(line)
            for s in map(lambda a, b: a + b, ch[::2], ch[1::2]):
                if not s: continue
                yield s

class RawSentenceReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.rgxSplitter = re.compile('([.!?:](?:["\']|(?![0-9])))')

    def __iter__(self):
        for line in open(self.filepath, encoding='utf-8'):
            ch = self.rgxSplitter.split(line)
            for s in map(lambda a, b: a + b, ch[::2], ch[1::2]):
                if not s: continue
                yield s

class RawTagger:
    def __init__(self, textIter, tagger = None):
        if tagger:
            self.tagger = tagger
        else :
            from konlpy.tag import Komoran
            self.tagger = Komoran()
        if type(textIter) == str: self.textIter = textIter.split('\n')
        else: self.textIter = textIter
        self.rgxSplitter = re.compile('([.!?:](?:["\']|(?![0-9])))')

    def __iter__(self):
        for line in self.textIter:
            ch = self.rgxSplitter.split(line)
            if len(ch) == 1:
                ch.append(".")

            for s in map(lambda a,b:a+b, ch[::2], ch[1::2]):
                if not s: continue
                yield self.tagger.pos(s)

class RawTaggerReader:
    def __init__(self, filepath, tagger = None):
        if tagger:
            self.tagger = tagger
        else :
            from konlpy.tag import Komoran
            self.tagger = Komoran()
        self.filepath = filepath
        self.rgxSplitter = re.compile('([.!?:](?:["\']|(?![0-9])))')

    def __iter__(self):
        for line in open(self.filepath, encoding='utf-8'):
            ch = self.rgxSplitter.split(line)
            for s in map(lambda a,b:a+b, ch[::2], ch[1::2]):
                if not s: continue
                yield self.tagger.pos(s)

class TextRank:
    def __init__(self, **kargs):
        self.graph = None
        self.window = kargs.get('window', 5)
        self.coef = kargs.get('coef', 1.0)
        self.threshold = kargs.get('threshold', 0.005)
        self.dictCount = {}
        self.dictBiCount = {}
        self.dictNear = {}
        self.nTotal = 0


    def load(self, sentenceIter, wordFilter = None):
        def insertPair(a, b):
            if a > b: a, b = b, a
            elif a == b: return
            self.dictBiCount[a, b] = self.dictBiCount.get((a, b), 0) + 1

        def insertNearPair(a, b):
            self.dictNear[a, b] = self.dictNear.get((a, b), 0) + 1

        for sent in sentenceIter:
            for i, word in enumerate(sent):
                if wordFilter and not wordFilter(word): continue
                self.dictCount[word] = self.dictCount.get(word, 0) + 1
                self.nTotal += 1
                if i - 1 >= 0 and (not wordFilter or wordFilter(sent[i-1])): insertNearPair(sent[i-1], word)
                if i + 1 < len(sent) and (not wordFilter or wordFilter(sent[i+1])): insertNearPair(word, sent[i+1])
                for j in range(i+1, min(i+self.window+1, len(sent))):
                    if wordFilter and not wordFilter(sent[j]): continue
                    if sent[j] != word: insertPair(word, sent[j])

    def loadSents(self, sentenceIter, tokenizer = None):
        import math
        def similarity(a, b):
            n = len(a.intersection(b))
            return n / float(len(a) + len(b) - n) / (math.log(len(a)+1) * math.log(len(b)+1))

        if not tokenizer: rgxSplitter = re.compile('[\\s.,:;-?!()"\']+')
        sentSet = []
        for sent in filter(None, sentenceIter):
            if type(sent) == str:
                if tokenizer: s = set(filter(None, tokenizer(sent)))
                else: s = set(filter(None, rgxSplitter.split(sent)))
            else: s = set(sent)
            if len(s) < 2: continue
            self.dictCount[len(self.dictCount)] = sent
            sentSet.append(s)

        for i in range(len(self.dictCount)):
            for j in range(i+1, len(self.dictCount)):
                s = similarity(sentSet[i], sentSet[j])
                if s < self.threshold: continue
                self.dictBiCount[i, j] = s

    def getPMI(self, a, b):
        import math
        co = self.dictNear.get((a, b), 0)
        if not co: return None
        return math.log(float(co) * self.nTotal / self.dictCount[a] / self.dictCount[b])

    def getI(self, a):
        import math
        if a not in self.dictCount: return None
        return math.log(self.nTotal / self.dictCount[a])

    def build(self):
        self.graph = networkx.Graph()
        self.graph.add_nodes_from(self.dictCount.keys())
        for (a, b), n in self.dictBiCount.items():
            self.graph.add_edge(a, b, weight=n*self.coef + (1-self.coef))

    def rank(self):
        return networkx.pagerank(self.graph, weight='weight')

    def extract(self, ratio = 0.1):
        ranks = self.rank()
        cand = sorted(ranks, key=ranks.get, reverse=True)[:int(len(ranks) * ratio)]
        pairness = {}
        startOf = {}
        tuples = {}
        for k in cand:
            tuples[(k,)] = self.getI(k) * ranks[k]
            for l in cand:
                if k == l: continue
                pmi = self.getPMI(k, l)
                if pmi: pairness[k, l] = pmi

        for (k, l) in sorted(pairness, key=pairness.get, reverse=True):
            print(k[0], l[0], pairness[k, l])
            if k not in startOf: startOf[k] = (k, l)

        for (k, l), v in pairness.items():
            pmis = v
            rs = ranks[k] * ranks[l]
            path = (k, l)
            tuples[path] = pmis / (len(path) - 1) * rs ** (1 / len(path)) * len(path)
            last = l
            while last in startOf and len(path) < 7:
                if last in path: break
                pmis += pairness[startOf[last]]
                last = startOf[last][1]
                rs *= ranks[last]
                path += (last,)
                tuples[path] = pmis / (len(path) - 1) * rs ** (1 / len(path)) * len(path)

        used = set()
        both = {}
        for k in sorted(tuples, key=tuples.get, reverse=True):
            if used.intersection(set(k)): continue
            both[k] = tuples[k]
            for w in k: used.add(w)

        #for k in cand:
        #    if k not in used or True: both[k] = ranks[k] * self.getI(k)

        return both

        #0.333
    def summarize(self, ratio = 0.333):
        r = self.rank()
        ks = sorted(r, key=r.get, reverse=True)[:int(len(r)*ratio)]
        return ' '.join(map(lambda k:self.dictCount[k], sorted(ks)))



#=================############################################

top_key_list = []

for arti in doc_nouns_list:
    tr = TextRank(window=5, coef=1)
    print('Load...')
    stopword = set([('있', 'VV'), ('하', 'VV'), ('되', 'VV'), ('없', 'VV') ])
    tr.load(RawTagger(arti), lambda w: w not in stopword and (w[1] in ('NNG', 'NNP', 'VV', 'VA')))
    print('Build...')
    tr.build()
    kw = tr.extract(0.1)
    top_key = []
    for k in sorted(kw, key=kw.get, reverse=True):

        #print("%s\t%g" % (k, kw[k]))
        for kk in k:
            #print(kk[0])
            top_key += kk[0]
            #top_key += list(k[kk])
        top_key = ''.join(top_key)
        print("topkey : ", top_key)
    top_key_list.append(top_key)


#====================================================================================

local_name = []
local_list = ["경기", "강원", "광주", "경북", "경남", "대구", "대전", "부산", "서울", "세종", "울산", "인천", "전남", "전북", "제주", "충남", "충북" ]
local_result = []
# 지명 찾기
article_count = 0
art_count_list = []
for i in top_key_list:

    for j in local_list:
        #print(j)
        local_num = i.find(j) # 지명 스캔   #이제 원본 기사 불러와서 지명 찾기
        if local_num != -1 :
            print("기사 번호: ", article_count)
            art_count_list.append(article_count)
            print(i, " 지명 추출 : ", j)
            if j == '강원':
                print ("강원도 도시 비교")
            if j == '경기':
                for jj in GGD:
                    l_num = i.find(jj)

                    if l_num != -1:
                        print("도시 발견! : ", jj)
                        local_name.append(jj)



            #print(j)
            local_result.append(j)

    article_count +=1







# ===================================================================================



locale_list = [] # 원문 기사를 찾기 위한 반복변수
result_loc = [] # 추출한 지명 저장 변수

# 다시 일치하는 기사의 원문 가져오기
for num in art_count_list:
    print("article index : ", u_list[num])
    print(article_list[u_list[num]])
    print()

    # 여기서 지명 추출
    for i in local_list:
        numl = article_list[u_list[num]].find(i)
        if numl != -1:
            print(i)
            # case 강원도
            if i == '강원':
                for loc in KW:

                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('강원도')
                        result_loc.append(loc)

            # case 경기도
            if i == '경기':
                for loc in GGD:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        print(idate = int(filter(str.isdigit,u_list[num])))
                        result_loc.append('경기도')
                        result_loc.append(loc)

# local_list = ["경기", "강원", "광주", "경북", "경남", "대구", "대전", "부산", "서울", "세종", "울산", "인천", "전남", "전북", "제주", "충남", "충북" ]

            # case 경상남도 GSND
            if i == '경남':

                for loc in GSND:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('경상남도')
                        result_loc.append(loc)

            # case 경상북도 GSBD
            if i == '경북':

                for loc in GSBD:
                    #loc_num = article_list[u_list[num]].find(loc) # 날짜 추출
                    if loc_num!= -1:
                        result_loc.append('경상북도')
                        result_loc.append(loc)

            # case 광주 GJ
            if i == '광주':
                for loc in GJ:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('광주광역시')
                        result_loc.append(loc)

            # case 대구 JG
            if i == '대구':
                for loc in DG:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('대구광역시')
                        result_loc.append(loc)

            # case 대전 DJ
            if i == '대전':
                for loc in DJ:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('대전광역시')
                        result_loc.append(loc)

            # case 부산 BS
            if i == '부산':
                for loc in BS:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('부산광역시')
                        result_loc.append(loc)

            # case 서울 SO
            if i == '서울':
                for loc in SO:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('서울특별시')
                        result_loc.append(loc)

            # case 세종 SJ
            if i == '세종':
                for loc in SJ:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('세종특별자치시')
                        result_loc.append(loc)

            # case 울산 US
            if i == '울산':
                for loc in US:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('울산광역시')
                        result_loc.append(loc)

            # case 인천 IC
            if i == '인천':
                for loc in IC:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('인천광역시')
                        result_loc.append(loc)

            # case 전북 JB
            if i == '전북':
                for loc in JB:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('전라북도')
                        result_loc.append(loc)

            # case 전남 JN
            if i == '전남':
                for loc in JN:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('전라남도')
                        result_loc.append(loc)

            # case 충북 CB
            if i == '충북':
                for loc in CB:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        #loc_num = article_list[u_list[num]].find(loc) # 날짜 추출
                        print(loc_num)
                        result_loc.append('충청북도')
                        result_loc.append(loc)

            # case 충남 CN
            if i == '충남':
                for loc in CN:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('충청남도')
                        result_loc.append(loc)

            # case 제주 JJ
            if i == '제주':
                for loc in JJ:
                    loc_num = article_list[u_list[num]].find(loc)
                    if loc_num!= -1:
                        result_loc.append('제주특별자치도')
                        result_loc.append(loc)


            article_list[u_list[num]].find(i)







#===================================================================================

size = len(result_loc)/2

print_out = []
for_cnt = 0
for i in range(0, int(size)):
    print_out.append(result_loc[for_cnt] + ' ' + result_loc[for_cnt+1])
    for_cnt +=2


#==============================================================================
# 파일 쓰기
out_name = str(yyy) + str(mmm) + 'adress.txt'
#print(out_name)

# ============================================================================

# 얻은 지명 리스트를 파일로 작성하기
fw = open(out_name, mode='wt', encoding = 'utf-8')
for i in range(len(print_out)):
    fw.write(print_out[i] + '\n')
fw.close()
