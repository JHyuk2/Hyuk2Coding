# 백준 연구소문제
import time
start = time.time()

"""
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2

7 3
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2

7 4
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
"""

def find_step(ix, iy, idx):
    # 최대거리를 저장하는 steps과 비교하기 위해 사용
    global steps
    global min_time
    global flag

    check[ix][iy] = 1
    if data[ix][iy] > steps:
        if min_time > 0 and min_time == steps:
            flag = -1
        steps = data[ix][iy]

    # 시계방향으로 위/오/아/왼 네 방향 탐색을 위한 dx, dy설정
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 네 방향 탐색을 하며 값을 더해줌
    for i in range(4):
        nx = ix + dx[i]
        ny = iy + dy[i]
        # 벽을 뚫고 넘어가면 실행되지 않게 조정
        # 0 <= x < size 이기 때문에 --- 0 미만이거나, size 이상이면 전부 에러
        if nx < 0 or ny < 0 or nx >= size or ny >= size: 
            continue

        # 진행 가능한 범위 내에 있는 경우
        else:
            # 이미 다른곳에서 진행하여 check 되었다면, 그 거리가 최단거리이기 때문에 진행할 필요 없음. (벽진행x)
            if check[nx][ny] == True or data[nx][ny] == -1:
                continue
            else:
                if data[nx][ny] > 0 :
                    queue.append([nx, ny])
                    continue
                data[nx][ny] = data[ix][iy] + 1
                queue.append([nx, ny])

def false_check():
    for i in range(size):
        for j in range(size):
            # 순회를 할 수 없는데 전파가 될 수 없는경우
            if data[i][j] == 0 and check[i][j] == 0:
                return False
    else:
        return True


size, n = map(int, input().split())
origin_data = [list(map(int, input().split())) for _ in range(size)]

from itertools import combinations
from copy import deepcopy
from collections import deque
from pprint import pprint as pp

start_points = []

# 1) 시작지점들(2->-1)과 벽(1->-1)을 찾고 바꾸기
for i in range(size):
    for j in range(size):
        if origin_data[i][j] == 2:
            start_points.append([i, j])
            origin_data[i][j] = -1            
        elif origin_data[i][j] == 1:
            origin_data[i][j] = -1

start_points_combi = combinations(start_points, n)

# 3) check 리스트를 만들고, start_points와 새로 만들어진 data를 통해 탐색진행

# 시작지점으로부터 하나씩 진행!
queue = deque()

min_time = -1 # 결과저장용
flag = 1

for idx, starts in enumerate(start_points_combi):
    check = [[0]*size for _ in range(size)]
    steps = 0
    data = deepcopy(origin_data)
    
    for s in starts:
        queue.append(s)
        x, y = s
        data[x][y] = 0

    while len(queue):
        cur_step = queue.popleft()  # ex) cur_step = [1, 2]
        ix, iy = cur_step
        if check[ix][iy] == True:
            continue
        find_step(ix, iy, idx)
        if flag==-1:
            break

    # queue가 비어있게 되면 탈출.
    if false_check():
        if min_time == -1:
            min_time = steps
        elif steps < min_time:
            min_time = steps

print(min_time)