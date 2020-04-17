# import sys
# sys.stdin = open('input.txt')
'''
'''

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    stack = [(x, y)]
    
    while stack:
        start = stack.pop()
        start_x = start[0]
        start_y = start[1]

        for i in range(8):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            if 0 <= nx < 10 and 0<= ny < 10 and star_map[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))
    # stack소진시
    else:
        cnt +=1

for tc in range(int(input())):
    star_map = [list(map(int, input().split())) for _ in range(10)]
    cnt = 0
    visited = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(10):
        for j in range(10):
            if star_map[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
    print(f'#{tc+1} {cnt}')