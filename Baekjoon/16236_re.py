# 아기 상어 문제
# 첫 줄 입력 N (N x N 사이즈의 맵)

# 상어 입력받았고
N = int(input())
maps = []
for i in range(N):
    temp = list(map(int, input().split()))
    # 입력하면서 상어의 현재위치(9) 찾기
    if 9 in temp: 
        start_x = temp.index(9)
        start_y = i
    maps.append(temp)

# Rules
# 1) 자기보다 큰 물고기는 지나갈 수 없음
# 2) 자기보다 작은 물고기만 먹을 수 있음.
# 3) 먹을 수 있는 물고기가 2 이상인 경우, 가장 가까운 물고기를 먹음
# 4) 가장 가까운 물고기가 2 이상인 경우, 가장 위에 있는 물고기 -> 그 중에서도 가장 왼쪽에 있는 물고기를 먹는다.
# 5) 물고기는 자신의 크기와 같은 숫자의 물고기를 먹으면 size up!

# My Logics
# 1) 먹을 수 있는 물고기를 찾는다. (완전탐색으로 search)
# 2) 1번이 True인 경우, 물고기까지 갈 수 있는지 search (BFS로 갈 수 있는지 탐색 + 시간까지 한번에)
# 3) 각 물고기의 좌표정보 + 시간을 리스트로 묶어서 저장
# 4) 물고기를 얼마나 먹었는지 counter도 필요하겠네. size가 달라지면 먹을 수 있는 게 많아지니까.

size = 2 # 아기상어 시작 크기
count = 0 # 현재 사이즈와 count가 같아지는 경우, size up, count = 0 초기화

# 상하좌우 이동을 위한 x, y좌표계
x = [0, 1, 0, -1]
y = [1, 0, -1, 0]

# 먹을 수 있는 물고기가 존재하는가?
def is_exists(size):
    global N
    res = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] < size:
                res.append([i, j])
    return res

# BFS
def bfs(start_x, start_y):
    
    