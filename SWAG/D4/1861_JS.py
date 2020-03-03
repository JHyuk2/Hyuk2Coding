# 정사각형 방
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def get_result(x, y):
    value = [0] * 4
    for i in range(4):
        if x + dx[i] in range(N) and y + dy[i] in range(N):
            value[i] = room[x + dx[i]][y + dy[i]]
    if room[x][y] + 1 not in value:
        distance[x][y] = 1
    else:
        if not distance[x][y]:
            i = value.index(room[x][y] + 1)
            distance[x][y] = get_result(x + dx[i], y + dy[i]) + 1
    return distance[x][y]
    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    max_distance = 1
    min_size = N*N
    for i in range(N):
        for j in range(N):
            size = room[i][j]
            temp = get_result(i, j)
            if temp > max_distance:
                max_distance = temp
                min_size = size
            elif temp == max_distance:
                if size < min_size:
                    min_size = size
    print(f'#{tc} {min_size} {max_distance}')