# DFS
# 배추벌레

T = int(input())

def dfs(cabbage, pos, cnt):
    y, x = pos
    stack = [(y, x)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while stack:
        temp = stack.pop()
        temp_y, temp_x = temp
        cabbage[temp_y][temp_x] = 0

        for i in range(4):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            
            if (0 <= ny < len(cabbage)) and (0 <= nx < len(cabbage[0])) and cabbage[ny][nx]:
                stack.append((ny, nx))
    else:
        return cnt + 1

for tc in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    stack = []

    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1

    for y in range(N):
        for x in range(M):
            if cabbage[y][x]: # 배추가 있으면
                count = dfs(cabbage, (y, x), count)

    print(count)