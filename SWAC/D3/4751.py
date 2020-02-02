
T = int(input())

for test_case in range(1, T+1):
    char = list(input())

    width = (len(char) -1)*4 + 5
    result = []

    for i in range(5):
        tmp = ''
        for j in range(width):
            if i == 0 or i == 4:
                if (j % 4) == 2:
                    tmp += '#'
                else:
                    tmp += '.'
            elif i % 2 : # 1 or 3  
                if j % 2:
                    tmp += '#'
                else:
                    tmp += '.'
            else: # i == 2(middle)
                if not j%4 :
                    tmp += '#'
                elif j%4 == 2:
                    tmp += char[j//4]
                else:
                    tmp += '.'
        result.append(tmp)
    
    for i in range(len(result)):
        for j in range(width):
            print(result[i][j], end ='')
        print()