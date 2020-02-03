tmp =[[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]]
tmp2 = [[True]*4]*4


# Q의 좌표를 받았을 때 가로,세로,대각을 False로 만드는 함수
def turn(tmp, pos):
    x = pos[0]
    y = pos[1]

    for i in range(len(tmp)):
        if i == x:
            tmp[i] = [False]*len(tmp)
        else:
            for j in range(len(tmp)):
                if j == y or (j-i == y-x) or (i+j == x+y):
                    tmp[i][j] = False
        tmp[x][y] = 'Q'
    print(tmp)
    return tmp

tmp_list = turn(tmp, (0,0))
for i in range(len(tmp_list)):
    for j in range(len(tmp_list)):
        print(tmp_list[i][j], end = ' ')
    print()

print('-'*30)

tmp2_list = turn(tmp2, (0, 0))
for i in range(len(tmp2_list)):
    for j in range(len(tmp2_list)):
        print(tmp2_list[i][j], end = ' ')
    print()
