# 벽돌깨기
# 필요해 보이는 것부터 나열하자
# 1) 천장 찾기.
# 2 - 1) n만큼 상하좌우 부수기  - 함수화
# 2 - 2) 연쇄반응 일으키기
# 3) 아래로 당기기
# 4) bfs로 경우의수 나열하기.

'''
1
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
'''
from copy import deepcopy

# 모든 작업 실행은 시계방향 90도 회전상태에서 진행
# 1) 구슬 시작지점 찾기 
def find_starts(data_list):
    tmp_list = []
    for idx, tmp_data in enumerate(data_list):
        if tmp_data.count(0):
            tmp_list.append([idx, tmp_data.index(0)-1])
    start_list = sorted(tmp_list)
    return start_list

# 2) 구슬 연쇄반응
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bomb(x, y, r, arr):
    global W, H
    if r == 1:
        arr[x][y] = 0
        return arr
    else:
        arr[x][y] = 0
        for i in range(4):
            for j in range(1, r):
                nx = x + dx[i]*j
                ny = y + dy[i]*j
                if 0 <= nx < W and 0 <= ny < H:
                    bomb(nx, ny, arr[nx][ny], arr)

# 3) 남은거 당기기
def drop_bead(data_list):
    for i in range(len(data_list)):
        tmp = [j for j in data_list[i] if j != 0]
        data_list[i] = tmp + (len(data_list[i]) -len(tmp)) * [0]
    return data_list
    

for tc in range(1, 1+int(input())):
    bead, W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]
    # 시계방향으로 90도 돌려서 진행
    trans_data = list(map(list, (zip(*reversed(data)))))
    start_list = find_starts(trans_data)
    print(start_list)
    trans_copy = deepcopy(trans_data)

    bomb(0, 8, trans_copy[0][8], trans_copy)
    for i in range(len(data)):
        print(trans_copy[i])
    print('------------------')
    bomb(2, 2, trans_copy[2][2], trans_copy)
    for i in range(len(data)):
        print(trans_copy[i])

