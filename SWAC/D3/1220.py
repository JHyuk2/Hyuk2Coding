## 즉, 인덱스가 0~6까지 있으면 0 -> 6 (0+6) -> 1(8, 15) -> 5 -> 2 -> 4 의 순서로 순회해야 한다.

'''
1 0 0 0 0 0 2 
0 0 0 0 1 2 0
0 0 1 0 2 0 1
1 0 0 0 0 0 0
0 0 0 1 0 2 0
2 1 2 0 0 0 0
0 0 0 2 0 0 0
'''
def check_magnet(tmp_list):

    N = len(tmp_list)
    rotate_tmp = list(map(list, zip(*tmp_list)))


    # print('-----------after magnet------------------------------')

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
        
    # new_tmp = list(map(list, zip(*rotate_tmp)))
    return remain


## 문제에서 요구하는 바는, 몇 개가 남아있냐가 아니라, 몇 개의 교착상태가 존재하느냐.
for test_case in range(10):
    N = int(input())
    tmp_list = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        tmp_list.append(tmp)
    
    magnet = check_magnet(tmp_list)
    print(f'#{test_case+1} {magnet}')