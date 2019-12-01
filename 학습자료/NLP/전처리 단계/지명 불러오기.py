# 제주특별자치도지명 리스트 준비
JJ=[]
file=open('C:\\Python\\source\\adress_db\\제주특별자치도list.txt','rt' , encoding='UTF-8')

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
