# 아기 상어
from collections import deque

n = int(input())
grid = []
size = 2
distance = 0

# 그리드 생성 및 아기상어 위치 찾기
for y in range(n):
    temp = list(map(int, input().split()))
    if 9 in temp:
        x = temp.index(9) 
        # 초기 좌표 y, x, 사이즈 2
        pos = (y, x, size, distance)
    grid.append(temp)


# bfs 사용해서 거리탐색

# 나보다 작은 사이즈의 물고기가 있는지 확인하기
def find_eatable(grid):
    global n
    global size
    res = []
    for y in range(n):
        temp = list(map(lambda x: 1 if (x !=0 and x < size) else 0, grid[y]))
        for x in range(n):
            if temp[x]:
                res.append([y, x])
    return res

eatable = find_eatable(grid)
print(eatable)

def search(current):
    global n
    choices = []
    cur_y, cur_x, cur_size, dist = current
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[cur_y][cur_x] = 1
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    # 현재 위치로부터 탐색
    queue = deque()
    queue.append([cur_y, cur_x, cur_size, 0])

    while queue:
        y, x, size, dist = queue.popleft()
        
        # 만약 현재위치가 먹을 수 있는 곳이라면,
        if [y, x] in eatable and not visited[y][x]:
            choices.append([y, x, size, dist])
        visited[y][x] = 1

        # 4방향 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # index check
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                # 갈 수 있는 곳은 queue에 넣어주기
                queue.append([ny, nx, size, dist+1])

    return choices        

choice_list = search(pos)
# 거리가 가까운 순 - y값이 작은 순 - x값이 작은 순
sorted_choices = sorted(choice_list, key=lambda x:(x[3], x[1], x[0]))

print(sorted_choices)