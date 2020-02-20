# 미로

'''
3 --- tc
5 --- N by N
13101
10101
10101
10101
10021

0 --- road
1 --- wall
2 --- start
3 --- goal
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global maze
    if maze[x][y] == '3':
        return 1

    maze[x][y] = '1'
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 벽 밖을 탈출하지 않는 경우에만 실행
        if 0 <= nx < len(maze) and 0 <= ny < len(maze) and maze[nx][ny] != '1':
            if dfs(nx, ny) == 1:
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]

    # start_point 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                start_x = i
                start_y = j

    result = dfs(start_x, start_y)
    print(f'#{tc} {result}')