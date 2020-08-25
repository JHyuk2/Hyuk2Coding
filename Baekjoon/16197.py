from pprint import pprint as pp

# 두 동전
# .: 공백, #: 벽, o: 동전
x, y = map(int, input().split())
area = [[-1 for _ in range(y+2)] for _ in range(x+2)] # 테두리에 벽을 세우고 시작한다.

# 1) 가장 바깥쪽을 -1 로 설정하여 테두리를 감싼다.
# 2) bfs를 적용하여 동전 하나만 -1을 만나는 때를 count. 그 외의 경우는 경로에서 제외한다.
# 3) 10회를 넘어가거나 bfs 큐에 남아있는게 없는 경우 -1을 출력한다.

# 1. 동전 위치 찾기

loc = []
for i in range(x):
    tmp = list(input())
    area[i+1] = [-1] + tmp + [-1]
    if 'o' in tmp:
        tmp_y = tmp.index('o')
        loc.append([i, tmp_y])

# 동전의 위치로부터 bfs를 적용하여 탐색한다.
# constraint. 두 동전은 한번에 움직인다.



# 1) 이전의 동전위치가 각각 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

