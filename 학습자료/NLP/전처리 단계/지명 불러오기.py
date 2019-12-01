# 경상북도 지명 리스트 준비
GSBD=[]
file=open('C:\\Python\\source\\adress_db\\경상북도list.txt','rt' , encoding='UTF-8')

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
