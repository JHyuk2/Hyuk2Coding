# Magnetic

'''
----------------N극(1)
1 0 0 0 0 0 0 
0 0 0 0 1 2 0
0 0 0 0 0 0 0
1 0 0 0 0 0 0
0 0 0 1 0 0 0
2 0 2 0 0 0 0
0 0 0 2 0 0 0 
----------------S극(2)
'''

def magnetic(tmp_list):
    ## 양쪽이 같이 움직이면 좋겠지만, 한 작업엔 한개씩만 움직일 수 있음.
    # 1) N극에 가까운 N들 움직이기.
    N = len(tmp_list)

    for x in range(N):
        for y in range(N):
            if tmp_list[x][y] == 1 and y+1 = N: # 마지막일 때
                tmp_list[x][y] = 0

            elif tmp_list[x][y] == 1 and tmp[x][y+1] == 0:
                tmp_list[x][y] = 0
                tmp_list[x][y+1] = 1

            elif tmp_list[x][y] ==2 and y ==0:
                tmp_list[x][y] = 0

            elif tmp_list[x][y] == 2 and tmp[x][y-1] == 0:
                tmp_list[x][y] = 0
                tmp_list[x][y-1] = 2
    return tmp_list # 남아있는 개수.

for test_case in range(2):
    