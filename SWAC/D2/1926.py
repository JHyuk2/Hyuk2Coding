## 369 게임 만들기.
# 1 2 - 4 5 - 7 8 - 10 11 12 - 14 15 - ... 28 - - - - --

t = int(input())
clap = ['3', '6', '9']
result = ''

for i in range(1, t+1):
    tmp = str(i)
    count = 0

    if tmp == '1':
        result += tmp
    else:
        for t in tmp:
            if t in clap:
                count +=1
            
        if count != 0:
            result += ' '+ '-'*count
        else: # count !=0:
            
            result += ' ' +tmp

print(result)