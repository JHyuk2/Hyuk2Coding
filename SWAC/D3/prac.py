## 처음부터 다시풀자.

# tmp_list = [[0 for j in range(6)] for i in range(6)]
# tmp_list[0] = [1, 1, 1, 0, 2, 2]
# tmp_list[1] = [0 for _ in range(6)]
# tmp_list[3] = [2, 2, 0, 0, 1, 1]
# tmp_list[5] = [1, 2, 1, 0 ,0, 1]

'''
1 0 0 0 0 0 0 0 2 0 0 0 1 0 1
0 0 0 0 0 0 0 0 0 0 1 0 0 2 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 2 0 0 0 0 1 2 0 0 0 0 0
0 0 0 0 2 0 2 0 0 0 2 0 0 0 0
0 0 2 0 0 0 1 1 1 0 0 0 0 0 0
0 1 1 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 2 0 1 0 0 0 0 0 1
0 0 0 0 1 0 0 0 0 0 0 0 1 0 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 2
0 0 0 0 0 1 2 0 0 1 0 0 0 2 0
0 1 0 2 0 0 0 0 0 0 0 0 0 0 1
0 0 0 2 2 0 2 0 0 0 0 2 0 2 0
'''


tmp_list = []
for i in range(15):
    tmp = list(map(int, input().split()))
    tmp_list.append(tmp)

print('-----------tmp------------------------------')

N = len(tmp_list)
for i in range(N):
    for j in range(N):
        print(tmp_list[i][j], end = ' ')
    print()



## 두번 반전한 결과는 똑같다. (상관무)
## 

rotate_tmp = list(map(list, zip(*tmp_list)))


print('-----------after magnet------------------------------')

remain = 0
for i in range(N):
    for j in range(N):
        if rotate_tmp[i][j] == 1 and j+1 < N: # 어짜피 j+1 == N(마지막) 인 경우, 버려야 할 값이다.
            if 2 in rotate_tmp[i][j+1:]: # 카운트 될 경우 remain.
                remain += 1
                rotate_tmp[i][j] = 1
            else:
                rotate_tmp[i][j] = 0
        elif rotate_tmp[i][j] == 2 and j > 0: # j == 0또한 버려야 할 값.
            if 1 in rotate_tmp[i][:j]:
                remain +=1
                rotate_tmp[i][j] = 2   
            else:
                rotate_tmp[i][j] = 0
        else:
            rotate_tmp[i][j] = 0
    
new_tmp = list(map(list, zip(*rotate_tmp))) 

for i in range(N):
    for j in range(N):
        print(new_tmp[i][j], end = ' ')
    print()
